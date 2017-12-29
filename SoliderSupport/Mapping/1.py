from __future__ import print_function
import numpy as numpy
import matplotlib.pyplot as plt
from sympy.geometry import Circle, Point
from scipy import optimize
import tri
signal = []
N = 0
	
def getXY(X,Y):
	global N
	if X > Y:
		T = X
		X = Y
		Y = T 
		pass
	return (X-1)*(2*N-X)/2 + (Y - X - 1)
	pass

def printList(a):
	for x in xrange(0,len(a)):
		print(a[x],end=' ')
		pass
	print()
	pass

def getDistance(signal):
	distance = []
	powerRef = -44
	n_ = 2
    #n_=2-2.5 ideal open free space area

	for x in xrange(0,len(signal)):
		temp = math.pow(10,(powerRef - signal[x])/(10*n_))
		distance.append(temp)
		pass

	return distance
	pass

def main():
	global signal,N

	inputval = 1
	
	print("Total No. of Nodes: ", end = '')
	T = input()

	N = T
	noof = T*(T-1)/2

	distance = []

	for x in xrange(0,noof):
		temp = input()
		distance.append(temp)
		pass

	# distance = getDistance(signal)

	# printList(signal)
	printList(distance)

	print("Select Any Three for Ref: ", end = '')
	A = input()
	B = input()
	C = input()

	check = []

	for x in xrange(0,T):
		check.append(0)
		pass
	print(len(check))
	# Plotting A
	X1 = 0
	Y1 = 0
	plt.plot(X1,Y1,'o')
	check[A-1] = 1
	print(X1,Y1)

	X2 = distance[getXY(A,B)]
	Y2 = 0
	plt.plot(X2,Y2,'o')
	check[B-1] = 1
	print(X2,Y2)

	c1 = Circle(Point(X1,Y1),distance[getXY(A,C)])
	c2 = Circle(Point(X2,Y2),distance[getXY(B,C)])
	intersection = c1.intersection(c2)
	if len(intersection) == 0:
		print("Need to Improve in this case")
		return
		pass
	X3 = intersection[0].x
	Y3 = intersection[0].y
	plt.plot(X3,Y3,'o')
	check[C-1] = 1
	print(X3,Y3)

	# obj = tri.getFun(0,0,0,0,0,0,0,0,0)

	for y in range(0,T):
		if check[y] != 1:
			obj = tri.getFun(distance[getXY(A,y+1)],distance[getXY(B,y+1)],distance[getXY(C,y+1)],X1,X2,X3,Y1,Y2,Y3)
			res=optimize.minimize(obj.point,[1,0], method="CG")
			plt.plot(res.x[0],res.x[1],'o')
			print("Point : ",end='')
			print(y+1,res.x[0],res.x[1])
			pass
		pass
	pass

	plt.show()

if __name__ == '__main__':
	main()



# while True:
# 	print("Menu\n1.Add New\n0.Exit")
# 	inputval = input()
# 	if (inputval == 0):
# 		break
# 		pass
# 	temp = input()
# 	signal.append(temp)
# 	print("Added")
# 	pass