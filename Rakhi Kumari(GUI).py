import pandas as pd
import numpy as np
from joblib import load

#loading the columns:
insured_sex=load("insured_sex.joblib")
insured_education_level=load("insured_education_level.joblib")
insured_occupation=load("insured_occupation.joblib")
insured_hobbies=load("insured_hobbies.joblib")
insured_relationship=load("insured_relationship.joblib")
incident_type=load("incident_type.joblib")

incident_severity=load("incident_severity.joblib")
authorities_contacted=load("authorities_contacted.joblib")

property_damage=load("property_damage.joblib")
police_report_available=load("police_report_available.joblib")
auto_make=load("auto_make.joblib")
y=load("y.joblib")
StandardScaler=load("StandardScaler.joblib")
SimpleImputer=load("SimpleImputer.joblib")
BalancedBaggingClassifier=load("BalancedBaggingClassifier.joblib")

# taking a input from the user:
'''
new=pd.DataFrame({"age":[int(input("Enter the age of the customer ="))],"policy_deductable":[int(input("Enter the policy deductable value ="))],"policy_annual_premium":[float(input("Enter the annual premium value of policy ="))],"insured_zip":[int(input("Enter the value of the insured zip of your policy ="))],"insured_sex":[str(input("Enter the sex of the customer of the policy (FEMALE/MALE)="))],"insured_education_level":[str(input("Enter the education level of the customer ="))],"insured_occupation":[str(input("Enter the occupation of the  customer ="))],"insured_hobbies":[str(input("Enter the hobbies of the customers ="))],"insured_relationship":[str(input("Enter the relation of the customer ="))],"capital_gain":[int(input("Enter the value of capital gain ="))],"capital_loss":[int(input("Enter the value of the capital loss ="))],"incident_type":[str(input("Enter the type of the incident  ="))],"incident_severity":[str(input("Enter the detils of the incident severity ="))],"authorities_contacted":[str(input("Enter the contacted authorities ="))],"incident_hour_of_the_day":[int(input("Enter the time duration of the incident="))],"number_of_the_vehicles_involved":[int(input("Enter the number of the involved vehlicles="))],"property_damage":[str(input("Is there any damaged property (YES/NO) ="))],"bodily_injuries":[int(input("Enter the number of bodily injuries of the incident="))],"witnesses":[int(input("Enter the number of witnesses="))],"police_report_available":[str(input("Is there any police report available (YES/NO)="))],"total_claim_amount":[int(input("Enter the total claimed amount="))],"injury_claim":[int(input("Enter the total amount for injury claimed ="))],"property_claim":[int(input("Enter the total amount for property claimed ="))],"vehicle_claim":[int(input("Enter the total amount for vehicle claimed = "))],"auto_make":[str(input("Enter the brand of the vehicle = "))]})




new["insured_sex"]=ls.transform(new["insured_sex"])
new["insured_education_level"]=le.transform(new["insured_education_level"])
new["insured_occupation"]=lo.transform(new["insured_occupation"])
new["insured_hobbies"]=lho.transform(new["insured_hobbies"])
new["insured_relationship"]=lr.transform(new["insured_relationship"])
new["incident_type"]=lt.transform(new["incident_type"])
new["incident_severity"]=lse.transform(new["incident_severity"])
new["authorities_contacted"]=lco.transform(new["authorities_contacted"])
new["property_damage"]=ld.transform(new["property_damage"])
new["police_report_available"]=lp.transform(new["police_report_available"])
new["auto_make"]=lm.transform(new["auto_make"])
new=sc.transform(new)
new=sI.transform(new)


print("Is this insurance claim is Fraud or not: ",BalancedBaggingClassifier.predict(new))
'''

#FrontEnd Development by using Tkinter:
    
