my_family = {'bror':[], 'sister':[], 'mor':[], 'far':[]}

def add_family_role(role, name):
    if role in my_family:
        my_family[role].append(name)
    else:
        my_family[role] = name
    return my_family

add_family_role('far', 'Bob')
add_family_role('bror', 'Arne')
add_family_role('bror', 'Per')
print(my_family)

