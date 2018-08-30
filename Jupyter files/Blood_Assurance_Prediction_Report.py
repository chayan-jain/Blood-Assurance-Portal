
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

secure_random = random.SystemRandom()

HospitalList = []
with open (r'C:\Users\Prateek\Desktop\Ansible\Project\Dataset\HospitalsList.txt','r') as b:
    for x in b.readlines():
        p=x.strip('\n')
        HospitalList.append(p)

foo = []
with open (r'C:\Users\Prateek\Desktop\Ansible\Project\Dataset\DOCNAME.csv','r') as b:
    for x in b.readlines():
        p=x.strip('\n')
        foo.append(p)
        

df = np.random.randint(0,100)

raw_data = {'Name_Of_Hospital': [secure_random.choice(HospitalList) for i in range(30)],
            'Doctor1': [secure_random.choice(foo) for i in range(30)],
            'Doctor2': [secure_random.choice(foo) for i in range(30)],
            'FR1': ['Not Available' for i in range(30)],
            'FR2': ['Not Available' for i in range(30)],
            'Mobile1': [9000000000+np.random.randint(900000000,999999999) for i in range(30)],
            'Mobile2': [9000000000+np.random.randint(900000000,999999999) for i in range(30)],
}
df = pd.DataFrame(raw_data, columns = ['Name_Of_Hospital','Doctor1','Doctor2','FR1','FR2','Mobile1','Mobile2'])
df.to_csv(r'C:\Users\Prateek\Desktop\Ansible\Project\HospitalTable.csv')
df


# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date, timedelta

df = pd.read_csv(r'C:\Users\Prateek\Desktop\Ansible\Project\HospitalTable.csv')
for HospitalName in df['Name_Of_Hospital']:
    
    time = []
    def perdelta(start, end, delta):
        curr = start
        while curr < end:
            yield curr, min(curr + delta, end)
            curr += delta
    for s, e in perdelta(date(2018, 6, 16), date(2018, 7, 15), timedelta(days=1)):
             time.append(s)
            
    df = np.random.randint(0,100)
    raw_data = {
                'Date':[i for i in range(1,11)],
                'O+': [np.random.randint(50,70) for i in range(10)],
                'O-': [np.random.randint(60,80) for i in range(10)],
                'A+': [np.random.randint(40,70) for i in range(10)],
                'A-': [np.random.randint(30,60) for i in range(10)],
                'B+': [np.random.randint(50,80) for i in range(10)],
                'B-': [np.random.randint(60,80) for i in range(10)],
                'AB+': [np.random.randint(50,80) for i in range(10)],
                'AB-': [np.random.randint(60,90) for i in range(10)],
                'HH': [np.random.randint(0,10) for i in range(10)],
    }
    df = pd.DataFrame(raw_data, columns = ['Date','O+', 'O-', 'A+', 'A-', 'B+','B-','AB+','AB-','HH'])
    df.to_csv(r'C:\Users\Prateek\Desktop\Ansible\Project\BloodGroupDataset\{}.csv'.format(HospitalName))
    print("Blood group dataset of {} is created.".format(HospitalName))




# In[16]:


# Prediction Only for next 30 days   (1)

import numpy as np
import pandas as pd
import sklearn
import sklearn.cross_validation as skcross
import sklearn.linear_model as sk_lm


HospitalName = str(input("Enter the Hospital name whose prediction is required:-   "))
x_test = int(input("Enter the Prediction value date:-  "))

data = pd.read_csv(r'C:\Users\Prateek\Desktop\Ansible\Project\BloodGroupDataset\{}.csv'.format(HospitalName))

ls = ['O+','O-','A+','A-','B+','B-','AB+','AB-','HH']

print("Predicted Blood group units that must be available on {} date:- ".format(x_test))

for i in range(1,10):
    x=data.iloc[:,0:1]
    y=data.iloc[:,i]

#    print(x)
#    print(y)
    x_train,x_testOld,y_train,y_testOld=skcross.train_test_split(x,y,test_size=0,random_state=20)

    
    model=sk_lm.LinearRegression()
    model.fit(x_train,y_train)
    y_predict=model.predict(x_test)

    print("\t For {} blood group :- {} units Predicted ".format(ls[i-1],int(y_predict)))


# In[ ]:


# Prediction Only for next 30 days   (2)
import numpy as np
import pandas as pd
import sklearn
import sklearn.cross_validation as skcross
import sklearn.linear_model as sk_lm


HospitalName = str(input("Enter the Hospital name whose prediction is required:-   "))
#curr_date = 
x_test = int(input("Enter the Prediction value date:-  "))
print("Blood units that must be donated by public before {} date is:- ".format(x_test))

df = pd.read_csv('D:\{}.csv'.format(HospitalName))

ls = ['O+','O-','A+','A-','B+','B-','AB+','AB-','HH']

print("Predicted Blood group units that must be available on {} date:- ".format(x_test))

for i in range(1,10):
    x=df.iloc[:,0:1]
    y=df.iloc[:,i]

