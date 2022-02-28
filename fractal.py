import matplotlib.pyplot as plt
# import pandas as pd
import math
myset = []
def serpenski(x,y,length,myset):
	if (length > 1):
		p1_x = x;
		p1_y = y;
		p2_x = x + length;
		p2_y = p1_y
		p3_x = p1_x + length * math.cos(math.pi/3);
		p3_y = p1_y + length * math.sin(math.pi/3);
		myset.append([p1_x,p1_y,p2_x,p2_y,p3_x,p3_y])
		#print(p1_x,p1_y,p2_x,p2_y, p3_x, p3_y)
		serpenski((p1_x + p2_x) / 2, (p1_y + p2_y) / 2,length / 3,myset)
		serpenski((p2_x + p3_x) / 2, (p2_y + p3_y) / 2,length / 4,myset)
		serpenski((p1_x + p3_x) / 2, (p1_y + p3_y) / 2,length / 4,myset)
		#serpenski()


length = 32
serpenski(0,0,length,myset)
#print(myset)
plt.xlim(-2, length + 2)
plt.ylim(-2, length + 2)
for i in myset:
	plt.scatter(i[0],i[1])
	plt.scatter(i[2],i[3])
	plt.scatter(i[4],i[5])
for i in myset:
	plt.plot( [i[0], i[2], i[4], i[0]]    ,   [i[1], i[3], i[5], i[1]] )
plt.show()

