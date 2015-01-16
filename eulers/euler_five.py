def find_smallest_multiple():
    tester = 20
    while True:
        important_var = False
        for i in range(1, 21):
            if tester % i != 0:
                important_var = True
                break
        if important_var:
            tester += 20
        else:
            return tester

print find_smallest_multiple()