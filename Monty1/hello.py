print('Hello World')
print("Hello Friend")
print('I won\'t be able to come.')
print(2/2)
print('Football\\rugby')
name=input('Enter your name')
print('Hello {}'.format(name))
class BBIT:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def Student(self):
        print(f'My name is {self.first_name} {self.last_name}')
day=BBIT('David','Kinyanjui')
day.Student()
jac=BBIT('Jacob','Odhiambo')
jac.Student()
a=input("enter an integer")
b=input("enter an integer")
print(f"{a} multiplied by {b} is {a+b}.")