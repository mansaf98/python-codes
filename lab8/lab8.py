import pandas as pd
import xlrd as rd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
##############################################################################################
# Task 1
sales = pd.read_excel('Sales.xlsx')
# T1.A
sales.groupby('month_number')['Total'].sum().plot(kind='line')
plt.title('total sales per month as a line plot')
plt.show()
# T1.B
t1b = plt.subplot()
t1b.stackplot(sales['month_number'].tolist(),
              sales['Milk'].tolist(), sales['Olives'].tolist(), sales['Sugar'].tolist(), sales['Rice'].tolist(), sales['Snacks'].tolist(), labels=['milk', 'olives', 'sugar', 'rice', 'snacks'])
t1b.legend(loc='upper left')
plt.title('stackplot that shows the sales per month')
plt.show()
# T1.C
sales.groupby('month_number')['Milk', 'Olives',
                              'Sugar', 'Rice', 'Snacks'].sum().plot(kind='bar', stacked=True)
plt.title('stackplot that shows the sales per month')
plt.show()
# T1.D
plt.pie((sales.values.tolist()[4])[1:6], labels=[
        'milk', 'olives', 'sugar', 'rice', 'snacks'], autopct='%1.1f%%', startangle=90)
plt.legend()
plt.title('percentage of sales for each product in May')
plt.show()
# T1.E
sales.plot(kind='line', x='month_number', y='Milk', ax=plt.gca())
sales.plot(kind='line', x='month_number', y='Olives', ax=plt.gca())
sales.plot(kind='line', x='month_number', y='Sugar', ax=plt.gca())
sales.plot(kind='line', x='month_number', y='Rice', ax=plt.gca())
sales.plot(kind='line', x='month_number', y='Snacks', ax=plt.gca())
plt.title('sales for each product across all months')
plt.show()
# T1.F
sales.plot(kind='bar', x='month_number', y='Milk', ax=plt.gca())
plt.title('milk sales for each quarter')
plt.show()
# Task 2
movies = pd.read_excel('movies.xls')
# T2.A
d = {}
for w in ((movies.groupby('Country')['Language'].apply(
        list))['China']):
    if w in d.keys():
        d[w] += 1
    else:
        d[w] = 1
plt.pie(list(d.values()), labels=list(d.keys()),
        autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.title('movies produced by China by language')
plt.show()
# T2.B
plt.pie((movies.groupby('Country')['Title'].count())[[
    'Spain', 'France', 'Canada', 'China']], labels=[
    'Spain', 'France', 'Canada', 'China'],
    autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.title(
    'movies produced by Spain, France, Canada, China by % of movies produced')
plt.show()
# T2.C
france = movies.loc[movies['Country'] == 'France']
plt.scatter(france['Budget'], france['IMDB Score'],
            s=france['Duration'], c='c', cmap='viridis', edgecolor='None')
plt.title(
    'relation between the budget and the IMDB score for movies produced by France')
plt.show()
# T2.D
genres = []
for ind in movies.index:
    genres.extend((movies['Genres'][ind]).split('|'))
genremovies = Counter(genres)
plt.pie(list(genremovies.values()), labels=list(genremovies.keys()),
        autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.title(
    'percentage of the movies for each Genre')
plt.show()
