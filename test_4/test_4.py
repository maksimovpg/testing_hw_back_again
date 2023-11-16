from one_hot_encoder import fit_transform
import pytest


def test_hello_world():
    actual = fit_transform('hello, world')
    expected = [('hello, world', [1])]
    assert actual == expected


def test_empty_string():
    with pytest.raises(TypeError):
        fit_transform()


def test_many_args():
    actual = fit_transform('foo', 'bar', 'baz')
    expected = [
        ('foo', [0, 0, 1]),
        ('bar', [0, 1, 0]),
        ('baz', [1, 0, 0])
    ]
    assert actual == expected


def test_meow():
    actual = fit_transform('a', 'd', 'c')
    expected = [
        ('a', [0, 0, 1]),
        ('d', [0, 1, 0]),
        ('c', [1, 0, 0])
    ]
    assert actual == expected
    assert ('j', [0, 0, 0]) not in expected
