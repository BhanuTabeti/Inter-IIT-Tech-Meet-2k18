from machine import Pin
from machine import I2C
from time import sleep
from math import atan2, pi

def map(val, in_min, in_max, out_min ,out_max):
		return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class MPU6050():
	"""docstring for MPU6050"""
	def __init__(self, scl, sda):
		super(MPU6050, self).__init__()
		# Pins for SCl And SDA
		self.scl = scl
		self.sda = sda
		# Register Address
		self.address = 104

		# Setting UP IC
		self.i2c = I2C(scl = Pin(self.scl), sda = Pin(self.sda))
		# Initialisation
		self.i2c.start()
		self.i2c.writeto(self.address, bytearray([107,0]))
		self.i2c.stop()

		# Other Required Variables
		self.minVal = 265
		self.maxVal = 402
		self.RAD_TO_ANG = 57.3

	def map(self, val, in_min, in_max, out_min ,out_max):
		return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
		pass
		
	def int16(self, x):
		if x > 32767:
			return x - 65536
			pass
		return x
		pass

	def data(self):
		self.i2c.start()
		rawVal = self.i2c.readfrom_mem(self.address, 0x3B, 14)
		self.i2c.stop()
		
		if len(rawVal) != 14:
			return self.data()
			pass
		result = []

		Acx = (self.int16(rawVal[0] << 8 | rawVal[1]))
		Acy = (self.int16(rawVal[2] << 8 | rawVal[3]))
		Acz = (self.int16(rawVal[4] << 8 | rawVal[5]))

		xAng = self.map(Acx, self.minVal, self.maxVal, -90, 90)
		yAng = self.map(Acy, self.minVal, self.maxVal, -90, 90)
		zAng = self.map(Acz, self.minVal, self.maxVal, -90, 90)

		result.append(self.RAD_TO_ANG * (atan2(-yAng, -zAng) + 3.14))
		result.append(self.RAD_TO_ANG * (atan2(-xAng, -zAng) + 3.14))
		result.append(self.RAD_TO_ANG * (atan2(-yAng, -xAng) + 3.14))

		result.append((self.int16(rawVal[8] << 8 | rawVal[9]))/131)
		result.append((self.int16(rawVal[10] << 8 | rawVal[11]))/131)
		result.append((self.int16(rawVal[12] << 8 | rawVal[13]))/131)
		return result
		pass