class LFSR:
    def __init__(self, state, poly, n):
        self.state = state
        self.poly = poly
        self.n = n

    def generate(self):
        last = self.state & 1

        binary = bin(self.state & self.poly)[2:]

        new_bit = binary.count('1') % 2

        after_shift = (bin(self.state >> 1)[2:])
        self.state = int(str(new_bit) + after_shift.zfill(self.n - len(after_shift) - 1), 2)

        return last

    @staticmethod
    def combine(b1, b2, b3):
        return (b1 & b2) ^ ((b1 ^ 1) & b3)


if __name__ == "__main__":
    g1 = LFSR(int('11010', 2), int('10101', 2), 5)
    g2 = LFSR(int('1010000', 2), int('0101101', 2), 7)
    g3 = LFSR(int('00111110', 2), int('00001111', 2), 8)

    sequence = []
    for _ in range(10**4):
        sequence.append(LFSR.combine(g1.generate(), g2.generate(), g3.generate()))

    zeros = sequence.count(0)
    ones = sequence.count(1)
    print('Zeros = ' + str(zeros))
    print('Ones = ' + str(ones))

    r = []
    res = 0
    for i in range(1, 6):
        for j in range(10**4 - i):
            res += (-1)**(sequence[j] ^ sequence[j + 1])
        r.append(res)
        res = 0

    print('r-statistics: ' + str(r))

    print('sequence: ' + str(sequence))
