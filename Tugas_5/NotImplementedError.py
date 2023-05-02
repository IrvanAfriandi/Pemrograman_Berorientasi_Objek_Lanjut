class MyBaseClass:
    def my_method(self):
        raise NotImplementedError("Method belum diimplementasikan")

class MySubClass(MyBaseClass):
    def my_method(self):
        print("Metode diimplementasikan")

try:
    base = MyBaseClass()
    base.my_method()
except NotImplementedError as e:
    print(e)

sub = MySubClass()
sub.my_method()
