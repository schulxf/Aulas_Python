def decoradora(func):
    print('Decorator 1')

    def wrapper(*args, **kwargs):
        print('Wrapper')
        res = func(*args, **kwargs)
        return res
    return wrapper

@decoradora
def soma(x,y):
    return x + y

print(soma(5,10))