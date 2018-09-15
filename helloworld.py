
msg = "hello world"
print(msg.upper())

simpleList = [1, 2, 3]
for item in simpleList:
    print(item)

print('List Length')
print (len(simpleList))

class Calculator:
    def __init__(self, a, b):
            self.num1 = a
            self.num2 = b
    
    def add(self):
        return self.num1 + self.num2

x = Calculator(50, 100)
print(x.add())





