


class test:
    def __init__(self, par):
        self.par = par



a = test(10)

def testfunc():
    a.par = 20
    print(a.par)



print(a.par)
testfunc()
print(a.par)


