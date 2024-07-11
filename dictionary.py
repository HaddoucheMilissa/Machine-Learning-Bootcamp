dict1={"Alger":16,
       "Blida":9,
       "Adrar":1,
       "Bejaia":6
       }
print(dict1)

#in deep learning
import numpy as np 
settings={
    "W1": np.random.randn(1,20),
    "b1":np.random.rand(13,16),
    "W1":np.random.rand(20,1),
    "b2":np.random.rand(1,16),
}

#to get the values 
print(dict1.values())
#to get the keys
print(dict1.keys())
#to get the lenght
print("the lenght of my dict is:",len(dict1))
# to add an element 
dict1["tizi-ouzou"]=15
print(dict1)
#get method
print(dict1.get("constantine")) #the value doesnt exist
print(dict1.get("Alger")) #output 16

#fromkeys method
list1=("banana","water","tomato","kiwi","oil")
print(dict1.fromkeys(list1,"test"))

value= dict1.pop('Bejaia')
print(value)
print("======")
#print all the values 
for i in dict1.values():
    print(i)
print("======")
# print the keys and values
for i,j in dict1.items():
    print(i,j)
print("======")

<<<<<<< HEAD
dict1={
    '0':'frameworks',
    '1':'python',
    '2':'django',
    '3':'ai'
}
name=['frameworks','python','django','ai']
dico={k:v for k,v in enumerate(name)}
print(dico)
print(dico.keys())
print(dico.values())
=======
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

>>>>>>> 491c4dc498e384571bea8aab1fb3300fff391cae
