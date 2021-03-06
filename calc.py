
# Leverage Calculation.

def increase(num, start = 1, end = 10, lev_start = 1):
    multi = (end / start) ** (1.0 / num)
    val = start
    for i in range(num):
        val = val * multi

    val_lev = lev_start
    for i in range(num):
        val_lev = val_lev * (1 + (multi - 1) * 3)

    print('%d: %f, %f, val_3 : %f' % (num, multi, val, val_lev))

    return val_lev

def decrease(num, start = 10, end = 1, lev_start = 10):
    multi = (end / start) ** (1.0 / num)
    val = start
    for i in range(num):
        val = val * multi

    val_lev = lev_start
    for i in range(num):
        val_lev = val_lev * (1 - (1 - multi) * 3)

    print('%d: %f, %f, val_3 : %f' % (num, multi, val, val_lev))

    return val_lev

def main():
    print("start!!")
    for i in range(10, 21):
        decrease(i, 10, 1)
    for i in range(1, 11):
        increase(i)
    # leverage max =>
    # leverage min =>
    # max day => 1/1 , min day => 3/ 20 ==> total day =>  31 + 28 + 20 = 79
    res = decrease(79, 1000, 300, 1000)
    for i in range(1, 1001):
        increase(i, 300, 1000, res)

if __name__ == "__main__":
    main()