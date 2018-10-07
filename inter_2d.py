import utils as us
import matplotlib as pl

class Interpolation:
    def __init__(self, file_name):
        self.data = us.load(file_name, dem=2)
        self.inter_data = None
        self.calculate()

    def calculate(self):
        pass

    def plot(self):
        pass
