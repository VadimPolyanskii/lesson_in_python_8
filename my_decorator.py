# Написать свой декоратор
def show_prod(f):

    def wrapper(*args, **kwargs):
        print('Ниже произведение чисел!')
        print(f(*args, **kwargs))
        print('Это было произведение чисел!')
    return wrapper


# Функция произведения чисел
@show_prod
def prod(a,b):
    return a*b


prod(5,10)
