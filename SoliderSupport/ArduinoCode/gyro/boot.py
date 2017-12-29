from time import sleep
from machine import ADC, Pin
import mpu6050

wrist    = mpu6050.MPU6050(22,23)
shoulder = mpu6050.MPU6050(18,19)

Thumb 	= ADC(Pin(39))
Index 	= ADC(Pin(34))
Middle 	= ADC(Pin(35))
Ring 	= ADC(Pin(32))
Little	= ADC(Pin(33))

Fingers = [0,0,0,0,0]

def setVal(x,val,thr):
	if val < thr:
		Fingers[x] = 1
		pass
	else:
		Fingers[x] = 0
		pass
	pass
while True:
	setVal(0, Thumb.read() , 1400)
	setVal(1, Index.read() , 2500)
	setVal(2, Middle.read(), 2750)
	setVal(3, Ring.read()  , 2500)
	setVal(4, Little.read(), 2500)
	print(Fingers + wrist.data() + shoulder.data(), end = '')
	print(",")
	sleep(.5)
	pass