def disp():
    print("disp started")
    new=pd.DataFrame({"age":[int(s1.get())],"policy_deductable":[int(s2.get())],"policy_annual_premium":[float(s3.get())],"insured_zip":[int(s4.get())],"insured_sex":[str(s5.get())],"insured_education_level":[str(s6.get())],"insured_occupation":[str(s7.get())],"insured_hobbies":[str(s8.get())],"insured_relationship":[str(s9.get())],"capital_gain":[int(s10.get())],"capital_loss":[int(s11.get())],"incident_type":[str(s12.get())],"incident_severity":[str(s13.get())],"authorities_contacted":[str(s14.get())],"incident_hour_of_the_day":[int(s15.get())],"number_of_the_vehicles_involved":[int(s16.get())],"property_damage":[str(s17.get())],"bodily_injuries":[int(s18.get())],"witnesses":[int(s19.get())],"police_report_available":[str(s20.get())],"total_claim_amount":[int(s21.get())],"injury_claim":[int(s22.get())],"property_claim":[int(s23.get())],"vehicle_claim":[int(s24.get())],"auto_make":[str(s25.get())]})
    new["insured_sex"]=ls.transform(new["insured_sex"])
    new["insured_education_level"]=le.transform(new["insured_education_level"])
    new["insured_occupation"]=lo.transform(new["insured_occupation"])
    new["insured_hobbies"]=lho.transform(new["insured_hobbies"])
    new["insured_relationship"]=lr.transform(new["insured_relationship"])
    new["incident_type"]=lt.transform(new["incident_type"])
    new["incident_severity"]=lse.transform(new["incident_severity"])
    new["authorities_contacted"]=lco.transform(new["authorities_contacted"])
    new["property_damage"]=ld.transform(new["property_damage"])
    new["police_report_available"]=lp.transform(new["police_report_available"])
    new["auto_make"]=lm.transform(new["auto_make"])
    new=sc.transform(new)
    new=sI.transform(new)
    ans=BalancedBaggingClassifier.predict(new)
    l.config(text=ans[0])


   
from tkinter import *

root=Tk()
root.geometry("1400x1400")
root.title("Insurance claim Project.")
# assigning the variables to the different columns according to their datatypes:
 

bg = PhotoImage(file = r"C:\\Users\\desktop\\Downloads\\5559852-imresizer (1).png")
labelA1 = Label( root, image = bg)
labelA1.place(x =0, y =0)

    
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
s8=StringVar()
s9=StringVar()
s10=StringVar()
s11=StringVar()
s12=StringVar()
s13=StringVar()
s14=StringVar()
s15=StringVar()
s16=StringVar()
s17=StringVar()
s18=StringVar()
s19=StringVar()
s20=StringVar()
s21=StringVar()
s22=StringVar()
s23=StringVar()
s24=StringVar()
s25=StringVar()


label1=Label(root,text="Insurance Fraud prediction",fg="navy blue",bg="lightskyblue",font=("Castellar","25","bold")).place(x=600,y=20)

label2=Label(root,text="Enter the age of the customer: ",fg="black",font=("Californian FB","15")).place(x=50,y=100)
age=Entry(root,textvariable=s1,width=10).place(x=630,y=100,height=30)

label3=Label(root,text="Enter the policy deductable value: ",fg="black",font=("Californian FB","15")).place(x=50,y=140)
policy_deductable=Entry(root,textvariable=s2,width=10).place(x=630,y=140,height=30)

label4=Label(root,text="Enter the annual premium value of policy: ",fg="black",font=("Californian FB","15")).place(x=50,y=180)
policy_annual_premium=Entry(root,textvariable=s3,width=10).place(x=630,y=180,height=30)

label5=Label(root,text="Enter the value of the insured zip of your policy: ",fg="black",font=("Californian FB","15")).place(x=50,y=220)
insured_zip=Entry(root,textvariable=s4,width=10).place(x=630,y=220,height=30)


label6=Label(root,text="Enter the sex of the customer of the policy (FEMALE/MALE): ",fg="black",font=("Californian FB","15")).place(x=50,y=260)
insured_sex=Entry(root,textvariable=s5,width=10).place(x=630,y=260,height=30)

label7=Label(root,text="Enter the education level of the customer: ",fg="black",font=("Californian FB","15")).place(x=50,y=300)
insured_education_level=Entry(root,textvariable=s6,width=10).place(x=630,y=300,height=30)

label8=Label(root,text="Enter the occupation of the  customer: ",fg="black",font=("Californian FB","15")).place(x=50,y=340)
insured_occupation=Entry(root,textvariable=s7,width=10).place(x=630,y=340,height=30)

label9=Label(root,text="Enter the hobbies of the customers: ",fg="black",font=("Californian FB","15")).place(x=50,y=380)
insured_hobbies=Entry(root,textvariable=s8,width=10).place(x=630,y=380,height=30)

