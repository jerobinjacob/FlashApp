# Method 1
print('Method 1')
a = {'Jerobin' : 22, 'Jeleena' : 17}
b = {'Jebin' : 21, 'Nitin' : 22}

a.update(b)
print(a)

# Method 2
print('Method 2')
c = {'Jerobin' : 22, 'Jeleena' : 17}
d = {'Jebin' : 21, 'Nitin' : 22}

merge = {**c, **d}
print(merge)

# Method 3
print('Method 3')
e = {'Jerobin' : 22, 'Jeleena' : 17}
f = {'Jebin' : 21, 'Nitin' : 22}

merge = a | b
print(merge)
