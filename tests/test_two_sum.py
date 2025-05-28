from problems.two_sum import two_sum

def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_multiple():
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]

def test_no_result():
    assert two_sum([1, 2, 3], 7) == []

