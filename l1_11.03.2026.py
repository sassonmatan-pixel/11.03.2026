# create dictionary of yourself
# 'name', 'year_of_birth', 'address_city', 'height', 'phone', 'siblings' set/tuple/list

# BONUS: create dict of your addrres with: country, city, street
from pprint import pprint
dict_matan = {
    'name': 'matan',
    'year_of_birth': 2001,
     'address' : {
        'country': 'israel',
        'city': 'jerusalem',
        'street': 'leo picard'
    },
    'height': 1.70,
    'phone': 'samsung galaxy s22 ultra',
    'siblings': ['menashe', 'lior', 'sivan']
}

print(dict_matan['address']['city'])
print(dict_matan['siblings'][2])

dict_matan['height']+= 0.05
print()
print(2026 - dict_matan['year_of_birth'])
pprint(dict_matan)