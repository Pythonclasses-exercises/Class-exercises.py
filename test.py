class Test:
    def __init__(self, answer1, answer2):
        self.answer1 = answer1
        self.answer2 = answer2
    def answer(self):
      return  self.answer1 + self.answer2
    def divide(self):
       return self.answer1 / self.answer2
    def multiple(self):
       return self.answer1 * self.answer2
    def modulus(self):
       return self.answer1 % self.answer2
    
test1 = Test(14, 2)   
test2 = Test(15, 5)  


print(test1.answer())
print(test2.answer())
print(test1.divide())
print(test2.divide())
print(test1.multiple())
print(test2.multiple())
print(test1.modulus())
print(test2.modulus())