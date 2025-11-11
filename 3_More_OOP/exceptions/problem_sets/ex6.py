'''Write a function that takes a list of numbers and returns the inverse of each
number (if n is a number, then 1 / n is its inverse). Handle any exceptions that
might occur.

i
- list of numbers
o
- return inverse of each number (new list?)

'''

def invert_nums(lst):
    new_list = []

    for num in lst:
        try:
            inverse = 1 / num
        except ZeroDivisionError as e:
            print(f'{e}: Replaced with 0')
            inverse = 0
        finally:
            new_list.append(inverse)

    return new_list

my_list = [1, 2, 3, 0]

print(invert_nums(my_list))