#    print(x)
#    print(y)
    x_train,x_testOld,y_train,y_testOld=skcross.train_test_split(x,y,test_size=0,random_state=20)

    
    model=sk_lm.LinearRegression()
    model.fit(x_train,y_train)
    y_predict=model.predict(x_test)

    print("\t For {} blood group :- {} units Predicted ".format(ls[i-1],int(y_predict)))
    
    x = df.loc[9,ls[i-1]]
    print("\t \t \t {} units available".format(x))


# In[10]:


# Prediction Only for next 30 days   (3)
import numpy as np
import pandas as pd
import sklearn
import sklearn.cross_validation as skcross
import sklearn.linear_model as sk_lm


HospitalName = str(input("Enter the Hospital name whose prediction is required:-   "))
#curr_date = 
x_test = int(input("Enter the Prediction value date:-  "))
#print("Blood units that must be donated by public before {} date is:- ".format(x_test))

arrR = []
arrD = []

df = pd.read_csv(r'C:\Users\Prateek\Desktop\Ansible\Project\BloodGroupDataset\{}.csv'.format(HospitalName))

ls = ['O+','O-','A+','A-','B+','B-','AB+','AB-','HH']

#print("Predicted Blood group units that must be available on {} date:- ".format(x_test))

for i in range(1,10):
    x=df.iloc[:,0:1]
    y=df.iloc[:,i]

#    print(x)
#    print(y)
    x_train,x_testOld,y_train,y_testOld=skcross.train_test_split(x,y,test_size=0,random_state=20)

    
    model=sk_lm.LinearRegression()
    model.fit(x_train,y_train)
    y_predict=model.predict(x_test)

    print("\t For {} blood group :-".format(ls[i-1]))
    print("\t \t \t {} units Predicted ".format(int(y_predict)))
    
    x = df.loc[9,ls[i-1]]
    print("\t \t \t {} units available".format(x))
    
    transaction = x - int(y_predict) 
    if transaction > int(y_predict):
        print("You have to take {} units blood from Nearby Hospital:- ".format(transaction-int(y_predict)))
        arrR.append([HospitalName,ls[i-1],transaction-int(y_predict)])
    elif transaction < int(y_predict):
        print("You have to give {} units blood from Nearby Hospital:- ".format(int(y_predict)-x))
        arrD.append([HospitalName,ls[i-1],int(y_predict)-x])
    else:
        print("Nothing to do.")
    print()


# In[ ]:


# Prediction Only for next 30 days   (4)
import numpy as np
import pandas as pd
import sklearn
import sklearn.cross_validation as skcross
import sklearn.linear_model as sk_lm

arrR = []
arrD = []

df = pd.read_csv(r'C:\Users\Prateek\Desktop\Ansible\Project\HospitalTable.csv')

x_test = int(input("Enter the Prediction value date:-  "))


for HospitalName in df['Name_Of_Hospital']:

    df = pd.read_csv(r'C:\Users\Prateek\Desktop\Ansible\Project\BloodGroupDataset\{}.csv'.format(HospitalName))

    ls = ['O+','O-','A+','A-','B+','B-','AB+','AB-','HH']

    for i in range(1,10):
        x=df.iloc[:,0:1]
        y=df.iloc[:,i]

        x_train,x_testOld,y_train,y_testOld=skcross.train_test_split(x,y,test_size=0,random_state=20)


        model=sk_lm.LinearRegression()
        model.fit(x_train,y_train)
        y_predict=model.predict(x_test)

     #   print("\t For {} blood group :-".format(ls[i-1]))
     #   print("\t \t \t {} units Predicted ".format(int(y_predict)))

        x = df.loc[9,ls[i-1]]
     #   print("\t \t \t {} units available".format(x))

        transaction = x - int(y_predict) 
        if transaction > int(y_predict):
          #  print("You have to take {} units blood from Nearby Hospital:- ".format(transaction-int(y_predict)))
            arrR.append([HospitalName,ls[i-1],transaction-int(y_predict)])
        elif transaction < int(y_predict):
           # print("You have to give {} units blood from Nearby Hospital:- ".format(int(y_predict)-x))
            arrD.append([HospitalName,ls[i-1],int(y_predict)-x])
        else:
            print("")
       # print()
    
ch = input("Whether you need the details of Hospitals(Y/N):- ")
if ch=='Y':
            ls = ['O+','O-','A+','A-','B+','B-','AB+','AB-','HH']
            hosNameDonate = []
            hosNameReceive = []
            hospitalNamearrD =""
            hospitalNamearrR =""
            for bg in ls:

                
                for index in range(len(arrD)):
                    if arrD[index][1] == bg:
                        hospitalNamearrD = arrD[index][0]
                        break
                hosNameDonate.append([bg,hospitalNamearrD])
                for index in range(len(arrR)):
                    if arrR[index][1]==bg:
                        hospitalNamearrR = arrR[index][0]
                        break
                hosNameReceive.append([bg,hospitalNamearrR])
            print("\n Hospital Details where blood is needed:- \n")
            for index in range(len(hosNameDonate)):
                print(hosNameDonate[index][0]," : ", hosNameDonate[index][1])
            print("\n Hospital Details where blood is extra available:- \n")
            for index in range(len(hosNameReceive)):
                print(hosNameReceive[index][0], " : " , hosNameReceive[index][1])
elif ch=='N':
            print("Thank you for coming")
else:
            print("Wrong choice")
    

