from view import select_model
from view import get_data
from logger import log_expression as log_ex
from logger import log_ansver as log_ansv

def get_logs():
    read_logs = open('log.txt', 'r')
    for line in read_logs:
        print(line)
    read_logs.close()
    

def start_calculations(data = get_data()):
    log_ex("".join(data))
    if select_model(data) == 'rational':
        from model_rational_numbers import calculator
    else:
        from model_complex_numbers import calculator
    result = calculator(data)
    result = result[0]
    log_ansv(result)
    print(f'Ответ = {result}')


start_calculations()
get_logs()