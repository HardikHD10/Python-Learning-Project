def add(*args) :
    sum = 0
    for n in args:
        sum += n
    return sum

# print(1,3,4,5,6,7,45,234,5645,23,78,43,106,800)

def Calculate(n,**kwargs):
    # for key,value in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

Calculate(2,add=3,multiply=4)
