#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    store = []
    switch = 1
    for i in range(list_length):
        try:
            x = my_list_1 / my_list_2
        except ZeroDivisionError:
            print("division by 0")
            switch = 1
        except TypeError:
            print("wrong type")
            switch = 1
        except IndexError:
            print("out of Error")
            switch = 1
        finally:
            if switch:
                switch = 0
                store.append(0)
            else:
                store.append(x)
    return store
