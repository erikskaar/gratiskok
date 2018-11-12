fruit = {'bananer':0, 'druer':1}
if 'bananer' in fruit:
    del fruit['bananer']
fruit['bringebær'] = 5
fruit['skogsbær'] = 3
fruit['jordbær'] = 20

for key, value in fruit.items():
    print(fruit)