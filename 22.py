

a =4

def testfunc():
    global a
    a = 5
    print(a)


testfunc()
print(a)
