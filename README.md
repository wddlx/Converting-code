# Converting-code
This code aims to convert an image of a disk with any PA and inclination to a face-on image in polar coordinates.


Inputs:
image: 2d array.

PA and inclination: Real number, default is 0.

center: The center of the disk. Default is the center of the image.

final_radius: The radius of the disk. Should be smaller than the distance from the center of the disk to the edge of the image. Default is 100.

pw: How many is the circle is divided into. 360/pw is the division value of the $\theta$ axis of the polar coordinates. The default value is 360.

r0 and times: We multiply the brightness of the disk with r^{times} to compensate for the dimming. r0 is where the brightness do not change, 
and times is how the compensation goes with r. The default of r0 is 40 and of times is 2.
