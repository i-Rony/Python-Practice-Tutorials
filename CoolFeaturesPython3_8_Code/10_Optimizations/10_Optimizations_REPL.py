# Example 01

# Python 3.7

import collections
from timeit import timeit
Person = collections.namedtuple("Person", "name twitter")
raymond = Person("Raymond", "@raymondh")

timeit("raymond.twitter", globals=globals())

# Example 02

# Python 3.8

import collections
from timeit import timeit
Person = collections.namedtuple("Person", "name twitter")
raymond = Person("Raymond", "@raymondh")

timeit("raymond.twitter", globals=globals())

# Example 03

# Python 3.7

import sys

sys.getsizeof(list(range(20191014)))

# Example 04

# Python 3.8

import sys

sys.getsizeof(list(range(20191014)))
