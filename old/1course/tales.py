import time

# if поедешь == 'направо':
#     коня_потеряешь()
# elif поедешь == 'прямо':
#     голову_сложишь()
# elif поедешь == 'налево':
#     жениться_заставят()
# else:
#     ни_с_чем_возвратишься()


def bay_the_elephant():
    отмазка = input('Купи слона!\n')
    while отмазка != 'покупаю':
        отмазка = input(f'Все говорят, {отмазка}, а ты купи слона!\n')
    print('Молодец! С тебя миллион!')



def infinity_tale(повторов=0):
    сказка = [
        'У попа была собака,',
        'он её любил.',
        'Она съела кусок мяса,',
        'он её убил.',
        '(Убил!)',
        '(ай-я-я-яй!)',
        '(ай-я-я-яй!)',
        '(ай-я-я-яй!)',
        '(ой-ё-ё-ой!)',
        '(ой-ё-ё-ой!)',
        '(ой-ё-ё-ой!)',
        'В землю закопал,',
        'надпись написал:'
    ]

    for строка in сказка:
        print('\t' * повторов + строка)
        time.sleep(2)

    infinity_tale(повторов + 1)





def say_my_name(his_name_is_spoken_times = 0):

    if his_name_is_spoken_times == 0:
        name = input('Say my name!\n')
    else:
        name = input(f'Y{"ee"*his_name_is_spoken_times}s...\n')
    
    name = name.lower()

    if 'beetlejuice' in name:
        his_name_is_spoken_times += 1
        
        if his_name_is_spoken_times < 3:
            say_my_name(his_name_is_spoken_times)
        else:
            print('Ouuu year!!!')
            return
    else:
        his_name_is_spoken_times = 0
        print(f'Ou, no! Not {name}!')
        say_my_name()


def tale_about_repka():
    фермер = 'Дэдка'
    овощ = 'Рэпка'

    print(
        f"Посадил {фермер} {овощ}.\n"
        f"Вырас {овощ} большая-прэбольшая.\n"
        f"Cтал {фермер} {овощ} из земли тащить."
    )

    цепочка = [овощ, фермер]

    помощники = ['Бабка', 'Внючка', 'Жючка', 'Кошка', 'Мышка']

    for помощник in помощники:
        print(
            f'Тянут потянут - вытянут нэ могут\n'
            f'\n'
            f'Позвал {цепочка[-1]} {помощник}\n'
        )

        цепочка.append(помощник)

        позади = помощник
        for тянущий in цепочка[::-1][1:]:
            print(f'{позади} за {тянущий}')
            позади = тянущий

    print(f'И вытянули {овощ}!')



def tale_about_niggers(x = 10):
    while x != 0:
        print(f'было {x} негритят')
        print(f'один умер')
        x = x - 1
        print(f' осталось {x} негтритят')
    print("никого не стало")



def tale_about_niggers_with_details():
    судьбы = [
        ('кушали медок', 'был ужален пчелой'),
        ('играли в баскетбол', 'застрял в корзине'),
        ('купались в озере', 'скушан крокодилом'),
        ('ходили без маски', 'заболел короной'),
        ('катались в метро', 'уехал за конечную'),
        ('сели в самолет', 'улетел в Австралию'),
        ('нюхали друг-друга', 'был слишком вкусный'),
        ('гуляли по тайге', 'встретил медведя'),
        ('заселились в отель', 'познакомился с Агатой Кристи'),
        ('валялись на траве', 'был утащен муравьями'),
    ]

    судьбы = судьбы[::-1]
    осталось = len(судьбы) + 1

    while осталось > 1:
        судьба = судьбы[осталось - 2]
        print(f'{осталось} негритят {судьба[0]}')
        осталось = осталось - 1
        print(f'Один {судьба[1]} и их осталось {осталось}')
    print('Последний негритенок вздохнул устало')
    print('Ушел из нашей сказки, и никого не стало')



if __name__ == '__main__':
    # infinity_tale(сказка)

    bay_the_elephant()


# # сказка_про_негритят()


