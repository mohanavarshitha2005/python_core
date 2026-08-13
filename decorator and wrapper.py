def greet():
    print("this is py-21")
func=greet
def decortor1(func):
    def wrapper():
        print("hi")
        func()
        print("byee")
    return wrapper
greet=decortor1(greet)
greet()
greet()