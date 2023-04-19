a = [10,20,30,40,50]

a.append(5)
a.append(6)
a.append(7)
print(a)

a.remove(50)
print(a)
a.pop(2)
print(a)
a.pop()
print(a)

a.sort()
print(a)

empty=[]
for val in a:
    if val >= 6 and val <= 20:
        empty.append(val)

empty=[0] * 10
empty[5] = 10
print(empty)

dog='dog'
three_dogs= dog*3
print(three_dogs)

squares = [i * i for i in range(1,10) if i%2==0]
print(squares)

animals = ['dog','cat','dog','turtle']
dogs = [animal for animal in animals if animal == 'dog']
print(dogs)

a_set = {1,2,3,3,3,3}
print(a_set)
a_list = [1,2,3,4,4,4,4]
no_dups = set(a_list)
print(no_dups)


fav_foods = {'kathleen': 'pizza', 'max':'burgers', 
             'matt':'chicken parm', 'andy':'ice cream'}
mff=fav_foods['matt']

for key in fav_foods:
    print(key, 'fav food is',fav_foods[key])

for key,val in fav_foods.items():
    print(key,'fav food is',val)

if 'christina' in fav_foods:
    print(fav_foods['christina'])
else:
    fav_foods['christina']='sushi'
print(fav_foods)