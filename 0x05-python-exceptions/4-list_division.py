#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for j in range(list_length):

        try:
            sumList = my_list_1[j] / my_list_2[j]

        except(ValueError, TypeError):
            print("wrong type")
            sumList = 0
        except ZeroDivisionError:
            print("division by 0")
            sumList = 0
        except IndexError:
            print("out of range")
            sumList = 0
        finally:
            new_list.append(sumList)
    return (new_list)
