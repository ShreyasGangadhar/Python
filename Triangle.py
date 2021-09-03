n= int(input("Enter a number "))
for i in range(3):
       #No of rows
    print(' '*(n-i-1),end="")
    print('*'*(2*i+1),end="")
    print(' '*(n-i-1))   