import numpy
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
        val_lev = val_lev * (1 + (multi - 1) * 3)

    print('%d: %f, %f, val_3 : %f' % (num, multi, val, val_lev))

    return val_lev

def leverage_calc(max_days, start, end, lev_start):
    multi = (end / start) ** (1.0 / max_days)
    # print(multi)
    avg = multi.sum() / multi.size

    val_lev = lev_start
    start_tmp = start
    for i in range(max_days):
        val_lev = val_lev * (1 + (avg - 1) * 3)
    #     start_tmp = start_tmp * multi

    # print(start_tmp)
    # print(end)

    print('|%d|%f|%f|' % (max_days, avg,  val_lev))
    return val_lev

def main():
    print("start!!")
    # for i in range(10, 21):
    #     decrease(i, 10, 1)
    for i in range(10, 300, 10):
        increase(i)
    # leverage max =>
    # leverage min =>
    # max day => 1/1 , min day => 3/ 20 ==> total day =>  31 + 28 + 20 = 79
    # res = decrease(79, 1000, 300, 1000)
    # for i in range(1, 1001):
    #     increase(i, 300, 1000, res)
    max_2012 = numpy.array([85.73,130.55,128.94,101.10,82.29,100.11,123.34,229.81,121.20,102.41])
    max_2020 = numpy.array([65.7,121.01,86.27,69.90,68.01,45.90,119.70,153.35,96.89,69.14])
    min_2020 = numpy.array([26.84,59.39,34.24,30.69,18.95,9.13,46.66,61.76,38.61,32.62])
    current = numpy.array([58.34,109.0,74.58,75.04,57.32,31.23,87.35,163.59,79.03,60.93])
    days = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    for i in days:
        leverage_calc(i, current, max_2012, 170.44)

    for i in days:
        leverage_calc(i, current, max_2020, 170.44)

if __name__ == "__main__":
    main()