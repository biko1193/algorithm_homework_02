import selection;

list1 = [4, 7, 2, 3, 9, 5, 1, 0, 8, 6]
list2 = [33, 65, 11, 232, 554, 3, 45, 91, 0, 334, 23, 7]

def test():
    assert 4 == selection.partition(list1)
    assert 5 == selection.partition(list2)
