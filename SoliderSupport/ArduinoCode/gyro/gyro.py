def map(val, in_min, in_max, out_min ,out_max):
		return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def int16(x):
	if x/32767:
		return -32768 + x%32767
		pass
	return x
	pass
	
from machine import Pin
from machine import I2C
from time import sleep
from math import atan2, pi

gyro1 = I2C(scl = Pin(23),sda = Pin(22))
# gyro2 = I2C(scl = Pin(17),sda = Pin(16))

gyro1.scan()
# gyro2.scan()

# [104]

address = 104
minVal	= 265
maxVal	= 402

RAD_TO_ANG = 57.3

gyro1.start()
gyro1.writeto(address, bytearray([107,0]))
gyro1.stop()

# gyro2.start()
# gyro2.writeto(address, bytearray([107,0]))
# gyro2.stop()

while True:
	gyro1.start()
	rawVal1 = gyro1.readfrom_mem(address, 0x3B, 14)
	gyro1.stop()

	# gyro2.start()
	# rawVal2 = gyro1.readfrom_mem(address, 0x3B, 14)
	# gyro2.stop()

	# print(rawVal)
	Acx1 = rawVal1[0] << 8 | rawVal1[1]
	Acy1 = rawVal1[2] << 8 | rawVal1[3]
	Acz1 = rawVal1[4] << 8 | rawVal1[5]

	# Acx2 = rawVal2[0] << 8 | rawVal2[1]
	# Acy2 = rawVal2[2] << 8 | rawVal2[3]
	# Acz2 = rawVal2[4] << 8 | rawVal2[5]
	
	# print(Acx, Acy, Acz)

	xAng1 = map(Acx1, minVal, maxVal, -90, 90)
	yAng1 = map(Acy1, minVal, maxVal, -90, 90)
	zAng1 = map(Acz1, minVal, maxVal, -90, 90)

	# xAng2 = map(Acx2, minVal, maxVal, -90, 90)
	# yAng2 = map(Acy2, minVal, maxVal, -90, 90)
	# zAng2 = map(Acz2, minVal, maxVal, -90, 90)

	# while True:
	# 	print(gyro.get_data())
	# 	sleep(1)
	# 	pass
	# print(xAng, yAng, zAng)
	x1 = RAD_TO_ANG * (atan2(-yAng1, -zAng1) + 3.14)
	y1 = RAD_TO_ANG * (atan2(-xAng1, -zAng1) + 3.14)
	z1 = RAD_TO_ANG * (atan2(-yAng1, -xAng1) + 3.14)
	
	# x2 = RAD_TO_ANG * (atan2(-yAng2, -zAng2) + 3.14)
	# y2 = RAD_TO_ANG * (atan2(-xAng2, -zAng2) + 3.14)
	# z2 = RAD_TO_ANG * (atan2(-yAng2, -xAng2) + 3.14)

	print(x1, y1, z1)
	# print(x1, y1, z1)

	sleep(0.5)
	pass



	# gyro1.readfrom_mem(address, 0x3B, 14)

