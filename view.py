def get_data():
    data = input('Введите выражение для рассчета: ')
    expression_list = [el for el in data]
    return expression_list

def select_model(text):
    model = 'rational'
    for el in text:
        if el == 'j':
            model = 'complex'
    return model