a = {'Macbook' : 50000, 'HP' : 35000, 'Dell' : 40000}

# Loop Through Keys:
print('Keys:')
for keys in a:
    print(keys)

# Loop Through Values:
print('\nValues:')
for values in a.values():
    print(values)

# Loop Through Both Keys and Values:
print('\nBoth Keys And Values:')
for keys, values in a.items():
    print(f'{keys} : {values}')





