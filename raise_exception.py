def raise_excep():
    age=int(input("enter the age"))
    if age>18:
        print("please process")
    else:
        raise Exception("age should be greater than 18")
    print("rest code")
raise_excep()