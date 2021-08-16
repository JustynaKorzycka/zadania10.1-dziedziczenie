class Shape:
  def __init__(self, side_):
    self.side = side_
  def calculate_field(self):
    return 0

class Square(Shape):
  def __init__(self, length):
    super().__init__(length)
  
  def calculate_field(self):
    super().calculate_field()
    return self.side ** 2


def main():
  sq1 = Square(5)
  print(sq1.calculate_field())

if __name__ == '__main__':
  main()


