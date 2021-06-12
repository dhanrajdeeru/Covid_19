# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:05:57 2021

@author: Hp
"""

import pandas as pd
import matplotlib.pyplot as plt
import Project3 as p3
import practice1 as prac1

ds = pd.read_csv("CVID_19_STATE.csv",index_col=1)

list_state=ds['State_Name']
var1=0
list1=ds['Total _Confirmed'].values.tolist()
for i in range(0,len(list1)):
    var1 = var1+list1[i]
print('Total _Confirmed : ',var1)
var2 =0
list2 =ds['Deaths'].values.tolist()
for i in range(0,len(list2)):
    var2 = var2+list2[i]
print('Deaths : ',var2)
var3 =0
list3 =ds['Cured_Discharged_Migrated'].values.tolist()
for i in range(0,len(list3)):
    var3 = var3+list3[i]
print('Cured_Discharged_Migrated : ',var3)

var=[var1,var2,var3]
mylabels1 = ['Total - Confirmed','Deaths','Cured/Discharged/Migrated']
myexplode=[0.1,0,0]
plt.pie(var, startangle = 45, explode = myexplode, shadow = True, autopct='%1.1f%%')
plt.legend(mylabels1)
plt.title('Pie-Chart representation of Covid-19 Metrics INDIA')
plt.show()

fig=plt.figure(figsize=(20,20))
ds1 = ds.sort_values('Total _Confirmed',ascending=False)
ds2 = ds.sort_values('Deaths', ascending=False)
ds3 = ds.sort_values('Cured_Discharged_Migrated', ascending=False)

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.bar(ds1.index, ds1['Total _Confirmed'])
ax1.set_xticklabels(ds1.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax1.set_title("Covid-19 Metrics INDIA ('Total_Confirmed')",fontsize='20')
ax1.set_xlabel("States",fontsize=14)
ax1.set_ylabel("Cases",fontsize=14)
ax2.bar(ds2.index, ds2['Deaths'])
ax2.set_xticklabels(ds2.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax2.set_title("Covid-19 Metrics INDIA ('Deaths')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Cases",fontsize=14)
plt.show()

fig1=plt.figure(figsize=(20,10))
ax3= fig1.add_subplot(2,1,1)
ax3.bar(ds3.index,ds3['Cured_Discharged_Migrated'])
ax3.set_xticklabels(ds3.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax3.set_title("Covid-19 Metrics INDIA ('Cured_Discharged_Migrated')",fontsize='20')
ax3.set_xlabel("States",fontsize=14)
ax3.set_ylabel("Cases",fontsize=14)
plt.show()

for i,state in enumerate(list_state):
    print(i+1,state,end=" ; ")
fig10 = plt.figure(figsize=(20,5))
label=['Total - Confirmed','Deaths','Cured/Discharged/Migrated']
num = list(range(1,37))

plt.plot(num , ds['Total _Confirmed'], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['Deaths'], color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['Cured_Discharged_Migrated'], color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)

plt.title("COVID-19 INDIA ",fontsize=20)
plt.ylabel("Total_Number")
plt.legend(label)

plt.xticks(num)
plt.show()

# Vaccination by Age

var1=0
list1=ds['18_to_45'].values.tolist()
for i in range(0,len(list1)):
    var1 = var1+list1[i]
print('18_to_45 : ',var1)

var2 = 0
list2 =ds['45_to_60'].values.tolist()
for i in range(0,len(list2)):
    var2 = var2 + list2[i]
print('45_to_60 : ',var2)

var3 =0
list3 =ds['60_plus'].values.tolist()
for i in range(0,len(list3)):
    var3 = var3 + list3[i]
print('60_plus : ',var3)

var=[var1,var2,var3]
mylabels2 = ['18 to 45','45 to 60',' 60+']
myexplode=[0.1,0,0]
plt.pie(var, startangle = 90, explode = myexplode, shadow = True, autopct='%1.1f%%')
plt.legend(mylabels2)
plt.title('Pie-Chart representation of Covid-19 Vaccination by Age INDIA')
plt.show()

fig2=plt.figure(figsize=(20,15))
ds1 = ds.sort_values('18_to_45',ascending=False)
ds2 = ds.sort_values('45_to_60', ascending=False)
ds3 = ds.sort_values('60_plus', ascending=False)

ax1 = fig2.add_subplot(2,1,1)
ax2 = fig2.add_subplot(2,1,2)
ax1.bar(ds1.index, ds1['18_to_45'])
ax1.set_xticklabels(ds1.index, rotation=45 ,horizontalalignment='right' , fontsize='12')
ax1.set_title("Covid-19 Vaccination by Age INDIA ('18_to_45')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Total_Number",fontsize=14)
ax2.bar(ds2.index, ds2['45_to_60'])
ax2.set_xticklabels(ds2.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax2.set_title("Covid-19 Vaccination by Age INDIA ('45_to_60')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Total_Number",fontsize=14)
plt.show()

fig3=plt.figure(figsize=(20,15))
ax3= fig3.add_subplot(2,1,1)
ax3.bar(ds3.index,ds3['60_plus'])
ax3.set_xticklabels(ds3.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax3.set_title("Covid-19 Metrics INDIA ('60+')",fontsize='20')
ax3.set_xlabel("States",fontsize=14)
ax3.set_ylabel("Total_Number",fontsize=14)
plt.show()


for i,state in enumerate(list_state):
    print(i+1,state,end=" ; ")

fig11 = plt.figure(figsize=(20,10))
ds1 = ds.sort_values('18_to_45',ascending=False)
ds2 = ds.sort_values('45_to_60', ascending=False)
ds3 = ds.sort_values('60_plus', ascending=False)
label=['18_to_45','45_to_60','60_plus']
num = list(range(1,37))

plt.plot(num , ds['18_to_45'], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['45_to_60'], color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['60_plus'], color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)

plt.title("Vaccination by Age INDIA ",fontsize=20)
plt.ylabel("Total_Number")
plt.legend(label)

plt.xticks(num)
plt.show()

# Vaccination by Gender

var1=0
list1=ds['Male_Dose'].values.tolist()
for i in range(0,len(list1)):
    var1 = var1+list1[i]
print('Male_Dose : ',var1)

var2 = 0
list2 =ds['Female_Dose'].values.tolist()
for i in range(0,len(list2)):
    var2 = var2 + list2[i]
print('Female_Dose : ',var2)

var3 =0
list3 =ds['Others_Dose'].values.tolist()
for i in range(0,len(list3)):
    var3 = var3 + list3[i]
print('Others_Dose : ',var3)

var=[var1,var2,var3]
mylabels2 = ['Male_Dose','Female_Dose','Others_Dose']
myexplode=[0.1,0,0]
plt.pie(var, startangle = 60, explode = myexplode, shadow = True, autopct='%1.1f%%')
plt.legend(mylabels2)
plt.title('Pie-Chart representation of Covid-19 Vaccination by Gender INDIA')
plt.show()

fig4=plt.figure(figsize=(20,15))
ds1 = ds.sort_values('Male_Dose',ascending=False)
ds2 = ds.sort_values('Female_Dose', ascending=False)
ds3 = ds.sort_values('Others_Dose', ascending=False)

ax1 = fig4.add_subplot(2,1,1)
ax2 = fig4.add_subplot(2,1,2)
ax1.bar(ds1.index, ds1['Male_Dose'])
ax1.set_xticklabels(ds1.index, rotation=45 ,horizontalalignment='right' , fontsize='12')
ax1.set_title("Covid-19 Vaccination by Gender INDIA ('Male_Dose')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Total_Number",fontsize=14)
ax2.bar(ds2.index, ds2['Female_Dose'])
ax2.set_xticklabels(ds2.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax2.set_title("Covid-19 Vaccination by Gender INDIA ('Female_Dose')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Total_Number",fontsize=14)
plt.show()

fig5=plt.figure(figsize=(20,15))
ax3= fig5.add_subplot(2,1,1)
ax3.bar(ds3.index,ds3['Others_Dose'])
ax3.set_xticklabels(ds3.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax3.set_title("Covid-19 Vaccination by Gender INDIA ('Others_Dose')",fontsize='20')
ax3.set_xlabel("States",fontsize=14)
ax3.set_ylabel("Total_Number",fontsize=14)
plt.show()

for i,state in enumerate(list_state):
    print(i+1,state,end=" ; ")

fig12 = plt.figure(figsize=(20,10))
ds1 = ds.sort_values('Male_Dose',ascending=False)
ds2 = ds.sort_values('Female_Dose', ascending=False)
ds3 = ds.sort_values('Others_Dose', ascending=False)
label=['Male_Dose','Female_Dose','Others_Dose']
num = list(range(1,37))

plt.plot(num , ds['Male_Dose'], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['Female_Dose'], color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['Others_Dose'], color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)

plt.title("Vaccination by Doseage INDIA ",fontsize=20)
plt.ylabel("Total_Number")
plt.legend(label)

plt.xticks(num)
plt.show()

# Vaccination by Doseage

var1=0
list1=ds['First_Dose'].values.tolist()
for i in range(0,len(list1)):
    var1 = var1+list1[i]
print('First_Dose : ',var1)

var2 = 0
list2 =ds['Second_Dose'].values.tolist()
for i in range(0,len(list2)):
    var2 = var2 + list2[i]
print('Second_Dose : ',var2)

var3 =0
list3 =ds['Total_Dose'].values.tolist()
for i in range(0,len(list3)):
    var3 = var3 + list3[i]
print('Total_Dose : ',var3)

var=[var1,var2,var3]
mylabels2 = ['First_Dose','Second_Dose','Total_Dose']
myexplode=[0.1,0,0]
plt.pie(var, startangle = 60, explode = myexplode, shadow = True, autopct='%1.1f%%')
plt.legend(mylabels2)
plt.title('Pie-Chart representation of Covid-19 Vaccination by Vaccine_Dose INDIA')
plt.show()

fig6=plt.figure(figsize=(20,15))
ds1 = ds.sort_values('First_Dose',ascending=False)
ds2 = ds.sort_values('Second_Dose', ascending=False)
ds3 = ds.sort_values('Total_Dose', ascending=False)

ax1 = fig6.add_subplot(2,1,1)
ax2 = fig6.add_subplot(2,1,2)
ax1.bar(ds1.index, ds1['First_Dose'])
ax1.set_xticklabels(ds1.index, rotation=45 ,horizontalalignment='right' , fontsize='12')
ax1.set_title("Covid-19 Vaccination by Vaccine_Dose INDIA ('First_Dose')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Total_Number",fontsize=14)
ax2.bar(ds2.index, ds2['Second_Dose'])
ax2.set_xticklabels(ds2.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax2.set_title("Covid-19 Vaccination by Vaccine_Dose INDIA ('Second_Dose')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Total_Number",fontsize=14)
plt.show()

fig7=plt.figure(figsize=(20,15))
ax3= fig7.add_subplot(2,1,1)
ax3.bar(ds3.index,ds3['Total_Dose'])
ax3.set_xticklabels(ds3.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax3.set_title("Covid-19 Vaccination by Vaccine_Dose INDIA ('Total_Dose')",fontsize='20')
ax3.set_xlabel("States",fontsize=14)
ax3.set_ylabel("Total_Number",fontsize=14)
plt.show()

for i,state in enumerate(list_state):
    print(i+1,state,end=" ; ")

fig13 = plt.figure(figsize=(20,10))
ds1 = ds.sort_values('First_Dose',ascending=False)
ds2 = ds.sort_values('Second_Dose', ascending=False)
ds3 = ds.sort_values('Total_Dose', ascending=False)
label=['First_Dose','Second_Dose','Total_Dose']
num = list(range(1,37))

plt.plot(num , ds['First_Dose'], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['Second_Dose'], color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['Total_Dose'], color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)

plt.title("Vaccination by Doseage INDIA ",fontsize=20)
plt.ylabel("Total_Number")
plt.legend(label)

plt.xticks(num)
plt.show()

# Vaccination by Vaccine_type

var1=0
list1=ds['Covaxin'].values.tolist()
for i in range(0,len(list1)):
    var1 = var1+list1[i]
print('Covaxin : ',var1)

var2 = 0
list2 =ds['Covishield'].values.tolist()
for i in range(0,len(list2)):
    var2 = var2 + list2[i]
print('Covishield : ',var2)

var3 =0
list3 =ds['Sputnik'].values.tolist()
for i in range(0,len(list3)):
    var3 = var3 + list3[i]
print('Sputnik : ',var3)

var=[var1,var2,var3]
mylabels2 = ['Covaxin','Covishield','Sputnik']
myexplode=[0.1,0.2,0]
plt.pie(var, startangle = 45, explode = myexplode, shadow = True, autopct='%1.1f%%')
plt.legend(mylabels2)
plt.title('Pie-Chart representation of Covid-19 Vaccination by Vaccine_Type INDIA')
plt.show()

fig8=plt.figure(figsize=(20,15))
ds1 = ds.sort_values('Covaxin',ascending=False)
ds2 = ds.sort_values('Covishield', ascending=False)
ds3 = ds.sort_values('Sputnik', ascending=False)

ax1 = fig8.add_subplot(2,1,1)
ax2 = fig8.add_subplot(2,1,2)
ax1.bar(ds1.index, ds1['Covaxin'])
ax1.set_xticklabels(ds1.index, rotation=45 ,horizontalalignment='right' , fontsize='12')
ax1.set_title("Covid-19 Vaccination by Vaccine_Type INDIA ('Covaxin')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Total_Number",fontsize=14)
ax2.bar(ds2.index, ds2['Covishield'])
ax2.set_xticklabels(ds2.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax2.set_title("Covid-19 Vaccination by Vaccine_Type INDIA ('Covishield')",fontsize='20')
ax2.set_xlabel("States",fontsize=14)
ax2.set_ylabel("Total_Number",fontsize=14)
plt.show()

fig9=plt.figure(figsize=(20,15))
ax3= fig9.add_subplot(2,1,1)
ax3.bar(ds3.index,ds3['Sputnik'])
ax3.set_xticklabels(ds3.index, rotation=60 ,horizontalalignment='right' , fontsize='12')
ax3.set_title("Covid-19 Vaccination by Gender INDIA ('Sputnik')",fontsize='20')
ax3.set_xlabel("States",fontsize=14)
ax3.set_ylabel("Total_Number",fontsize=14)
plt.show()

for i,state in enumerate(list_state):
    print(i+1,state,end=" ; ")

fig14 = plt.figure(figsize=(20,10))
ds1 = ds.sort_values('Covaxin',ascending=False)
ds2 = ds.sort_values('Covishield', ascending=False)
ds3 = ds.sort_values('Sputnik', ascending=False)
label=['Covaxin','Covishield','Sputnik']
num = list(range(1,37))

plt.plot(num , ds['Covaxin'], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['Covishield'], color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(num , ds['Sputnik'], color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)

plt.title("Vaccination by Vaccine_Type INDIA ",fontsize=20)
plt.ylabel("Total_Number")
plt.legend(label)

plt.xticks(num)
plt.show()


#Detailed Information of Covid_19 in each state
a=1

while (a == 1):
    list_state1 = ds['State_Name']
    print('\nCOVID-19 INFORAMATION OF PARTICULAR STATES\n')
    for i , state in enumerate(list_state1):
        print(i+1,state,end=' ; ')
    n = int(input('\nenter the serial_number given below : '))
    a = p3.check_condition(n)

# if you want to predict the model 
# feature set should be in following fromat
#1. basic symptoms - entries can be either 1/0 ,if symptom are present then 1 or else 0
#2. less basic symptoms - entries can be either 1/0 ,if symptom are present then 1 or else 0
#3. severe symptoms - entries can be either 1/0 ,if symptom are present then 1 or else 0
#4. none - entries can be either 1/0 ,if any of the above symptoms are not present then 1 or else 0
prac1.Covid_19()