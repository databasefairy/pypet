
cat = {
    'name': 'Sal',
    'hungry': True,
    'weight': 10.5,
    'photo': '(=^o.o^=)__'
}

def feed(pet):
    if pet['hungry']==True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
    else: 
        print pet['name']+' is not hungry'

print cat
feed(cat)
print cat