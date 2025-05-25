class Calculator():
    def __init__(self,a,b):
        print('I am a constructor')
        self.a=a
        self.b=b
    def add(self):
        print("Addition: ",self.a+self.b)
    def sub(self):
        print("Subraction: ",self.a-self.b)
    def mul(self):
        print("Multiplication: ",self.a*self.b)
    def div(self):
        print("Division: ",self.a/self.b)
    def calculate(a, b):
        print(a + b)
cal=Calculator(5,5)

cal.add()
cal.sub()
cal.mul()
cal.div()
Calculator.calculate(2, 3)