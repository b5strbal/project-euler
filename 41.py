# This file was *autogenerated* from the file 41.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_1 = Integer(1); _sage_const_1234 = Integer(1234)
def is_pandigital(n):
    return set(str(n)) == {str(x) for x in range(_sage_const_1 , len(n))}

is_pandigital(_sage_const_1234 )

