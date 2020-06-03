import numpy as np

import image


def test_read_image():
    im, a = image.read_image('data/sudoku1.jpg')
    assert (im.width, im.height) == (300, 300)
    assert a.shape == (300, 300)


def test_values_around():
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    assert image.values_around(a, 1, 1) == [1, 2, 3, 4, 6, 7, 8, 9]
    assert image.values_around(a, 0, 2) == [2, 5, 6]


def test_shrink():
    c = np.array([
        [True, True, True],
        [True, False, True],
        [True, False, True],
    ])
    expected = np.array([
        [False],
        [False],
    ])
    shrunk, position = image.shrink(c, (0, 0))
    assert np.array_equal(shrunk, expected)
    assert position == (1, 1)
