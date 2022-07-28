number = [200,500,300]
out = map(str,number)
print(list(out))

out = map(lambda i: i/10, number)
print(list(out))


