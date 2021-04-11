def generate(p, q, e):
    f = (p - 1) * (q - 1)

    def extend_gcd(x, y):
        if not y:
            return x, 1, 0

        res = extend_gcd(y, x % y)
        return res[0], res[2], res[1] - int(x / y) * res[2]

    return extend_gcd(f, e)


def crypt(x, e, n):
    def fast_pow(x, e):
        if e % 2:
            return (fast_pow(x, e - 1) * x) % n
        elif e:
            half = fast_pow(x, e // 2)
            return (half * half) % n
        else:
            return 1

    return fast_pow(x, e)


def print_options():
    print('1) Generate', '2) Encrypt', '3) Decrypt', '4) Exit', sep='\n')


if __name__ == "__main__":
    opt = 0

    while opt != 4:
        print_options()
        opt = int(input('option to choose: '))

        if opt == 1:
            p, q, e = int(input('p: ')), int(input('q: ')), int(input('e: '))
            print('n: ', p * q)
            print('ф(n): ', (p - 1) * (q - 1))
            gen = generate(p, q, e)

            print('incorrect values') if gen[0] != 1 else print('d: ', gen[2])
        elif opt == 2 or opt == 3:
            txt, key, n = int(input('text: ')), int(input('key: ')), int(input('n: '))

            print('result: ', crypt(txt, key, n)) if txt % n == txt else print('incorrect text input')
