#import fileformodule as ff
# liste=ff.fibonacci(20)
# print(liste)


#OR
#from fibonacci import * ( everything)

from fileformodule import fibonacci
liste=fibonacci(40)
print(liste)

# modules
import math
import statistics
import random
import os
import glob

# MATH
print(math.pi)
print(math.cos(0))
print(math.cos(2*math.pi))
print(math.exp(5))
print(math.log10(30))

# STATS
print(statistics.mean(liste))
print(statistics.variance(liste))
print(statistics.median(liste))

# RANDOM
print(random.choice(liste))
#print(random.seed(2)) to keep always the same result
print(random.choice(['ai','python','ml','dl']))
print(random.randint(10,20)) # int
print(random.random()) # float
print(random.randrange(30)) 
print(random.sample(range(30),11)) # gimme a list of 11 elements their range is 30

