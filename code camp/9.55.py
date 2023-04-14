import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# read
data = pd.read_csv('IDS_Assignment_2_traindata1.csv')
data1 = pd.read_csv('IDS_Assignment_2_traindata.csv')

# drop
data1 = data1.drop(pd.Series(data.sample(20).index))

# spilt
X = data.drop(columns=['Result'])
y = data['Result']

# spilt
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train
model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy rate：", accuracy)


###
##data = pd.read_csv('IDS_Assignment_2_traindata1.csv')
##data1 = pd.read_csv('IDS_Assignment_2_traindata.csv')
##
##data1['Result'].replace(['yes', 'no'], [1, 0], inplace=True)
##
### drop
##data1 = data1.drop(pd.Series(data.sample(20).index))
##X = data1.iloc[:, 0:19]
##Y = data1.iloc[:, -1]
##best_features = SelectKBest(score_func=chi2, k=3)
##fit = best_features.fit(X, Y)
##df_scores = pd.DataFrame(fit.scores_)
##df_columns = pd.DataFrame(X.columns)
##
##features_scores = pd.concat([df_columns, df_scores], axis=1)
##features_scores.columns = ['Features', 'Score']
##print(features_scores.columns)
##features_scores.sort_values(by='Score')
##print(features_scores)
