#!/usr/bin/env python
Program := BubbleSort

# Bubble sort function written in pycal
def bubblesort(l) =
  for i in range(len(l)) =
    for j in range(len(l) - 1, i, neg(1)) =
      if (l[j] < l[j - 1]) =
        swap(A, j, j - 1)
 
def swap(l, x, y) =
  tmp := l[x]
  l[x] := l[y]
  l[y] := tmp