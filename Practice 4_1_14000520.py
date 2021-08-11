
def chest(m,n):

   
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0:
                print('#', end=" ")
            else:
                print('*', end=" ")
        print("\n")

n = int(input("enter n length = "))
m = int(input("enter m length = "))
chest(m,n)