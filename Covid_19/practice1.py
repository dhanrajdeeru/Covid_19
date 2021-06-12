# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:42:59 2021

@author: Hp
"""

def Covid_19():
    import pandas as pd
    from sklearn.linear_model import LogisticRegression 
    from sklearn.model_selection import train_test_split as tts
    from sklearn.metrics import confusion_matrix as conmat

    ds_1 = pd.read_csv('Prediction1.csv')

    logreg = LogisticRegression()
    ds_1['Severity'].unique()

    new_value = {'Severity_Mild':0, 'Severity_Moderate':1, 'Severity_None':2,
                 'Severity_Severe':3}

    ds_1.replace({'Severity': new_value} ,inplace=True)
    ds_1['Severity'].unique()

    X = ds_1.iloc[:,:-1].values
    y = ds_1.iloc[:,-1].values


    X_train,X_test,y_train,y_test =tts(X,y,test_size=0.2,random_state=80)

    logreg.fit(X_train,y_train)

    model_accuracy = logreg.score(X_test,y_test)
    model_prediction = logreg.predict(X_test)

    #type(X)

    print(' Model_Accuracy : ',model_accuracy*100)
    print(' Model_Prediction : ',model_prediction)

    print(conmat(y_test,model_prediction))
    
    print(' Checking Model Prediction : \n')
    s= [[1,0,0,0]]
    s_1=logreg.predict(s)
    print(s_1)
    if s_1==1:print('Moderate')
    if s_1==0:print('Mild')
    if s_1==2:print('None')
    if s_1==3:print('Severe')



    print(' To predict about Covid-19 situation in future \n')
    print(' 1. Identify the number of people infected')
    print(' 2. Check for the sevierity of the infection (Mild,Moderate,Severe)')
    print(' 3. After which it is possible to predict about future \n')
    print(' Here we are predicting out of 1000 people')
    c = 0
    while(True):
        var_1 = int(input('Press 1. to continue \n 2. exit'))
        if var_1 == 2:
            break
        else:
            print('Enter the values as per Sevierity of infection : \n')
            var_2 = int(input('Mild  :  '))
            var_3 = int(input('Moderate  :  '))
            var_4 = int(input('Severity  :  '))

        if var_2 >= 600:
            #print('Covid situation will be out of  in control  \n')
            c=c+1
        else:
            #print('Covid situation will be in control ')
            c=c-1

        if var_3 >= 300:
            #print('Covid situation will be out of  in control  \n')
            c=c+1
        else:
            #print('Covid situation will be in control ')
            c=c-1
        if var_4 >= 100:
            #print('Covid situation will be out of  in control  \n')
            c=c+1
        else:
            #print('Covid situation will be in control ')
            c=c-1
        if c > 0:
            print('1. Mild = {} \n2.Moderate = {}\n3.Severe = {} \n '.format(var_2,var_3,var_4))
            print('Covid situation will be out of   control  \n')
        else:
            print('1. Mild = {} \n2.Moderate = {}\n3.Severe = {} \n '.format(var_2,var_3,var_4))
            print('Covid situation will be in control \n')