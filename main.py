# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print('a')
name = '1'
num = 1

print(num)
print(name)
is_ok = True
print(is_ok, type(is_ok))

print(num, type(num))

new_num = int(name)
print(new_num, type(new_num))

print('Hi', 'Mike', sep=',', end='')
print('Hi', 'Mike', sep=',', end='.\n')

print(2 + 2)

import math

result = math.sqrt(25)
print(result)

y= math.log2(10)
print(y)

print('i don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello.\n How are you?')
print(r'C:\name\name')
print("###########")
print("""\
line1
line2\
""")
print("###########")

print('Hi.' * 3 + 'Mike.')

print('py''thon')
s = ('aaaaaaaaaaaa' 
    'bbbbbbbbbbbbbbb')
print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('############')
print(word[0:2])
print(word[:2])
print(word[2:])
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)

s = 'My name is Mike.Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike','Nancy'))
r = [1, 2, 3, 4, 5, 1, 2, 3]

print(r.index(3,3))
print(r.count(3))
if 100 in r:
    print('exit')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = '¥¥¥'.join(to_split)
print(x)

print(help(list))

i = [1,2,3,4,5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1,2,3,4,5]
y = x.copy()
# y = x[:]
y[0] = 100
print('y =', y)
print('x =', x)

X= 20
Y = x
y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

seat =[]
min = 0
max = 5

x= {'a':1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a':1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# l = [
#     ['apple'100]：
#     ['banana' : 200],
#     ['orange' : 300],
# ]
fruits = {
    'apple' : 100,
    'banana' : 200,
    'orange' : 300,
}


print(fruits['apple'])

# sintyou = float(input('身長入力してください＞ '))
# taijuu = float(input(
#     # '体重入力'
# ))
# bmi = taijuu/sintyou**2
#
# print('Bmi=' ,bmi, sep='')

# jisoku = float\
#     (input('時速>'))
# byousoku = jisoku/60**2
#
# print('byouso',byousoku,sep='')


satu = int(input('金額＞'))
man = satu%10000
sen = satu/10000%1000
hyaku = satu/10000/1000%100
juu = satu/10000/1000/100%10
go = satu/10000/1000/100/10%5
iti = satu/10000/1000/100/10/5%1

print(man,sen,hyaku,juu,go,iti,sep='')