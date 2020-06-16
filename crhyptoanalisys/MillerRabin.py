def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
        return r


def MillerRabin(n, a=12, s=7):
    for j in range(1, s + 1):
        b = toBinary(n - 1)
        d = 1
        for i in range(len(b) - 1, -1, -1):
            x = d
            d = (d * d) % n
            if d == 1 and x != 1 and x != n - 1:
                return True  # Составное
            if b[i] == 1:
                d = (d * a) % n
                if d != 1:
                    return True  # Составное
                return False  # Простое
if __name__ == "__main__":
    print(MillerRabin(52, 7))