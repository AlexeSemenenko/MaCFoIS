import re

ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
N = len(ALPHABET)


def gcd(a, b):
    if not b:
        return [1, 0, a]

    y, x, res = gcd(b, a % b)

    return [x, y - (a // b) * x, res]


def encryption(text, a, b):
    ciphertext = ''

    for i in text:
        symbol_index = (a * ALPHABET.index(i) + b) % N

        ciphertext += ALPHABET[symbol_index]

    return ciphertext


def decryption(ciphertext, a_1, b):
    text = ''

    for i in ciphertext:
        symbol_index = a_1 * (ALPHABET.index(i) - b) % N

        text += ALPHABET[symbol_index]

    return text


if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')

    if not a.isdigit() or not b.isdigit():
        print('\nIncorrect keys (should be only numbers)')
        exit()

    results = gcd(int(a), N)
    x = results[0]
    nod = results[2]

    if nod != 1:
        print('\nIncorrect keys (nod(a, N) should be != 1)')
        exit()

    text_test = input('Enter text: ').upper()
    text_test = re.sub(r'[^\w]', '', text_test)

    # print('Encrypted: ' + encryption(text_test, int(a), int(b)))
    print('Decrypted: ' + decryption(text_test, x, int(b)))
