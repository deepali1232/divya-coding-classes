#dictionary(key-value-pair)
d1={'apple':50,'mango':100,'guava':200,'banana':300}
print(d1)
print(type(d1))

#extracting keys                                                    
print(d1.keys())

#extracting values
print(d1.values())

#add new element in dict
d1['bag']=400
print(d1)

#change existing element or modify
d1['mango']=30
print(d1)

#update one dict value with another or append
stationary={'pen': 2,'rubber': 4,"bottle": 8}
books={'math':100,'english':400}
stationary.update(books)
print(stationary)

#pop an element
stationary.pop('rubber')
print(stationary)
