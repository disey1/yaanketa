name = "Alex"
name_2 = name
name = name + "1"
print(name)
print(name_2)


name_str = "Alex"
number_int = 1
number_float = 1.2
logic_bool = True
logic_1_bool = False

print(type(name_str))
print(type(number_int))
print(type(number_float))
print(type(logic_bool))


привет = 432
print(привет)

print(5 ** 3) #Возведение в степень

number = 10
number2 = '10'
print(number + 10)
print(number2 + number2)
print(number * 10)
print(number2 * 10)

print("Your name:")
name = input()
print("Wellcome " + name)



print("Type of your age:")
age = int(input())
if age > 20:
    print('Bag')
elif age == 20:
    print("Good")
else:
    print("Wheel")

for i in range(51):# 0 - 50
    print(i)

for i in range(9,51,10):# 0 - 50 шаг в 10
    print(i)

name = input("Type your name: ")
print("Wellcome " + name)
print(f"Wellcome {name}")#analog