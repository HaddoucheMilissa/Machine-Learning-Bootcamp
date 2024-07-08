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
py.append('ai')
print("after append",py) #add an element at the end
py.insert(3,"flask")
print("after insert",py)

L2=['PC','new list','hello']
#merge the 2 lists
py.extend(L2)
print("after extend",py)
print(len(py))
