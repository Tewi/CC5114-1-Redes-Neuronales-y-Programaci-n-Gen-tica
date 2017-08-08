from PerceptronNAND import PerceptronAND
class SummingBitGate:

    def __init__(self):
        self.NAND = PerceptronNAND()

    def add(self, x1, x2):

        step1 = self.NAND.output(x1, step1)
        step2a = self.NAND.output(x1, step1)
        step2b = self.NAND.output(x2, step1)

        sumBit = self.NAND.output(step2a, step2b)
        carryBit = self.NAND.output(step1, step1)
