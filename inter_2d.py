import utils as ut


class Interpolation:
    def __init__(self, file_name):
        self.data = ut.load(file_name, dem=2)
        self.inter_data = None
        self.calculate()
        self.plot()

    def calculate(self):
        c = []

    def plot(self):
        pass
