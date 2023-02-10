#!/usr/bin/env python
# coding: utf-8


import os
import sys

if __name__ == "__main__":

    fn = sys.argv[1]

    fp = open(fn,'r')
    data = fp.readlines()
    fp.close()

    data_dict = {}
    
    i=0
    while "END" not in data[i]:
        i += 1
        
        if "HOLDER" in data[i]:
            holder, hi = data[i].split()
            name, namei = data[i+1].split()
            title, titlei = data[i+5].strip().split(maxsplit=1)

            titlei = titlei.replace(' ', '').split(':')
            #titlei = titlei.split(':')[1].replace(' ', '')

            hi = int(hi.strip())
            namei = namei.strip()
            data_dict[hi] = {holder: hi, name: namei, title: titlei}
    
    for k in data_dict.keys():
        name = data_dict[k]['NAME']
        title = data_dict[k]['TITLE'][1]
        new_name = name + '_' + title

        
        if os.path.exists(name):
            os.rename(name, new_name)
        else:
            print( new_name, name, "does not exist" )
            








