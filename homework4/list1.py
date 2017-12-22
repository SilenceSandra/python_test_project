def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
#  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
  print('{0} got: {1} expected: {2}'.format(prefix, got, expected))


def match_ends(words):
  a = 0

  for word in words:
    if len(word)>1 and word[0]==word[-1]:
        a += 1
  return a


def front_x(initiallist):
    xwords = []
    otherwords = []

    for word in initiallist:
        if word.startswith('x'):
            xwords.append(word)
        else:
            otherwords.append(word)
    return sorted(xwords) + sorted(otherwords)

print('\n', 'front_x')
test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


def last(t): return t[-1]
def sort_last(tuples):
    return sorted(tuples, key=last)

print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)] ))


def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\n', 'front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\n', 'sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
