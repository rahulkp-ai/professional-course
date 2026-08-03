# pip3 install pylint==2.11.1
# pip install --upgrade pylint astroid

def __add__(a,b):
    return a + b

num1 = 4
num2 = 5

total = __add__(num1,num2)

print("The sum of {} and {} is {}".format(num1,num2,total))
