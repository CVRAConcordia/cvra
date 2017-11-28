from picamera import PiCamera
from time import sleep
import cv2
import numpy as np

camera = PiCamera()

camera.capture('foo.jpg')

img = cv2.imread('foo.jpg')

np.savetxt("foo.txt", img, delimiter=" ", fmt="%s")

