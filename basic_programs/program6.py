#logical operator(|,&)
a=True
b=False
out = a | b
print("a | b",out)
out = a & b
print("a & b",out)
out = a | a 
print("a | a",out)
out = b | b
print("b | b",out)
out = b | a
print("b | a",out)
