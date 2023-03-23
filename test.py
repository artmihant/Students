from random import randint

def hello_world():
    print('Hello, World!')

def how_your_name():
    name = input('Как тебя зовут?\n')
    print('Привет,', name)

def double():
    num = int(input('Введите число?\n'))
    num = num * 2
    print(num)

# shoping_list = [
#     'apples',
#     'grape',
#     'melon',
#     'berres',
#     'juice',
#     'vodka'
# ]

# for element in shoping_list:
#     print(element)

def prime_list(N):

    def prime_test(number):
        if number%2 == 0 and number != 2:
            return False
        for i in range(3,int(number**(1/2))+1,2):
            if number%i == 0:
                return False
        return True

    res = [2]
    for i in range(3,100,2):
        if prime_test(i):
            res.append(i)
    return res

for p in prime_list(100):
    print(p**2)
