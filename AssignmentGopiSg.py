#To Calculate Simple Interest for Bank Customer for Fixed Deposit 
str(['Female','SeniorCitizen','Male','NonSeniorCitizen']) 
Ap=str(input('customer gender=')) 
Ts=str(input('customer citizenship=')) 
p=int(input('Enter Initial Principal=')) 
t=int(input('Enter the Time period of Deposit=')) 
r=float() 
if (Ap=='Male' and Ts=='NonSeniorCitizen'): 
   r=float(0.05) 
   print('R=',r) 
   print('Simple Interest=',(p*t*r)/100) 
elif (Ap=='Female' and Ts=='NonSeniorCitizen'): 
     r=float (0.06) 
     print('R=',r) 
     print('Simple Interest=',(p*t*r)/100) 
elif (Ap=='Male' and Ts=='SeniorCitizen'): 
     r=float (0.07) 
     print('R=',r) 
     print('Simple Interest=',(p*t*r)/100) 
elif (Ap=='Female' and Ts=='SeniorCitizen'): 
     r=float (0.08) 
     print('R=',r) 
     print('Simple Interest=',(p*t*r)/100) 
else: 
     print('Enter Correct Details!')
