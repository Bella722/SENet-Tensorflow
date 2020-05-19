'''
creat_list.py
'''

import os
import shutil
import random

woodtrain = open('data/wood_train.lst', 'w')
woodtest = open('data/wood_test.lst', 'w')

savedir = 'data/floor'
dirpath = 'F:/2019_DL_Nets/SENet-Tensorflow/dataset'

filelist = []
for parent, dirs, filenames in os.walk(dirpath):
    for subdir in dirs:
        labels = dirs.index(subdir)
        subfilelist = []
        for filename in os.listdir(os.path.join(parent, subdir)):
            objfile = os.path.join(parent, subdir, filename)
            desfile = os.path.join(savedir, str(labels) + "_" + filename)
            shutil.copyfile(objfile, desfile)
            subfilelist.append(str(labels) + "_"+ filename)
        random.shuffle(subfilelist)
        filelist.append(subfilelist)
    

ratio = 0.7
Tr_list = []
Te_list = []

for namelist in filelist:
    train_num = int(ratio*len(namelist))
    trainlist = namelist[0:train_num]
    for info in trainlist:
        Tr_list.append(info)
    vallist = namelist[train_num:]
    for info in vallist:
        Te_list.append(info)

random.shuffle(Tr_list)
for inf in Tr_list:
    woodtrain.write(inf + " " + inf[0][0] + "\n")
random.shuffle(Te_list)
for inf in Te_list:
    woodtest.write(inf + " " + inf[0][0] + "\n")

woodtest.close()
woodtrain.close()



