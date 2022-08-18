# importing the necessary library :

import pandas as pd
import numpy as np
import sklearn
data = pd.read_csv("insurance_claims.csv")

print(data.info())       #for printing the information related to the data:

# droping or deleting the unnecessary columns from the dataframe:
data = data.drop(['months_as_customer', 'policy_number', 'auto_year'], axis=1)

#Now let's check that is there any missing value present in the dataframe.
data.isnull().any()
#there is missing value which is representd by the '?'
# We will replace that '?' by "nan" values: 
data = data.replace('?', np.NaN)

#  slicing of dataframe in two variables:
x = data.iloc[:, 0:-1]                    # independent variables
y = data['fraud_reported']                # dependent variables

#independent variables=which are used for the prediction of dependent variablrs from machine.
#dependent variables=the data, which we want that machine should be predict.
 
#conversion of data into numeric form by using label encoder, because machine knows only integers/numeric data:    
from sklearn.preprocessing import LabelEncoder

ls=LabelEncoder()
x["insured_sex"]=ls.fit_transform(x["insured_sex"])
le=LabelEncoder()
x["insured_education_level"]=le.fit_transform(x["insured_education_level"])
lo=LabelEncoder()
x["insured_occupation"]=lo.fit_transform(x["insured_occupation"])
lho=LabelEncoder()
x["insured_hobbies"]=lho.fit_transform(x["insured_hobbies"])
lr=LabelEncoder()
x["insured_relationship"]=lr.fit_transform(x["insured_relationship"])

lt=LabelEncoder()
x["incident_type"]=lt.fit_transform(x["incident_type"])

lse=LabelEncoder()
x["incident_severity"]=lse.fit_transform(x["incident_severity"])
lco=LabelEncoder()
x["authorities_contacted"]=lco.fit_transform(x["authorities_contacted"])

ld=LabelEncoder()
x["property_damage"]=ld.fit_transform(x["property_damage"])
lp=LabelEncoder()
x["police_report_available"]=lp.fit_transform(x["police_report_available"])
lm=LabelEncoder()
x["auto_make"]=lm.fit_transform(x["auto_make"])

'''
# label encoding of dependent variable:
lf=LabelEncoder()
y=lf.fit_transform(y)'''



#Now for filling missing value we had to call numpy 
from sklearn.impute import SimpleImputer
sI=SimpleImputer(missing_values=np.nan,strategy="mean") 
sI.fit(x.iloc[:,0:])
x.iloc[:,0:]=sI.transform(x.iloc[:,0:])

# standard Scaling is used to standarised the value like a same unit.    
from sklearn.preprocessing  import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)                         # backend formula= (x- x_means)/standard_deviation 
# there is no need of scaling for the y variable, because it has only two values.

# spliting of data for testing and training:
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
# we had to divide our dependent ande independent data into 4 variable 
# i.e 2 for testing and 2 for training from ech dependent and independent data.
# (independent_var, dependent_var,size of data used for testing ,random_state= for shuffling of data)


# BalancedBaggingClassifier
from imblearn.ensemble import BalancedBaggingClassifier 
from sklearn.ensemble import RandomForestClassifier
bbc= BalancedBaggingClassifier( sampling_strategy = 'auto',replacement = False,random_state = 0)
bbc.fit(x_train, y_train)
y_pred_bbc = bbc.predict(x_test)
print("Training Accuracy: ", bbc.score(x_train, y_train))
print('Testing Accuarcy: ', bbc.score(x_test, y_test))


# saving the variables of label encoders:
from joblib import dump, load

dump(ls,"insured_sex.joblib")
dump(le,"insured_education_level.joblib")
dump(lo,"insured_occupation.joblib")
dump(lho,"insured_hobbies.joblib")
dump(lr,"insured_relationship.joblib")
dump(lt,"incident_type.joblib")
dump(lse,"incident_severity.joblib")
dump(lco,"authorities_contacted.joblib")
dump(ld,"property_damage.joblib")
dump(lp,"police_report_available.joblib")
dump(lm,"auto_make.joblib")
#dump(lf,"y.joblib")
dump(sc,"StandardScaler.joblib")
dump(sI,"SimpleImputer.joblib")
dump(bbc,"BalancedBaggingClassifier.joblib")

