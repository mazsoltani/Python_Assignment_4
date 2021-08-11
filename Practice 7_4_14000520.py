def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
x = int(input("Please Enter a="))
y= int(input("Please Enter b="))
print("The L.C.M. is", compute_lcm(x, y))