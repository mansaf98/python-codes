import pandas as pd
import xlrd as rd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
import random
##############################################################################################
number_of_colors = 250
color = ["#"+''.join([random.choice('0123456789ABCDEF')
                     for j in range(6)])for i in range(number_of_colors)]
deaths_by_risk_factors = pd.read_csv(
    'number-of-deaths-by-risk-factor.csv').round()
(deaths_by_risk_factors.groupby(['Year']).sum()).plot(
    xticks=list(range(1990, 2018)), title='Number of deaths by risk factor, World, 2017: Total annual number of deaths by risk factor, measured across all age groups and both sexes.', color=color)
plt.show()
share_of_deaths_from_smoking = pd.read_csv(
    'share-deaths-smoking.csv').round()
share_of_deaths_from_smoking = share_of_deaths_from_smoking.dropna()
share_of_deaths_from_smoking = share_of_deaths_from_smoking.pivot(
    index='Code', columns='Year', values='Smoking (IHME, 2019)')
share_of_deaths_from_smoking.sort_values(by=[2017], ascending=False).plot(
    kind='bar', color=color, title='Share of deaths from smoking, 1990 to 2017', xlabel='Country', ylabel='%')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()
death_rate_from_smoking = pd.read_csv(
    'death-rate-smoking.csv').round()
death_rate_by_cont = death_rate_from_smoking.loc[death_rate_from_smoking['Code'].isnull(
)]
death_rate_by_cont = death_rate_by_cont.drop(['Code'], axis=1)
death_rate_by_cont = death_rate_by_cont.pivot(
    index='Entity', columns='Year', values='Deaths')
death_rate_by_cont.sort_values(by=[2017], ascending=False).plot(kind='bar', color=color, title='Death rate from smoking, 1990 to 2017 sorted by contenint and wealth',
                                                                xlabel='Country', ylabel='The annual number of deaths attributed to smoking per 100,000 people.')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()
smoking_death_by_age = pd.read_csv(
    'smoking-deaths-by-age.csv').round()
smoking_death_by_age = smoking_death_by_age.dropna()
smoking_death_by_age = smoking_death_by_age.loc[smoking_death_by_age['Year'] == 2017]
smoking_death_by_age = smoking_death_by_age.drop(
    ['Year', 'Code', 'Entity'], axis=1)
smoking_death_by_age = smoking_death_by_age.T
smoking_death_by_age.loc[:, 'Row_Total'] = smoking_death_by_age.sum(
    numeric_only=True, axis=1)
smoking_death_by_age.plot.pie(
    y='Row_Total', title='Death rates from smoking by age, World, 2017')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
death_rate_from_smoking = pd.read_csv(
    'death-rate-smoking.csv').round()
death_rate_from_smoking = death_rate_from_smoking.dropna()
death_rate_from_smoking = death_rate_from_smoking.loc[
    death_rate_from_smoking['Year'].isin([1990, 2017])]
death_rate_from_smoking = death_rate_from_smoking.pivot(
    index='Code', columns='Year', values='Deaths')
death_rate_from_smoking = death_rate_from_smoking.reset_index()
ax = death_rate_from_smoking.plot(
    x=2017, y=1990, kind='scatter', figsize=(10, 10))
death_rate_from_smoking[[2017, 1990, 'Code']].apply(
    lambda x: ax.text(*x), axis=1)
