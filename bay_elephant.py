import random

def bay_elephant():
    gnilaya_otmaza = input('Купи слона!\n')

    while gnilaya_otmaza != 'покупаю':
        try:
            gnilaya_otmaza = input(f'Все говорят {gnilaya_otmaza}, а ты купи слона!\n')
        except UnicodeDecodeError:
            pass

    print('Молодец, с вас $100000000 за слона')
        
bay_elephant()