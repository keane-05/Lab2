import Lab2

print("Lab2")

def test_find_min_max():
    expected = [10.0, 90.0]
    arr = [30,10,80,90,40]
    result = Lab2.find_min_max(arr)
    assert(result == expected )
def test_calc_average():
    expected = 28.5
    arr = [30,10,80,90,40]
    result = Lab2.find_min_max(arr)
    assert(result == expected )

def test_calc_median_temperature():
    expected = 80
    arr = [30,10,80,90,40]
    result = Lab2.find_min_max(arr)
    assert(result == expected )
