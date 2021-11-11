#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from unittest import TestCase, main



def minimumAbsoluteDifference(arr):
    # Write your code here
    diff = []
    arr.sort()
    for  i in range(len(arr) - 1):
        diff.append(abs(arr[i + 1] - arr[i]))
    return min(diff)

    



class TestPractice(TestCase):
    def test_reverse(self):
        self.assertEqual(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]), 1)


              
if __name__ == "__main__":
    main()