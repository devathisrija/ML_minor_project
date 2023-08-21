import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

#DATA HANDLING
data = pd.read_csv('temp.csv')
print(data.head())
print(data.describe())
X = data[["selfmargin"]]
Y = data["profit"]
Y_ = data["p/l"]

#DATA ANALYSIS
plt.scatter(X['selfmargin'], Y, color='b')
plt.xlabel('selfmargin')  
plt.ylabel('profit') 
plt.show()


#MULTIPLE LINEAR REGRESSION
X = data[['req','purch','marmargin','selfmargin']]
mdl = LinearRegression()
mdl.fit(X, Y)
pred = mdl.predict([[30,25,15,15]])
print("MULTIPLE LINEAR REGRESSION")
print("Predicted value (MLR): ",pred[0])
print("Accuracy (MLR): ",mdl.score(X[:100], Y[:100])*100)

plt.scatter(X['selfmargin'], Y, color='b')
plt.plot(X['selfmargin'], mdl.predict(X),color='black',linewidth=3)
plt.xlabel('req,comp,purch,marmargin,selfmargin')  
plt.ylabel('profit') 
plt.show()


#Naive Bayes
from sklearn.naive_bayes import GaussianNB
mdl = GaussianNB()
mdl.fit(X, Y_)
pred = mdl.predict([[40]])
print("Predicted value (NB): ",pred[0])
print("Accuracy (NB): ",mdl.score(X[:100], Y_[:100])*100)

plt.scatter(X['selfmargin'], Y_, color='b')
plt.plot(X['selfmargin'], mdl.predict(X),color='black',linewidth=3)
plt.xlabel('selfmargin')  
plt.ylabel('p/l') 
plt.show()

