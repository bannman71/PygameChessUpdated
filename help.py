from pickletools import int4
import string
import numpy as np
from pyparsing import Char


temp_board = np.zeros([9, 9], dtype='S3')
temp_board[0, 0] = 'hlkj'
print(temp_board)

str = 'hello'

choppedstr = str[2:]

print(choppedstr)
print(float.is_integer((157.5 + 67.5) / 75))


rank = ((ord('A') - 64) * 75) - 66
print(ord('A'))
print(rank)