x = np.random.rand(100)
y = np.random.rand(100)
t = np.arange(100)
x = np.linspace(0, 270, 100)
y = x
plt.plot(x, y, '-r')
plt.title('Smoking death rate in 1990 vs. 2017')
plt.xlabel('Smoking death rate in 2017', color='#1C2833')
plt.ylabel('Smoking death rate in 1990', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
smoking_deaths = pd.read_csv(
    'smoking-deaths-1990-2017.csv').round()
smoking_deaths = smoking_deaths.loc[smoking_deaths['Year'].isin(
    list(range(1990, 2017)))]
smoking_deaths = smoking_deaths[smoking_deaths.Entity != 'World']
smoking_deaths = smoking_deaths.drop(
    ['Entity', 'Code', 'Year.1', 'Deaths - Smoking - Sex: Both - Age: All Ages (Number).1'], axis=1)
smoking_deaths = smoking_deaths.dropna()
smoking_deaths = smoking_deaths.pivot_table(index='Year', columns='Income classifications (World Bank (2017))',
                                            values='Deaths - Smoking - Sex: Both - Age: All Ages (Number)')
smoking_deaths.plot()
plt.title('Smoking death numbers by income status')
plt.xlabel('year', color='#1C2833')
plt.ylabel('number of deaths', color='#1C2833')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.grid()
plt.show()
smoking_shares = pd.read_csv(
    'share-of-adults-who-smoke.csv').round()
smoking_shares = smoking_shares.pivot_table(
    index='Code', columns='Year', values='Prevalence of current tobacco use (% of adults)')
smoking_shares.sort_values(by=[2018], ascending=False).plot(
    kind='bar', color=color, title='Share of adults who smoke, 2007 to 2018', xlabel='Country', ylabel='%')
plt.grid()
plt.show()
smoking_shares_cont = pd.read_csv(
    'share-of-adults-who-smoke.csv').round()
smoking_shares_cont = smoking_shares_cont.loc[smoking_shares_cont['Code'].isnull(
)]
smoking_shares_cont = smoking_shares_cont.drop(['Code'], axis=1)
smoking_shares_cont = smoking_shares_cont.pivot_table(
    index='Entity', columns='Year', values='Prevalence of current tobacco use (% of adults)')
smoking_shares_cont.sort_values(by=[2018], ascending=False).plot(
    kind='bar', color=color, title='countries sorted sorted by number of adults who smoke sorted by contenint', xlabel='Country', ylabel='year')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.grid()
plt.show()
men_v_women = pd.read_csv(
    'comparing-the-share-of-men-and-women-who-are-smoking.csv').round()
men_v_women = men_v_women.loc[men_v_women['Year'].isin([2016])]
men_v_women = men_v_women.drop(
    ['Total population (Gapminder, HYDE & UN)', 'Continent', 'Entity'], axis=1)
men_v_women = men_v_women.dropna()
men_v_women = men_v_women.reset_index()
ax = men_v_women.plot.scatter(x='Smoking prevalence, females (% of adults)',
                              y='Smoking prevalence, males (% of adults)')
men_v_women[['Smoking prevalence, females (% of adults)', 'Smoking prevalence, males (% of adults)', 'Code']].apply(
    lambda x: ax.text(*x), axis=1)
x = np.random.rand(100)
y = np.random.rand(100)
t = np.arange(100)
x = np.linspace(0, 50, 100)
y = x
plt.plot(x, y, '-r')
plt.title('Smoking in men vs. women, 2016')
plt.xlabel('Share of women', color='#1C2833')
plt.ylabel('Share of men', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
smoking_deaths = pd.read_csv(
    'smoking-deaths-1990-2017.csv').round()
cigarette_sales = pd.read_csv(
    'sales-of-cigarettes-per-adult-per-day.csv').round()
smoking_deaths = pd.read_csv(
    'smoking-deaths-1990-2017.csv').round()
smoking_deaths = smoking_deaths.dropna()
classi = smoking_deaths.set_index('Code').to_dict(
)['Income classifications (World Bank (2017))']
cigarette_sales = pd.read_csv(
    'sales-of-cigarettes-per-adult-per-day.csv').round()
cigarette_sales = cigarette_sales.dropna()
cigarette_sales['class'] = smoking_deaths['Code'].map(classi)
cigarette_sales = cigarette_sales.drop(['Entity', 'Code'], axis=1)
cigarette_sales = cigarette_sales.pivot_table(
    index='Year', columns='class', values='Sales of cigarettes per adult per day (International Smoking Statistics (2017)) ')
cigarette_sales.plot()
plt.title('Sales of cigarettes per adult per day, 1875 to 2015')
plt.xlabel('year', color='#1C2833')
plt.ylabel('number of cigarettes', color='#1C2833')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.grid()
plt.show()
adults_smoking = pd.read_csv(
    'adults-smoking-2000-2016.csv').round()
adults_smoking = adults_smoking.loc[
    adults_smoking['Year'].isin([2000, 2016])]
adults_smoking = adults_smoking.drop(
    ['Year.1', 'Entity', 'Smoking prevalence, total (ages 15+).1', 'Continent'], axis=1)
adults_smoking = adults_smoking.dropna()
adults_smoking = adults_smoking.pivot_table(
    index='Code', columns='Year', values='Smoking prevalence, total (ages 15+)')
adults_smoking = adults_smoking.reset_index()
print(adults_smoking)
ax = adults_smoking.plot(
    x=2016, y=2000, kind='scatter', figsize=(10, 10))
adults_smoking[[2016, 2000, 'Code']].apply(
    lambda x: ax.text(*x), axis=1)
x = np.random.rand(100)
y = np.random.rand(100)
t = np.arange(100)
x = np.linspace(0, 50, 100)
y = x
plt.plot(x, y, '-r')
plt.title('Share of adults who smoke in 2000 vs. 2016 The share of adults, aged 15 years and older, who smoke any tobacco product on a daily or non-daily basis.')
plt.xlabel('Share of adults who smoke in 2016', color='#1C2833')
plt.ylabel('Share of adults who smoke in 2000', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
