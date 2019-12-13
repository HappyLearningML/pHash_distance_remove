#-*-coding:utf-8-*-
import os
import sys
import cv2

cur_path = os.getcwd()
print(cur_path)
imagedir = os.path.join(cur_path, "../pick_3")
dstimagedir = os.path.join(cur_path, "../brightness_pick_3")

for roots, parents, files in os.walk(imagedir):
	for f in files:
		imagename = os.path.join(roots, f)
		image = cv2.imread(imagename)
		if image is None:
			continue
		else:
			image = image * 2
			dstimagename = os.path.join(dstimagedir, f)
			cv2.imshow("test", image)
			cv2.imwrite(dstimagename, image)
			cv2.waitKey(10)
			print(imagename)
