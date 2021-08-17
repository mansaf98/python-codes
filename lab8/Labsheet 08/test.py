import pandas as pd
import xlrd as rd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
movies = pd.read_excel('movies.xls')
genres = []
for ind in movies.index:
    genres.extend((movies['Genres'][ind]).split('|'))
genremovies = Counter(genres)
plt.pie(list(genremovies.values()), labels=list(genremovies.keys()),
        autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.title(
    'percentage of the movies for each Genre')
plt.show()
