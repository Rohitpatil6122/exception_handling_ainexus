def divby_zero(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("cannot be devided by zero")
    except TypeError:
        print("please enter int")
divby_zero(0,10)

