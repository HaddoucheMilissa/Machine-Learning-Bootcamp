#tuples 
T1=(1,4,9,55,20)
print(T1[2])
print(T1[-2]) #befor last element
print(T1[-1]) #last element

#listes
L1=[1,8,3,55,42,0]
print(L1)
print("size of liste l1 is",len(L1))
py=['django','python','ML','DL']
print(py)
print("size of liste py is",len(py))
all=[L1,py]
print(all)
print("size of liste all is",len(all)) #output 2

print("3 first elements of py liste",py[:3])
print("2 last elements of py liste",py[2:])
print(py[1:3])
#using steps
print("using step",py[0:3:2])
print(py[::2])
print(py[::-1])

#deep in liste
py=['django','python','ML','DL']
py.append('Ai')
print("after append",py) #add an element at the end
py.insert(3,"flask")
print("after insert",py)

L2=['PC','new list','hello']
#merge the 2 lists
py.extend(L2)
print("after extend",py)
print(len(py))

#sorting list
py.sort()
print(py) #capital letter has the priority

py.sort(reverse=True)
print(py)

num=[5,77,61,92,4,1,71,4,10]
num.sort
print(num)
print(num.count(4))
num.pop(2) 
print(num)

#loop on py num
for i, value in enumerate(py):
    print(i,value)
    
#condition for the py list
if "django" in py :
    print("exists")
else:
    print("doesnt exists")
    
print("============")
mat=[16,8,42,15,25]
wilaya=["Alger","Bechar","Tipaza","Tizi-ouzou","constantine"]
for i,j in zip(mat,wilaya):
    print(i,j)
    
# practice 
# we want to print all the squares from 0 to 9 
listSquare=[]
for i in range (10):
    listSquare.append(i**2)
print(listSquare)
print("======")
# other method:list comprehension
listSquare2=[i**2 for i in range(10)]
print(listSquare)
print("======")
#nested list :
nested=[[i for i in range(5)]for j in range(3) ]
print(nested)

