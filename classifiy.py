#-*-coding:utf-8-*-
import os
import sys
import numpy as np
from numpy import *
import cv2
from matplotlib import pyplot
import operator as op
import collections
import shutil



def flatten(x):
	b = str(x)
	b = b.replace('[', '')
	b = b.replace(']', '')
	a = list(eval(b))
	return a


def pHash(imagefile):
	"""get image pHash value"""
	image = cv2.imread(imagefile, 0)
	image = cv2.resize(image, (32, 32), interpolation=cv2.INTER_CUBIC)

	#create the two-diminese list
	h, w = image.shape[:2]
	vis0 = np.zeros((h,w), np.float32)
	vis0[:h, :w] = image

	#dct
	vis1 = cv2.dct(cv2.dct(vis0))
	vis1 = vis1[0:8, 0:8]

	img_list = flatten(vis1.tolist())

	avg = np.sum(img_list) * 1./len(img_list)
	avg_list = ['0' if i < avg else '1' for i in img_list]

	return ''.join(['%x' % int(''.join(avg_list[x:x + 4]), 2) for x in range(0, 8 * 8, 4)])


def hammingDist(s1,s2):
	assert len(s1) == len(s2)
	return np.sum([ch1 != ch2 for ch1, ch2 in zip(s1, s2)])





cur_path = os.getcwd()
orgimagedir = os.path.join(cur_path, "../tempdir_5/5_samples_merge_left_neg")
orgtemp = orgimagedir.split('/')[-1]
dirlist = os.listdir(orgimagedir)
for dir in dirlist:
	imagedir = os.path.join(orgimagedir, dir)
	imagelist = os.listdir(imagedir)

	while(1):
	#for i in range(len(imagelist)):
		print(len(imagelist))
		if len(imagelist) == 0:
			os.rmdir(imagedir)
			break
		#dstimagedir = os.path.join(cur_path, "../tempdir/car_%s"%imagelist[0])
		dstimagedir = os.path.join(cur_path, "../swei5/%s"%orgtemp)
		if not os.path.exists(dstimagedir):
			os.mkdir(dstimagedir)
		orgimagename = os.path.join(imagedir, imagelist[0])
		
		if len(imagelist) == 1:
			shutil.move(orgimagename, os.path.join(dstimagedir, imagelist[0]))
			break

		print(orgimagename)
		orghash1 = pHash(orgimagename)

		j=1
		while(1):
			imagename = os.path.join(imagedir, imagelist[j])
			if not os.path.exists(imagename):
				continue
			hash2 = pHash(imagename)
			out_score = 1 - hammingDist(orghash1, hash2)*1./(8*8/4)

			if out_score >= 0.8 and out_score < 1:
				#dstimagename = os.path.join(dstimagedir, imagelist[j])
				#shutil.move(imagename, dstimagename)
				print("remove file : ", imagename)
				os.remove(imagename)
				imagelist.remove(imagelist[j])
				j = j
			else:
				j = j+1
			if j == len(imagelist):
				break		

		shutil.move(orgimagename, os.path.join(dstimagedir, imagelist[0]))
		print("swei:", orgimagename)
		imagelist.remove(imagelist[0])
