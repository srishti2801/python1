# function can have default parameters if you want
# default params are added after required params

def add(a,b,c=1,d=0):
    return a+b+c+d




if __name__ == "__main__":
    out = add(20,20)
    print(out)
    out = add(20,20,10)
    print(out)
    out = add(20,20,10,20)
    print(out)
    out = add(20,20,c=10)
    print(out)
    out = add(20,20,d=20)
    print(out)
    out = add(20,20,d=20,c=10)
    print(out)
    out = add(20,d=20,c=10,b=20)
    print(out)