#-*-coding:utf-8-*-
import os
import sys
import cv2
import shutil

cur_path = os.getcwd()
orgimagedir = os.path.join(cur_path, "../5")


for roots, parents, files in os.walk(orgimagedir):
	for file in files:
		imagename = os.path.join(roots, file)
		son_dir = roots.split('/')[-1]
		print(son_dir)
		image = cv2.imread(imagename, 0)
		if image is not None:
			h, w = image.shape[:2]
			tempdir = os.path.join(cur_path, "../tempdir_5/%s/%dx%d"%(son_dir, h,w))
			print(tempdir)
			if os.path.exists(tempdir):
				shutil.move(imagename, os.path.join(tempdir, file))
				#cv2.imwrite(os.path.join(tempdir, file), image)
			else:
				os.mkdir(tempdir)
				shutil.move(imagename, os.path.join(tempdir, file))
				#cv2.imwrite(os.path.join(tempdir, file), image)


# for roots, parents, files in os.walk(orgimagedir):
# 	for file in files:
# 		imagename = os.path.join(roots, file)
# 		image = cv2.imread(imagename, 0)
# 		if image is not None:
# 			tempdir = os.path.join(cur_path, "../dstPdet")
# 			shutil.move(imagename, os.path.join(tempdir, file))
# 			print(file)