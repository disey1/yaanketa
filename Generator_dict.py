print("New branch")
print("New branch")
print("New branch")

set_1 = {'Lampa','Stol','Stul'}
print(type(set_1))
value = 1
shops_items = {key:value for key in set_1 }
print(shops_items)
print(shops_items.keys())

#Метод предоставляет вспомогательный конструктор, позволяющий создавать словари из последовательностей.

my_new_dict = dict.fromkeys(['one', 'two', 3])  # {'one': None, 'two': None, 3: None}
my_new_dict = dict.fromkeys(['one', 'two', 3], 10)  # {'one': 10, 'two': 10, 3: 10}