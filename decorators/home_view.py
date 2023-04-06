
def hello_view(func):
    def wrapper(*args, **kwargs):
        print('Welcome!')
        func(*args, **kwargs)
    return wrapper

def bye_view(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('Good bye!')
    return wrapper

@hello_view
@bye_view
def main_view(text):
    print(text)

main_view('Shablon')

