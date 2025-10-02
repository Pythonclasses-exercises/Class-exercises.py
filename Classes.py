class Employee:
  def __init__(self, first, last, email, payment):
    self.first = first
    self.last = last
    self. payment = payment
    self.email = email
  
  def full_name(self):
    return self.first + ' ' + self.last

emp_1 = Employee('Keza', 'Jesca','Keza.Jesca@comany.com', 5000)
emp_2 = Employee('Stella', 'Gatesi','Stella.Gatesi@comany.com', 7000 )

print(emp_1.email)
print(emp_2.payment)
print(emp_2.full_name())