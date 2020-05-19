# -*- coding: UTF-8 -*-
# File: demo.py


import os, cv2
from pickled import *
from load_data import *

data_path = './data/floor'
file_list = './data/wood_test.lst'
save_path = './bin'

if __name__ == '__main__':
  data, label, lst = read_data(file_list, data_path, shape=96)
  pickled(save_path, data, label, lst, bin_num = 1)


