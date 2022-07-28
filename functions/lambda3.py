# take a list of numbers from user in a single input

numbers = list(map(int, input().split()))
print(numbers)

numbers_halved = list(map(lambda i: int(i)/2, input().split()))
print(numbers_halved)

x = [12,15,19,17,13,30]
x_odd = list(filter(lambda i: i%2!=0, x))
print(x_odd)