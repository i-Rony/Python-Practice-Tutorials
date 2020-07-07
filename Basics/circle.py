class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2