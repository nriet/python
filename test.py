# coding=utf-8
from sys import argv
import time
import os,sys,getopt
import numpy as np
import datetime
from netCDF4 import Dataset
from shutil import copyfile

num1 = argv[1]
num2 = argv[2]
sum = int(num1) + int(num2)
print (sum)