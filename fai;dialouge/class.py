class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print('the name is',self.name)
    class mobile:
        def __init__(self,mobilename):
            self.mobilename=mobilename
        def mob(self):
            print('the mobilename',self.mobilename)
s1=student('hari')
s1.display()
s2=student.mobile('nokia')
s2.mob()