a = [2, 6, 4, 8, 7, 0]
b = list(range(10))
c = [5, 0]
d = [5]*5
e = [i**2 for i in range(10)]
f = 0b10
g = 0x12c
h = 222
print(id(a))
a.append( i for i in range(100) if i % 7 == 0)
print(id(a))



print(id(b))
b.append(6)
print(id(b))



print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(hex(h))
