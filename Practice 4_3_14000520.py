def product(m,n):

    for i in range(1,m+1):
        for j in range(1,n+1):
         print(i*j,end='\t')
        print()

n = int(input("enter n length = "))
m = int(input("enter m length = "))
product(m,n)

