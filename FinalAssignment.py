#import libraries needed for code
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import sklearn.preprocessing as pre

#import the data
df = pd.read_csv('C:/Users/brand/OneDrive/Documents/ISM4402/datasets/axisdata.csv')

#print averages asked from the book
print('Average cars sold: ' + str(df['Cars Sold'].mean()))

print('Max cars sold: ' + str(df['Cars Sold'].max()))

print('Min cars sold: ' + str(df['Cars Sold'].min()))

print('')
#make new dataframe to make sorting and printing easier
gcs = df.groupby(['Gender']).mean()['Cars Sold']
gcs = gcs.reset_index()
print('Average cars sold by gender: ' + gcs.to_string(index = False,header = False))

print('')
print('Average hours worked: ' + str(df['Hours Worked'].mean()))

print('Average hours worked of people who sell more than 3 cars a month: ' + str(df[df['Cars Sold'] > 3]['Hours Worked'].mean()))

print()

print('Average years of experience: ' + str(df['Years Experience'].mean()))

print('Average years of experience of people who sell more than 3 cars a month: ' + str(df[df['Cars Sold'] > 3]['Years Experience'].mean()))

#make new dataframe to make sorting and printing easier
stcs = df.groupby(['SalesTraining']).mean()['Cars Sold']
stcs = stcs.reset_index()

print('Average cars sold by if they had sales training: ' + str(stcs.to_string(index= False,header = False)))

#Best indictator of good sales person is if they had training. 

#define binary variables
gender = {'M': 1,'F': 0}
Training = {'Y': 1,'N': 0}
#transform the columns to be numbers for corr plot.
df['bGender'] = [gender[item] for item in df['Gender']]
df['bTraining'] = [Training[item] for item in df['SalesTraining']]

#plot the plots 
corr = df.corr() 
sns.heatmap(corr)
plt.figure()
sns.barplot(x = gcs['Gender'],y = gcs['Cars Sold'],data = gcs)
plt.figure()
sns.barplot(x = stcs['SalesTraining'], y = stcs['Cars Sold'],data = stcs)