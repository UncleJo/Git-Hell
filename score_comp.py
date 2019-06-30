#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    l=len(a)
    k=len(b)
    sum1=0
    sum2=0

    for i in range (0,3):
        if a[i]>b[i]:
            sum1=sum1+1
        if a[i]<b[i]:
            sum2=sum2+1

    return (str(sum1)+""+str(sum2))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
