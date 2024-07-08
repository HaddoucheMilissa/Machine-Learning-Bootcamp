def sign(x):
    if x>0:
        print(x,"is pos")
    elif x==0:
         print(x,"is null")
    else:
         print(x," is neg")
#calling sign function 
sign(0)
sign(-4)
sign(10)

# for loop
for i in range(5):
    print("my 1st loop",i)
# range can have 3 arguments

 #start from the number 8 till 15
print("==========")
for j in range(8,15):
    print("my 2nd loop",j)
print("==========")
# define the step
for k in range(8,15,3):
    print("my 3rd loop",k)
    
print("==========")

for z in range(5,-3,-2):
    print("my 4th function",z)
    sign(z)
    
x=2
while(x<10):
    print(x);x+=1
    