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

def setVal(x,val):
	Fingers[x] = val
while True:
	setVal(0, Thumb.read() )
	setVal(1, Index.read() )
	setVal(2, Middle.read())
	setVal(3, Ring.read()  )
	setVal(4, Little.read())
	print(Fingers + wrist.data() + shoulder.data(), end = '')
	print(",")
	sleep(.25)
	pass