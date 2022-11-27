# class student:
#     def sum(self,a=None,b=None,c=None):
#         s=0
#         if (a!=None and b!=None and c!=None):
#             s=a+b+c
#         elif (a!=None and b!=None):
#             s=a+b
#         else:
#             s=a
#         return s
# s1=student()
# print(s1.sum(10,20))

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        s1=self.m1+other.m1
        s2=self.m2+other.m2
        s3=student(s1,s2)
        return s3
s1=student(10,20)
s2=student(400,20)
s3=s1+s2
print(s3.m1,s3.m2)
