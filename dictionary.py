# dictionary are key:val pairs

data = {1:'navin', 2:'kiran', 4:'harsh'}
print(data)

# enter key to get the value
print(data[4]) 
print(data.get(1))
print(data.get(3))

# set key 3 to a value which is not defined 
print(data.get(3, 'peri')) 

keys = ['navin', 'kiran', 'harsh']
values = ['python', 'java', 'js']

 # 2 ways to merge 2 list into a dictionary

data = dict(zip(keys, values)) 
print(data)

t={}
for k in range(len(keys)):
    t[keys[k]]=values[k]
print(t)

