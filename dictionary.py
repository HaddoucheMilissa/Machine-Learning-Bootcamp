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
