from matplotlib import pyplot as plt
from ukranian_letters_frequency import *


def frequency_histogram(text):

    official = UKRAINIAN_LETTER_FREQUENCES
    freq = {}
    count = 0
    for char in text.lower():
        if char.isalpha():
            count += 1
            if char in freq.keys():
                freq[char] += 1
            else:
                freq[char] = 1
    for key in freq.keys():
        freq[key] /= count
    plt.bar(freq.keys(), freq.values(), color='b', label="Test data")
    plt.bar(official.keys(), official.values(), color='r', width=0.5, label="Official data")
    plt.title("Hystogram")
    plt.legend()
    plt.show()
    return freq

def test():
    text = "Тест простоти Міллера–Рабіна або тест Міллера–Рабіна — це тест простоти: алгоритм, який визначає чи є надане число простим. Його початкова версія, яку розробив професор Міллер, є детерміністичною, але детермінізм покладається на недоведену узагальнену гіпотезу Рімана;[1] Міхаель Рабін змінив її, щоб отримати безумовний імовірнісний алгоритм.[2]"
    print(text)
    print(frequency_histogram(text))


if __name__ == '__main__':
    test()