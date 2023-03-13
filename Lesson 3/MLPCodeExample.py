from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('forestfires.csv')
df.head()
ds=df.drop(columns=['month', 'day'])
#ds1=df.drop(['month', 'day'], axis=1)
  
train, test =  train_test_split(ds,test_size=.3,train_size=.7)
#random_state=42
X_train = train.drop("area", axis=1).copy()
Y_train = pd.DataFrame()
Y_train['area'] = train["area"].copy()

X_test = test.drop("area", axis=1).copy()
 
Y_test = pd.DataFrame()
Y_test['area'] = test["area"].copy()
 
regr = MLPRegressor(random_state=1, max_iter=500).fit(X_train, Y_train)
regr.predict(X_test[:2])
PredANN=regr.predict(X_test)

PredANNdf = pd.DataFrame(PredANN)   
PredANNdf.to_csv('ANNPred.csv')
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
print("MSE:", mean_squared_error(PredANN, Y_test,squared=False))



def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

print("MAPE:", mean_absolute_percentage_error(PredANN, Y_test))
print("R2 Score", r2_score(PredANN, Y_test))
