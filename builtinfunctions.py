#abs
x=-2
print(abs(x))
x=7
print(abs(x))
#round
x=8.65
print(round(x))
x=3.12
print(round(x))
#max
l=[11,9,0,43,12,99,38]
print("the max is",max(l))
print("the min is",min(l))
#len
print(len(l))
#sum
print(sum(l)) #11+9+0+43+12+99+38
#all and any
l2=[True,True,True,False]
print("using all",all(l2)) 
print("using any",any(l2))
print("=====")
#convert type
x=10
print(type(x)) #10 is an int
print(str(x)) # 10 is a string
y='33'
print(type(y)) # 33 is a string
print(int(y)) # 33 is an int
k=12
print(float(k))
#convert lists / tuples
liste1=[6,41,88,29,546] 
print(tuple(liste1)) # output (6,41,88,29,546)
# creat a list of dictionary's keys and values
D={"banana":150,
   "water":60,
   "cherry":180,
   "strawberry":110
   }
print(list(D.keys()))
print(list(D.values()))

#bases
A=15
print(bin(A))
print(oct(A))
print(hex(A))

#input 
#x=int(input("enter your age:"))
#while(x<= 0 or x>=100):
  # x=int(input("enter your age correctly :"))
  
#format 
# withou using format 
age=23
name="Lyna"
x= "Lyna is 23 years old"
print(x)

# with format
age=20
name="Ali"
x="{} is {} years old".format(name,age)
print(x) # the output: 20 is Ali years old

# other syntax using fomrmat
