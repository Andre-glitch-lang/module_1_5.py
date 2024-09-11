# 1st program
my_dict = {'Vasya': 1975, 'Egor': 1990, 'Masha': 2002}
print("dict:",my_dict)
print("Existing value:",my_dict['Vasya'])
print("Not existing value:",my_dict.get('Andre'))
my_dict.update({'Leonid': 1993 , 'Alexandra': 1999})
a = my_dict.pop('Egor')
print("Deleted value:", a)
print("Modified dictionary",my_dict)

# 2st program
my_set = "яблоко",1,2,3,1,2,3,4,4,"яблоко"
my_set = set(my_set)
print("set:", my_set)
my_set.add(12)
my_set.add("виноград")
my_set.discard('яблоко')
print("Modified_set:", my_set)
