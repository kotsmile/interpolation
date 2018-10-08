import utils as us


class Interpolation:
    def __init__(self, file_name):
        self.data = us.load(file_name, dem=3)
        us.plot_3d(self.data)
        self.inter_data = None
        self.calculate()
        self.plot()

    def calculate(self):
        pass

    def plot(self):
        pass
