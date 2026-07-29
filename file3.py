class Calculator:
    def __init__(self):
        self.result = 0
    
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        if b != 0:
            self.result = a / b
            return self.result
        return None