import pandas as pd
import xlrd as rd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
import random
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
