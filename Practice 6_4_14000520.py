def BMM(a,b):
    if a==b:
        print("BMM=",a)
    elif a<b:
        print("a<b")
    else:
        r=a/b
        t=b*int(r)
        if a==t:
            print("BMM=",b)
        else:
            b2=a-t
            a=b
            BMM(a,b2)
a=input('Please Enter a=')
b=input('Please Enter b=')
BMM(int(a),int(b))