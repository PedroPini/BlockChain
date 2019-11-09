def any_data_string(arg1, arg2):
    return f'{arg1} {arg2}'

def decades(data):
    if(data / 10 > 0):
        decada = data/10;
        return f'Você tem {decada:1.0f} decadas'
    else:
        return 'Data invalida'
        




print(decades(40))
#print(any_data_string(10,"Pedro"))