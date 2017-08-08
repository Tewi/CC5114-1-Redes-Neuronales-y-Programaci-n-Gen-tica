class PerceptronOR:
    def __init__(self):
        self.w1 = 1
        self.w2 = 1
        self.bias = 0

    def output(self, in1, in2):
        return 1 if (self.w1*in1 + self.w2*in2) + self.bias > 0  else 0
