import statsmodels.formula.api as sm
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/brand/OneDrive/Documents/ISM4402/datasets/gradedata.csv') #bringing in the csv file
#print(df.head())
#Before conversion to binary numeric
result1 = sm.ols(formula='grade ~ exercise + hours',data=df).fit() #defining a linear regression model for the first case
print(result1.summary()) #Getting the summary of the model
df['bGender'] = np.where(df['gender']=='female',1,0) #assigning 1 to female and 0 to male.
df = df.drop(['gender'], axis = 1) #dropping the gender column from the df
print(df.head()) #showing the new df
#After conversion to binary numeric variable
result = sm.ols(formula='grade ~ bGender + exercise + hours',data=df).fit() #Making the model including gender

print(result.summary()) #printing the summary for the second model that includes gender as a binary numeric variable 

#Using a different library for the regression
print('----') 
from sklearn.linear_model import LinearRegression #importing the sklearn linear regression function

print('Sklearn model')
print('Model without gender')
X1 = df.drop(['grade','fname','lname','address','bGender'], axis= 1) #making the predictor tables 
Y1 = df['grade'] #only assigning the grades column as the y value or our target variable
reg1 = LinearRegression().fit(X1,Y1) #making the first model from before in this new library to see if anything changes
print(reg1.score(X1,Y1)) #Getting the R^2 for the first model. This is not the adjusted R^2. It is just the R^2
print('Model with gender') #making the model with gender
X = df.drop(['grade','fname','lname','address'], axis = 1)
Y = df['grade']
reg = LinearRegression().fit(X, Y)

print(reg.score(X, Y)) #This is not the adjusted R^2. It is just the R^2

#As we can see, nothing really changes when we add gender. The R^2 increaded to 0.665 but the adjusted R^2 remains at 0.664. 
#Adjusted R^2 adjust for the number of predictors that we have. This is the prefered metric for us. 

