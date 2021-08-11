import pandas as pd
import xlrd as rd
import numpy as np
##############################################################################################
# task 1
df = pd.read_excel(
    r'C:\Users\yazan\OneDrive\Desktop\summer_2021\python\lab7\movies.xls')
print('uploaded the movies : ')
print(df)
# T1.1
print('average duration of movies is : ')
print(df['Duration'].mean())
# T1.2
print('heres the movies grouped by language and imbd score average : ')
print(df.groupby(['Language']).mean()['IMDB Score'])
# T1.3
print('heres list of english movies produced in spain : ')
print(df.loc[(df['Language'] == 'English') & (df['Country'] == 'Spain')])
# T1.4
print('the director of the Amigo movie is : ')
print(df[df['Title'].str.match('Amigo')]['Director'])
# T1.5
print('heres list of actors with the number of movies they where in ')
print(df.groupby(['Actor 1']).count()['Title'])
# T1.6
groupByMovies = (df.groupby(['Actor 1'])[
                 'Title'].count().reset_index(name='count'))
maxNum = groupByMovies.max()
print('actor with most starting roles is {} who started in {} movies '.format(
    maxNum[0], maxNum[1]))
# T1.7
print("actor James Franco films had a IMBD score of : ")
print(df.loc[df['Actor 1'] == 'James Franco'][['Title', 'IMDB Score']])
print("and a total budget of : ")
print(((df.loc[df['Actor 1'] == 'James Franco']
      [['Budget']]).sum()).to_string(index=False))
# T1.8
groupbyLang = df.groupby(['Language'])['Title'].count().reset_index(
    name='count')
div = int(groupbyLang['count'].sum())
eng = int((((groupbyLang.loc[groupbyLang['Language'] ==
                             'English']['count']).to_string(index=False))))
print("english makes {} % of all titles in the database ".format((eng/div)*100))
# T1.9
print("heres a list of all drama films in the database :\n  {} ".format(
    (df.loc[df['Genres'] == 'Drama']['Title']).to_string(index=False)))
# T1.10
q10 = df
q10.drop(['Facebook Likes - Actor 1', 'Facebook Likes - Actor 2'], axis=1)
print("removed columns : “Facebook Likes - Actor 1” and “Facebook Likes - Actor 2” from database ")
# T1.11
avg = q10["Budget"].mean()
q10['Budget'] = df['Budget'].fillna(avg)
print("all NaN values replaced with mean values which is {} ".format(avg))
# T1.12
q10.insert(len(q10.columns), 'Norm5_IMDB',
           q10['IMDB Score'], allow_duplicates=True)
q10['Norm5_IMDB'] = (q10['Norm5_IMDB']/q10['Norm5_IMDB'].abs().max())*5
print("added new column Norm5_IMDB and normalized all scores to 5 ")
# T1.13
q10 = q10.rename(columns={"IMDB Score": "Norm10_IMDB"})
print("renamed column IMBD score to Norm10_IMDB ")
# T1.14
q10.to_excel(
    r"C:\Users\yazan\OneDrive\Desktop\summer_2021\python\lab7\movies_updated.xlsx")
# task 2
detailed_answers_session_a = pd.read_excel(
    r'C:\Users\yazan\OneDrive\Desktop\summer_2021\python\lab7\detailed_answers_session_a.xlsx')
detailed_answers_session_b = pd.read_excel(
    r'C:\Users\yazan\OneDrive\Desktop\summer_2021\python\lab7\detailed_answers_session_b.xlsx')
grades = pd.read_excel(
    r'C:\Users\yazan\OneDrive\Desktop\summer_2021\python\lab7\grades.xlsx')
detailed_answers_session_a = detailed_answers_session_a.replace('-', np.nan)
detailed_answers_session_b = detailed_answers_session_b.replace('-', np.nan)
grades = grades.replace('-', np.nan)
# T2.1
count = pd.DataFrame(detailed_answers_session_a.count().filter(
    regex='Q'), columns=['count'])
max_value = int(count["count"].max())
print("heres the most answered question/s in sesseion A : \n {} ".format(
    (count.loc[count['count'] == max_value]).iloc[:, 0]))
# T2.2
avg = grades.fillna(0)
avg['year'] = avg['Student ID'].astype(str).str[0:2]
avg['average'] = (avg['Session_a'] + avg['Session_b'])
print("heres the average of the exam grouped by the year of the student : \n {} ".format(
    avg.groupby('year').mean()['average']))
# T2.3
print("{} students picked the answer a in the exam ".format(int((detailed_answers_session_a['Q12'].value_counts())[
      'a'])+int((detailed_answers_session_b['Q12'].value_counts())['a'])))
# T2.4
grades = grades.fillna(0)
grades['grade'] = grades['Session_a'] + grades['Session_b']
makeupabs = grades.loc[grades['grade'] == 0]
makeupA = detailed_answers_session_a.loc[detailed_answers_session_a.isnull(
).sum(axis=1)[0:] > 7]
makeupB = detailed_answers_session_b.loc[detailed_answers_session_b.isnull(
).sum(axis=1)[0:] > 7]
makeup = (makeupabs['Student ID'].tolist()) + \
    (makeupA['Student ID'].tolist()) + (makeupB['Student ID'].tolist())
print("the students that where absent from the exam or couldnt solve atleas seven questions are : {}".format(makeup))
