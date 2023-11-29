# class Father:
#     def land(self):
#         print("having five acer land")
#
# class Son(Father):
#     def money(self):
#         print("no money")
#
# s=Son()
# s.land
# s.money

class A:
    def disp(self):
        print("this is parent class")

class B(A):
    def disp(self):
        super().disp()
        print("this is child class")

obj=B()
obj.disp()

