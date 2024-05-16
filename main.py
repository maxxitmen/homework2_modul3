#  Функции с параметром по умолчанию
def print_params (a=1, b='string', c=True):
    print(a, b, c)

print_params(b = 25)

print_params(c = [1,2,3])

print_params()

print_params(1, 5)

print_params('Georgyi')

# Распаковка

values_list = [2, 'no string', False]

values_dict = {'a' : 3, 'b' : 'KONO DIO DA', 'c' : False}

print_params(*values_list)

print_params(**values_dict)

values_list2 = [42, 'ответ на вопрос жизни, вселенной и воообще']

print_params(*values_list2, 42)