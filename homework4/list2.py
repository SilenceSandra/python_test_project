def remove_adjacent(nums):
  mylist = []

  for num in nums:
      if not (num in mylist):
          mylist.append(num)
  return mylist


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    list3 = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))
    list3.extend(list1)
    list3.extend(list2)
    return list3


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('{0} got: {1} expected: {2}'.format(prefix, got, expected))


# Calls the above functions with interesting inputs.
def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print()
  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
