#mathematique functions using lambda
#one variable
f1= lambda x: x**2 #f(x)=x**2
print("this is our 1st functionf",f1(4)) #32

#two variables
f2= lambda x,y:x**2+y
print("this is our 2nd function",f2(2,3))

#functions using def
def  area_triangle(base ,hauteur,a):
    a=2
    print("the area of our trianle is",int((base*hauteur)/2))

#calling function
area_triangle(4,6,2)