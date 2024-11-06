import Lab2

print("Lab2")

def test_find_min_max():
    arr = [30,10,80,90,40]
    result_arr = Lab2.find_min_max(arr)
    assert(result_arr[0] == 10)
def test_calc_average():
    arr = [30,10,80,90,40]
    result_arr = Lab2.calc_average(arr)
    assert(result_arr == 50)

def test_calc_median_temperature():
    arr = [30,10,80,90,40]
    result_arr = Lab2.calc_median_tempterature(arr)
    assert(result_arr == 80)
