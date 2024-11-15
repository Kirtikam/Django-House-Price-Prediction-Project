from django.shortcuts import render;
from django.http import HttpResponse
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
def home(request):
 return render(request,"home.html")

def predict(request):
 return render(request,"predict.html")

def result(request):
  hr=pd.read_csv(r"C:\Users\Dell\3D Objects\ML\Housing.csv")
  from sklearn.preprocessing import LabelEncoder
  le=LabelEncoder()
  for i in range(0,hr.shape[1]):
    if hr.dtypes[i]==object:
        hr[hr.columns[i]]=le.fit_transform(hr[hr.columns[i]])
  sc=StandardScaler()
  x=hr.drop(['price'],axis=1)
  y=hr['price']
  x=sc.fit_transform(x)
  x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
  m1=LinearRegression()
  m1.fit(x_train,y_train)
  n1=float(request.GET['area'])
  n2=float(request.GET['bedrooms'])
  n3=float(request.GET['bathrooms'])
  n4=float(request.GET['stories'])
  n5=float(request.GET['parking'])
  s1=request.GET['basement']
  if s1=="yes":
      n6=1
  elif s1=="no":
      n6=0
  s2=request.GET['mainroad']
  if s2=="yes":
      n7=1
  elif s2=="no":
      n7=0
  s3=request.GET['guest_room']
  if s3=="yes":
      n8=1
  elif s3=="no":
      n8=0 
  s4=request.GET['hotwatering']
  if s4=="yes":
      n9=1
  elif s4=="no":
      n9=0
  s5=request.GET['airconditioning']
  if s5=="yes":
      n10=1
  elif s5=="no":
      n10=0
  s6=request.GET['prefarea']
  if s6=="yes":
      n11=1
  elif s6=="no":
      n11=0
  s7=request.GET['furnishing_status']
  if s7=="furnished":
     n12=0
  elif s7=="semi-furnished":
     n12=1
  elif s7=="unfurnished":
    n12=2
  pred=m1.predict([[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12]])
  price=round(pred[0])
  return render(request,"predict.html",{"result":price})
