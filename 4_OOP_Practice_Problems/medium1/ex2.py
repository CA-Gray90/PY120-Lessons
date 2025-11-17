'''
Without changing any of the below lines of code, update the InvoiceEntry class
so it functions as shown.
'''

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, num):
        self._quantity = num

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10000