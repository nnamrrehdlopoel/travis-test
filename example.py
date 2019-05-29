##!/home/leo/l/sonstiges/Programme/anaconda/bin/pytest

def add(a, b):
	# if b == 0:
	# 	return a
	return a + b


def test_add():
    assert add(2, 3) == 5

# def test_add_3():
#     assert add('space', 'ship') == 'spaceship'

def test_add_3():
    assert add('space', 'ship') == 'spaceship'

def test_add_4():
    assert type(add(1, 0)) is int



def subtract(a, b):
    return a + b  # <--- fix this in step 8


# uncomment the following test in step 5
#def test_subtract():
#    assert subtract(2, 3) == -1
