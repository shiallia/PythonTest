

test1 = [1,2,3]
test2 = test1
test2.append(4)

print(test1)
print(id(test1))

print(test2)
print(id(test2))


test1 = (1,2,3)
test2 = test1
test2.append(4)

print(test1)
print(id(test1))

print(test2)
print(id(test2))
