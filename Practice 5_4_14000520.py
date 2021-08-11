def factorial(num):

    m = 1
    for i in range(1,num+1):
        m *= i
        if m == num:
            print(f"Yes your Number is Factorial({i})")
            break
        elif i == num and m != num :
            print("No ... your Number is Not Factorial")
num = int(input("Please Enter Your Number=  "))
factorial(num)