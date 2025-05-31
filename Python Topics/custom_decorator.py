def custom_decorator(hello):
    def wrapper():
        print('Before Decoration')
        hello()
        print('After Decoration')
    return wrapper

@custom_decorator
def hello():
    print('Hello')

hello()

