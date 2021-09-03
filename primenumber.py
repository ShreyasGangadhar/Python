num= int(input("Enter a number"))
prime= True
for i in range(2,num):
     if (num % i == 0 and num!=2):
          prime=False
          print('reached')
    
print(prime)