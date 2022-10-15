# Задача: Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, 
# добавив в нее систему логирования.

from menu import get_logs as log
from menu import start_calculations as start

def go_menu():
    print('МЕНЮ\n1. История вычислений\n2. Рассчитать выражение')
    choose = int(input('Выберите 1 или 2: '))
    if choose == 1:
        print('\nИстория вычислений:')
        log()
    else:
        start()

go_menu()