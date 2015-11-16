#
# code to simplify supporting older python versions
#


import sys

from decimal import Decimal

if sys.version_info[:2] < (2, 7):

    # Pre-2.7 decimal and float did not compare correctly

    def numeric_greater(a, b):
        if isinstance(a, Decimal) and isinstance(b, float):
            return float(a) > b
        elif isinstance(a, float) and isinstance(b, Decimal):
            return a > float(b)
        else:
            return a > b

else:

    def numeric_greater(a, b):
        return a > b


try:
    from functools import cmp_to_key
except ImportError:
    def cmp_to_key(mycmp):
        'Convert a cmp= function into a key= function'
        class K:

            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0

            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0

            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0

            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0

            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0

            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
        return K
