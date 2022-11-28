# Nth prime palindrome number
n=int(input("Enter the number of palindrome number required: "))
count=0
rem=0
primecheck=0
i=2
while(count!=n):
    copy=i
    nn=0
    while(copy!=0):
        rem=copy%10
        nn=(nn*10)+rem
        copy=copy//10
    primecheck=0
    if(nn==i):
        for j in range(1,i+1):
            if(i%j==0):
                primecheck=primecheck+1
            if(primecheck==2):
                count=count+1
            if(count==n):
                print("The",n,"th prime palindromic number is:",i)
    i=i+1

