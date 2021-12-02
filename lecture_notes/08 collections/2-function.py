# Implementation

def getFirstAndLast(array):
  first = array.pop(0)
  last = array.pop()
  return first, last

# Usage

ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
first, last = getFirstAndLast(ages)
print({ 'first': first, 'last': last })
