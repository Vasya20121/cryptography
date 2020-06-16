import re
UA = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧЩШЬЮабвгґдеєжзиіїйклмнопрстуфхцчшщьюя1234567890-_':,. "
alp = dict(enumerate(UA))
alp_rev = dict(map(lambda x: x[::-1], enumerate(UA)))


def comparator(word1, word2):
    res = word1 * int(len(word2) / len(word1))
    for i in range(len(word1)):
        if len(res) == len(word2):
            break
        res += word1[i]
    return res


def encrypt(text, key):
    cipher = comparator(key, text)
    encrypted = ''.join([alp[(alp_rev[text[i]] + alp_rev[cipher[i]]) % len(UA)] for i in range(len(text))])
    return encrypted


def decrypt(text, key):
    cipher = comparator(key, text)
    decrypted = ''.join([alp[(alp_rev[text[i]] - alp_rev[cipher[i]]) % len(UA)] for i in range(len(text))])
    return decrypted

def test():
    keyword = "Допуск"
    text = "Тест простоти Міллера-Рабіна або тест Міллера-Рабіна - це тест простоти: алгоритм, який визначає чи є надане число простим."
    encrypted = encrypt(text, keyword)
    print(encrypted)
    decrypted = decrypt(encrypted, keyword)
    print(decrypted)

"""
P.S. вказав лише символи для укр. алфавіту, цифри і потрібні знаки для тестового тексту
"""
if __name__ == '__main__':
    test()