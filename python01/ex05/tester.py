from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_grey
from pimp_image import ft_blue
import cv2

array = ft_load("landscape.jpg")
inverted = ft_invert(array)
cv2.imwrite("inversion.jpg", cv2.cvtColor(inverted, cv2.COLOR_RGB2BGR))
red = ft_red(array)
cv2.imwrite("red.jpg", cv2.cvtColor(red, cv2.COLOR_RGB2BGR))
green = ft_green(array)
cv2.imwrite("green.jpg", cv2.cvtColor(green, cv2.COLOR_RGB2BGR))
blue = ft_blue(array)
cv2.imwrite("blue.jpg", cv2.cvtColor(blue, cv2.COLOR_RGB2BGR))
grey = ft_grey(array)
cv2.imwrite("grey.jpg", cv2.cvtColor(grey, cv2.COLOR_RGB2BGR))
print(ft_invert.__doc__)
