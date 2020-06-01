"""Tests for recursion excersises."""

import recursion


def test_count_vowels_empty():
    """Empty string returns 0."""
    assert recursion.count_vowels("") is 0


def test_count_vowels_simple():
    """Simple test cases."""
    assert recursion.count_vowels("abcde") == 2
    assert recursion.count_vowels("2bddeeniu") == 3


def test_count_vowels_upper_case():
    """Works with upper case characters."""
    assert recursion.count_vowels("AbCdE") == 2
    assert recursion.count_vowels("Python is FUN FUN FUN") == 5


def test_nested_sum_no_nesting():
    """Should handle non-nested lists."""
    assert recursion.nested_sum([1]) == 1
    assert recursion.nested_sum([1, 2, 3, 4]) == 10


def test_nested_sum_no_nested_edge_case():
    """Should handle non-nested lists."""
    assert recursion.nested_sum([]) == 0


def test_nested_sum_simple_nestings():
    """Test simple nestings."""
    assert recursion.nested_sum([[1, []]]) == 1
    assert recursion.nested_sum([[1, 2, 3, 4]]) == 10


def test_nested_sum_complex_nestings():
    """Test more complex nestings."""
    assert recursion.nested_sum([1, [1], [[1]], [[[1]]]]) == 4
    assert recursion.nested_sum([1, [1], [1, [1]], [1, [1], [1, [1]]]]) == 8
    assert recursion.nested_sum([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]) == 0


def test_permutations_empty():
    """Test permutations with empty input."""
    assert recursion.permutations("") == ['']


def test_permutations_simple():
    """Test permutations """
    assert recursion.permutations("xyz") == ['zyx', 'yzx', 'yxz', 'zxy', 'xzy', 'xyz']
    assert recursion.permutations("cat") == ['tac', 'atc', 'act', 'tca', 'cta', 'cat']


def test_permutations_no_duplicates():
    """Permutation list should not contain any duplicates."""
    aabc_perms = ['cbaa', 'bcaa', 'baca', 'baac', 'caba', 'acba', 'abca', 'abac', 'caab', 'acab', 'aacb', 'aabc']
    assert recursion.permutations("aabc") == aabc_perms



def test_permutations_long_strings():
    """Test permutations with longer inputs."""
    perms1 = recursion.permutations("Python")
    assert "Python" in perms1
    assert "hontyP" in perms1
    assert len(perms1) == 720

    perms2 = recursion.permutations("theeyes")
    assert len(perms2) == 840
    assert "theysee" in perms2
