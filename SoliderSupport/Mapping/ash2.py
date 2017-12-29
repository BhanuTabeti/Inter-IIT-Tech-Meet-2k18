import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import optimize

x1=0;
y1=0;

x2=3;
y2=0;

x3=3;
y3=-4;

power_ref=-44;

th=np.arange(0.0,2*math.pi,math.pi/50);

def db_distance(db):
   n=2
   #n=2-2.5 ideal open free space area
   return math.pow(10,(power_ref-db)/(10*n))

r1= 4
print r1
xunit1 = r1 * np.cos(th) + x1;
yunit1 = r1 * np.sin(th) + y1;
plt.plot(xunit1, yunit1);
plt.plot(x1,y1,'o');

r2= 5
print r2
xunit2 = r2 * np.cos(th) + x2;
yunit2 = r2 * np.sin(th) + y2;
plt.plot(xunit2, yunit2);
plt.plot(x2,y2,'o');

r3= 3
print r3
xunit3 = r3 * np.cos(th) + x3;
yunit3 = r3 * np.sin(th) + y3;
plt.plot(xunit3, yunit3);
plt.plot(x3,y3,'o');
plt.grid()


#function to find region of occerance 
#we do this by considering the distance from the 3 curves function and minimizing it
#that we do by taking the function and finding the partial derivatives wrt x,y and equating it to 0
def f(x):
# The minimizing function
   return math.pow(((x[0]-x1)*(x[0]-x1)+(x[1]-y1)*(x[1]-y1)-r1*r1),2)+math.pow(((x[0]-x2)*(x[0]-x2)+(x[1]-y2)*(x[1]-y2)-r2*r2),2)+math.pow(((x[0]-x3)*(x[0]-x3)+(x[1]-y3)*(x[1]-y3)-r3*r3),2)
#this functin finds the derivative and equals it to 0 and finds the corresponding coordinates
res=optimize.minimize(f, [1, 0], method="CG")    
x_out=res.x[0]
y_out=res.x[1]
print x_out,y_out
plt.plot(x_out,y_out,'o');
plt.show();
#plot()