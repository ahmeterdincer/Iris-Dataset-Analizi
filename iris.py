import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

#Veri Yükleme
veriler= pd.read_excel("Iris.xlsx")

x =veriler.iloc[:,1:4].values #Bagımsız değişkenler
y=veriler.iloc[:,4:].values#Bağımlı değişken


#Verilerin eğitim ve test için bölünmesi
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33, random_state=42)


#Verilerin ölçeklendirilmesi
sc= StandardScaler()
X_train= sc.fit_transform(x_train)
X_test= sc.transform(x_test)

#Buradan itibaren sınıflandırma algoritmaları başlıyor

#Logistic Regression Modelinin oluşturulması
from sklearn.linear_model import LogisticRegression
logr= LogisticRegression(random_state=42)
logr.fit(x_train,y_train)#Egitim

y_pred=logr.predict(x_test)#tahmin  

#Consfusion Matrix Oluşturulması
cm= confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n",cm)

#KNN algoritması
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1, metric='minkowski')
knn.fit(X_train, y_train)
y_pred= knn.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)


#SVC (SVM Classifier) algoritması
from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)

y_pred= svc.predict(X_test)
cm= confusion_matrix(y_test, y_pred)
print("SVM Confusion Matrix:\n",cm)


#Naive Bayes algoritması
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred= gnb.predict(X_test)
cm= confusion_matrix(y_test, y_pred)
print("Naive Bayes Confusion Matrix:\n",cm)

#Decision Tree Classifier algoritması
from sklearn.tree import DecisionTreeClassifier 
dtc=DecisionTreeClassifier(criterion='entropy')

dtc.fit(X_train,y_train)
y_pred=dtc.predict(X_test)

y_pred= dtc.predict(X_test)
cm= confusion_matrix(y_test, y_pred)
print("Decision Tree Confusion Matrix:\n",cm)

#Random Forest Classifier algoritması
from sklearn.ensemble import RandomForestClassifier
rfc= RandomForestClassifier(n_estimators=10, criterion='entropy')
rfc.fit(X_train,y_train)

y_pred=rfc.predict(X_test)

y_pred= rfc.predict(X_test)
cm= confusion_matrix(y_test, y_pred)
print("Random Forest Confusion Matrix:\n",cm)
