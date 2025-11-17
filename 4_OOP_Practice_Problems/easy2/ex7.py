class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())    # 'Amazon'
print(tv.model())           # 'Omni Fire'

print(Television.manufacturer())    # 'Amazon'
print(Television.model())           # TypeError, needs one argument, 'self' or object instance