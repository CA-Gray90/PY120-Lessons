# Which of the following are objects in Python? If they are objects, how can you find out what class they belong to?

#     - True                        -> object, Bool class
#     - 'hello'                     -> object, Str class
#     - [1, 2, 3, 'happy days']     -> object, list class
#     - 142                         -> object, Int class
#     - {1, 2, 3}                   -> object, Set class
#     - 1.2345                      -> object, float class

print(type(True).__name__)                       # bool
print(type('hello').__name__)                    # str
print(type([1, 2, 3, 'happy days']).__name__)    # list
print(type(142).__name__)                        # int
print(type({1, 2, 3}).__name__)                  # set
print(type(1.2345).__name__)                     # float

print(True.__class__.__name__)                          # bool
print('hello'.__class__.__name__)                       # str
print([1, 2, 3, 'happy days'].__class__.__name__)       # list
print((142).__class__.__name__)                         # int
print({1, 2, 3}.__class__.__name__)                     # set
print(1.2345.__class__.__name__)                        # float