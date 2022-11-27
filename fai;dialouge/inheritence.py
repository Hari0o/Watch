class A:
    # try:
        def m1(self):
            print('method 1')
    # except Exception:
        # print('class error')
class B(A):
    def m2(self):
        print('method 2')
    
class C(A):
    def m3(self):
        print('method 3')
class D(B,C):
    def m4(self):
        print('method 4')
    
s1=D()
s1.m1()
# s1.m2()


