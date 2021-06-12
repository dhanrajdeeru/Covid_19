# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:46:26 2021

@author: Hp
"""

import pandas as pd
import matplotlib.pyplot as plt
ds = pd.read_csv("CVID_19_STATE.csv",index_col=1)

def information(file):

    df_1 = pd.read_csv(file)

    var1=0
    list1=df_1['Confirmed_Cases_Value'].values.tolist()
    for i in range(0,len(list1)):
        var1 = var1+list1[i]
    print('Total_Confirmed :',var1)
    var2 =0
    list2 =df_1['Recovered_Value'].values.tolist()
    for i in range(0,len(list2)):
        var2 = var2+list2[i]
    print('Total_Recovered :',var2)
    var3 =0
    list3 =df_1['Deaths_Value'].values.tolist()
    for i in range(0,len(list3)):
        var3 = var3+list3[i]
    print('Deaths :',var3)
    var4=0
    list4 =df_1['Active_Cases_Value'].values.tolist()
    for i in range(0,len(list4)):
        var4 = var4 + list4[i]
    print('Active_Cases :',var4)
    var=[var1,var2,var3,var4]
    mylabels1 = ['Total - Confirmed','Cured/Discharged/Migrated','Deaths','Active-Cases']
    myexplode=[0.1,0,0,0.1]
    plt.pie(var, startangle = 60, explode = myexplode, shadow = True, autopct='%1.1f%%')
    plt.legend(mylabels1)
    plt.title('Pie-Chart representation')
    plt.show()

#-----------------------------------------

    list_state=df_1['District']
    
    for i,state in enumerate(list_state):
        print(i+1,state,end=" ; ")

    plt.figure(figsize=(20,5))
    label=['Male_Doses_Value','Female_Doses_Value','Others_Doses_Value','First_Dose_Value','Second_Dose_Value','Total_Dose_Value'
          ]
    num = list(range(1,len(list_state)+1))

    plt.plot(num , df_1['Male_Doses_Value'], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['Female_Doses_Value'], color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['Other_Doses_Value'], color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['First_Dose_Value'], color='cyan', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['Second_Dose_Value'], color='magenta', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['Total_Dose_Value'], color='yellow', marker='o', linestyle='dashed',linewidth=2, markersize=12)

    plt.title("COVID-19 ",fontsize=20)
    plt.ylabel("Total_Number")
    plt.legend(label)
    plt.xticks(num)
    plt.show()

    plt.figure(figsize=(20,5))
    label=['18_to_45', '45_to_60','60_plus_Value']
    num = list(range(1,len(list_state)+1))

    plt.plot(num , df_1['18_to_45_Value'], color='cyan', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['45_to_60_Value'], color='black', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['60_plus_Value'], color='yellow', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.title("COVID-19 ",fontsize=20)
    plt.ylabel("Total_Number")
    plt.legend(label)
    plt.xticks(num)
    plt.show()

    plt.figure(figsize=(20,5))
    label=['Covaxin','Covishield','Sputnik']
    num = list(range(1,len(list_state)+1))

    plt.plot(num , df_1['Covaxin_Value'], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['Covishield_Value'], color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(num , df_1['Sputnik_Value'], color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)

    plt.title("COVID-19 ",fontsize=20)
    plt.ylabel("Total_Number")
    plt.legend(label)
    plt.xticks(num)
    plt.show()  
    
def check_condition(n):
    if n == 1:
            print('\n')
            print('\nCOVID-19 details of Andaman and Nicobar :') 
            information("a1.csv") 
            return 1
    elif n == 2:
            print('\n')
            print('\nCOVID-19 details of Andhra Pradesh :') 
            information("a2.csv") 
            return 1
    elif n == 3:
            print('\n')    
            print('\nCOVID-19 details of Arunachal Pradesh :') 
            information("a3.csv") 
            return 1
    elif n == 4:
            print('\n')
            print('\nCOVID-19 details of Assam :') 
            information("a4.csv") 
            return 1
    elif n == 5:
            print('\n')
            print('\nCOVID-19 details of Bihar :') 
            information("a5.csv") 
            return 1
    elif n == 6:
            print('\n')
            print('\nCOVID-19 details of Chandigarh :') 
            information("a6.csv") 
            return 1
    elif n == 7:
            print('\n')
            print('\nCOVID-19 details of Chhattisgarh :') 
            information("a7.csv") 
            return 1
    elif n == 8:
            print('\n')
            print('\nCOVID-19 details of Delhi :') 
            information("a8.csv") 
            return 1
    elif n == 9:
            print('\n')
            print('\nCOVID-19 details ofDadra and Nagar Haveli and Daman and Diu :') 
            information("a9.csv") 
            return 1
    elif n == 10:
            print('\n')
            print('\nCOVID-19 details of Goa :') 
            information("a10.csv") 
            return 1
    elif n == 11:
            print('\n')
            print('\nCOVID-19 details of Gujarat :') 
            information("a11.csv") 
            return 1
    elif n == 12:
            print('\n')
            print('\nCOVID-19 details of Himachal Pradesh :') 
            information("a12.csv")
            return 1
    elif n == 13:
            print('\n')
            print('\nCOVID-19 details of Haryana :') 
            information("a13.csv") 
            return 1
    elif n == 14:
            print('\n')
            print('\nCOVID-19 details of Jharkhand :') 
            information("a14.csv") 
            return 1
    elif n == 15:
            print('\n')
            print('\nCOVID-19 details of Jammu and Kashmir :') 
            information("a15.csv") 
            return 1
    elif n == 16:
            print('\n')
            print('\nCOVID-19 details of Karnataka:') 
            information("a16.csv") 
            return 1
    elif n == 17:
            print('\n')
            print('\nCOVID-19 details of Kerala :') 
            information("a17.csv") 
            return 1
    elif n == 18:
            print('\n')
            print('\nCOVID-19 details of Lakshadweep :') 
            information("a18.csv") 
            return 1
    elif n == 19:
            print('\n')
            print('\nCOVID-19 details of Ladakh :') 
            information("a19.csv") 
            return 1
    elif n == 20:
            print('\n')
            print('\nCOVID-19 details of Maharashtra :') 
            information("a20.csv") 
            return 1
    elif n == 21:
            print('\n')
            print('\nCOVID-19 details of Meghalaya :') 
            information("a21.csv") 
            return 1
    elif n == 22:
            print('\n')
            print('\nCOVID-19 details of Manipur :') 
            information("a22.csv") 
            return 1
    elif n == 23:
            print('\n')
            print('\nCOVID-19 details of Madhya Pradesh :') 
            information("a23.csv") 
            return 1
    elif n == 24:
            print('\n')
            print('\nCOVID-19 details of Mizoram :') 
            information("a24.csv")
            return 1
    elif n == 25:
            print('\n')
            print('\nCOVID-19 details of Nagaland :') 
            information("a25.csv") 
            return 1
    elif n == 26:
            print('\n')
            print('\nCOVID-19 details of Odisha :') 
            information("a26.csv") 
            return 1
    elif n == 27:
            print('\n')
            print('\nCOVID-19 details of Punjab :') 
            information("a27.csv") 
            return 1
    elif n == 28:
            print('\n')
            print('\nCOVID-19 details of Puducherry :') 
            information("a28.csv") 
            return 1
    elif n == 29:
            print('\n')
            print('\nCOVID-19 details of Rajasthan :') 
            information("a29.csv") 
            return 1
    elif n == 30:
            print('\n')
            print('\nCOVID-19 details of Sikkim :') 
            information("a30.csv") 
            return 1
    elif n == 31:
            print('\n')
            print('\nCOVID-19 details of Telengana :') 
            information("a31.csv") 
            return 1
    elif n == 32:
            print('\n')
            print('\nCOVID-19 details of Tamil Nadu :') 
            information("a32.csv") 
            return 1
    elif n == 33:
            print('\n')
            print('\nCOVID-19 details of Tripura :') 
            information("a33.csv") 
            return 1
    elif n == 34:
            print('\n')
            print('\nCOVID-19 details of Uttarakhand :') 
            information("a34.csv") 
            return 1
    elif n == 35:
            print('\n')
            print('\nCOVID-19 details of Uttar Pradesh :') 
            information("a35.csv") 
            return 1
    elif n == 36:
            print('\n')
            print('\nCOVID-19 details of West Bengal :') 
            information("a36.csv") 
            return 1
    else:
            print('\n',)
            print('\nProtect yourself and others from COVID-19')
            print('Stay Home...... Stay Safe')
            return 2