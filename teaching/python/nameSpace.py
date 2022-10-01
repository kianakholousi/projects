# # name spaces
def f():
    print('Start f()')
    def g():
        print('Start g()')
        print('End g()')
        return
    g()
    print('End f()')
    return
f()

# variable scope
x = 'global'
def f():
    x = 'enclosing'
    def g():
        x = 'local'
        print(x)
    g() 
    print(x)
f()
print(x)

# print(dir(__builtins__))