# def fun_name():
# code...


# function for finding perimeter of a rectangle
def perimeter(l,b):
    p = 2 * (l + b)
    return p


if __name__ == "__main__":
    # use / call the function 
    out = perimeter(10,20)
    print("perimeter::" ,out)
    
    print("perimeter 2::",perimeter(20,20))