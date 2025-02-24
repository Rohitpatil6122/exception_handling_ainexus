def divby_zero(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("cannot be devided by zero")
    # except TypeError:
    #     print("please enter int")
    finally:
        print("i will always execute ")
    print("i am rohit")
divby_zero(0,"a")