ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
N = len(ALPHABET)


def encryption(text, key):
    ciphertext = ''
    key_index = 0

    for i in text:
        symbol_index = (ALPHABET.index(i) + ALPHABET.index(key[key_index])) % N

        ciphertext += ALPHABET[symbol_index]

        key_index = key_index + 1

        if key_index == len(key):
            key_index = 0

    return ciphertext


def decryption(ciphertext, key):
    text = ''
    key_index = 0

    for i in ciphertext:
        symbol_index = (ALPHABET.index(i) + N - ALPHABET.index(key[key_index])) % N

        text += ALPHABET[symbol_index]

        key_index = key_index + 1

        if key_index == len(key):
            key_index = 0

    return text


if __name__ == '__main__':
    text_test = 'СЕМЕНЕНКО'
    key_test = 'ЁЗЪ'
    text_encrypt = encryption(text_test, key_test)
    print(text_encrypt)
    print(decryption(text_encrypt, key_test))
