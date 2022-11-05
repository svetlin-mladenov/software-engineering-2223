class Circle():
  def __init__(self, center, r):
    self.center = center
    self.r = r
  def __str__(self):
    return "Center: " + str(self.center) + ",  radius = " + str(self.r)
