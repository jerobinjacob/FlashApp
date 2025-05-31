# GENRATOR

print('Genrator')
def num_genrator():
    yield 1
    yield 2
    yield 3

gen = num_genrator()

for i in gen:
    print(i)


# ITERATOR

print('Iterator')
list = [10, 20, 30, 40]

iterator = iter(list)

print(next(iterator))
print(next(iterator))
