##Python Decorator Function
#--A function that wraps another function and gives that some
#---additional functionality
import time

def delay_decorator(function):
    def wrapper_function():
        #Do something before
        time.sleep(2)
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello World")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()