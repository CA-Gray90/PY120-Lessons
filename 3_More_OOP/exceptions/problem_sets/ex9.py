'''
Write two functions to fetch the sixth element from the list: one using the
LBYL approach and another using the AFNP approach. In both cases, the function
should return None when the element isn't found.
'''

numbers = [1, 2, 3, 4, 5]

# LBYL
def lbyl(lst):
    if len(lst) <= 5:
        return None
    return lst[5]

def afnp(lst):
    try:
        lst[5]
    except IndexError:
        return None
