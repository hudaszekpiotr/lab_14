from app import bubble_sort
import pytest
import random



def test_empty_bubble_sort():
    arr = []
    expected_output = []
    assert bubble_sort(arr) == expected_output

def test_bubble_sort():
    arr = [1,2,3,4,5]
    expected_output = [1,2,3,4,5]
    assert bubble_sort(arr) == expected_output
 
def test2_bubble_sort():
    arr = [5,4,3,2,1]
    expected_output = [1,2,3,4,5]
    assert bubble_sort(arr) == expected_output

def test3_bubble_sort():
    arr = [0,12,1,4,5,2,1]
    expected_output = [0,1,1,2,4,5,12]
    assert bubble_sort(arr) == expected_output

def test5_large_list_sort():
    arr = list(random.sample(range(-20, 100000), 5000))
    expected_output = sorted(arr)
    assert bubble_sort(arr) == expected_output

def test4_descending_bubble_sort():
    arr = [0,12,1,4,5,2,1]
    expected_output = [12,5,4,2,1,1,0]
    assert bubble_sort(arr, False) == expected_output





