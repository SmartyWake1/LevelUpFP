from W2 import countRange

def countRange_as():
    lst = [1, 2, 3, 4]
    a_min = 1
    b_max = 4
    result = countRange(lst, a_min, b_max)
    assert result == [2, 3]
