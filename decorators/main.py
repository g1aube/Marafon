def i_am_top(func):
    def wrapper(*args, **kwargs):
        print('Start!')
        func(*args, **kwargs)
    return wrapper

def view_hello(hi_msg, bye_msg):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print(hi_msg)
            func(*args, **kwargs)
            print(bye_msg)
        return wrapper
    return inner_decorator

@i_am_top
@view_hello('Hello!', 'Bye!')
def view_link(links):
    print(f'''
{links} - !!!
''')

print(view_link('Links'))
