def niggers():
    niggers_count = 10
    while niggers_count:
        print(f'Было {niggers_count} негритят')
        niggers_count -= 1
        print(f'один выбыл, стало {niggers_count}')
    print('И никого не стало')


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



tale_about_niggers_with_details()