def find_large_pal():
    large_pal = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            number = i * j
            if str(number)[::-1] == str(number) and large_pal < number:
                large_pal = number
    return large_pal

if __name__ == "__main__":
    print find_large_pal()