label10=Label(root,text="Enter the relation of the customer: ",fg="black",font=("Californian FB","15")).place(x=50,y=420)
insured_relationship=Entry(root,textvariable=s9,width=10).place(x=630,y=420,height=30)

label11=Label(root,text="Enter the value of capital gain: ",fg="black",font=("Californian FB","15")).place(x=50,y=460)
capital_gains=Entry(root,textvariable=s10,width=10).place(x=630,y=460,height=30)

label12=Label(root,text="Enter the value of the capital loss: ",fg="black",font=("Californian FB","15")).place(x=50,y=500)
capital_loss=Entry(root,textvariable=s11,width=10).place(x=630,y=500,height=30)

label13=Label(root,text="Enter the type of the incident: ",fg="black",font=("Californian FB","15")).place(x=50,y=540)
incident_type=Entry(root,textvariable=s12,width=10).place(x=630,y=540,height=30)

label14=Label(root,text="Enter the details of the incident severity: ",fg="black",font=("Californian FB","15")).place(x=50,y=580)
incident_severity=Entry(root,textvariable=s13,width=10).place(x=630,y=580,height=30)

label15=Label(root,text="Enter the contacted authorities: ",fg="black",font=("Californian FB","15")).place(x=850,y=100)
authorities_contacted=Entry(root,textvariable=s14,width=10).place(x=1350,y=100,height=30)

label16=Label(root,text="Enter the time duration of the incident: ",fg="black",font=("Californian FB","15")).place(x=850,y=140)
incident_hour_of_the_day=Entry(root,textvariable=s15,width=10).place(x=1350,y=140,height=30)

label17=Label(root,text="Enter the number of the involved vehlicles: ",fg="black",font=("Californian FB","15")).place(x=850,y=180)
number_of_vehicles_involved=Entry(root,textvariable=s16,width=10).place(x=1350,y=180,height=30)

label18=Label(root,text="Is there any damaged property (YES/NO): ",fg="black",font=("Californian FB","15")).place(x=850,y=220)
property_damage=Entry(root,textvariable=s17,width=10).place(x=1350,y=220,height=30)

label19=Label(root,text="Enter the number of bodily injuries of the incident: ",fg="black",font=("Californian FB","15")).place(x=850,y=260)
bodily_injuries=Entry(root,textvariable=s18,width=10).place(x=1350,y=260,height=30)

label20=Label(root,text="Enter the number of witnesses: ",fg="black",font=("Californian FB","15")).place(x=850,y=300)
witnesses=Entry(root,textvariable=s19,width=10).place(x=1350,y=300,height=30)

label21=Label(root,text="Is there any police report available (YES/NO): ",fg="black",font=("Californian FB","15")).place(x=850,y=340)
police_report_available=Entry(root,textvariable=s20,width=10).place(x=1350,y=340,height=30)

label22=Label(root,text="Enter the total claimed amount: ",fg="black",font=("Californian FB","15")).place(x=850,y=380)
total_claim_amount=Entry(root,textvariable=s21,width=10).place(x=1350,y=380,height=30)

label23=Label(root,text="Enter the total amount for injury claimed: ",fg="black",font=("Californian FB","15")).place(x=850,y=420)
injury_claim=Entry(root,textvariable=s22,width=10).place(x=1350,y=420,height=30)

label24=Label(root,text="Enter the total amount for property claimed: ",fg="black",font=("Californian FB","15")).place(x=850,y=460)
property_claim=Entry(root,textvariable=s23,width=10).place(x=1350,y=460,height=30)

label25=Label(root,text="Enter the total amount for vehicle claimed: ",fg="black",font=("Californian FB","15")).place(x=850,y=500)
vehicle_claim=Entry(root,textvariable=s24,width=10).place(x=1350,y=500,height=30)

label26=Label(root,text="Enter the brand of the vehicle: ",fg="black",font=("Californian FB","15")).place(x=850,y=540)
auto_make=Entry(root,textvariable=s25,width=10).place(x=1350,y=540,height=30)

submit=Button(root,text="SUBMIT",bg="red",fg="yellow",command=disp,font=("Franklin Gothic Book",20)).place(x=1000,y=630)

l1= Label(root,text="Is this insurance claim is Fraud : " ,fg="white",bg="green",font=("Franklin Gothic Book","20")).place(x=400,y=700)
l=Label(root,fg="white",bg="green",font=("Franklin Gothic Book","15"))
l.place(x=870,y=700,height=30)

root.mainloop()