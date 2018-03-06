import matplotlib as mpl
from scipy.io.idl import readsav
from sys import argv
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import cmecloud
import math
import pdb

def rotation_matrix(x,y,z, angle, axis):
		
		# Perform rotations about 'axis' by angle

		theta = math.radians(angle)
		if axis == 'X': rot_matrix = [ [1.0, 0.0, 0.0], 
									   [0.0, cos(theta), -1.0*sin(theta)], 
									   [0.0, sin(theta), cos(theta)] ]

		if axis == 'Y': rot_matrix = [ [cos(theta), 0, sin(theta)], 
									   [0, 1, 0], 
									   [-1.0*sin(theta), 0, cos(theta)] ]

		if axis == 'Z': rot_matrix = [ [cos(theta), -1.0*sin(theta), 0], 
		                               [sin(theta), cos(theta), 0], 
		                               [0, 0, 1] ]

		xnew = x*(rot_matrix[ 0 ])[0] + y*(rot_matrix[ 0 ])[1] + z*(rot_matrix[ 0 ])[2]
		ynew = x*(rot_matrix[ 1 ])[0] + y*(rot_matrix[ 1 ])[1] + z*(rot_matrix[ 1 ])[2]
		znew = x*(rot_matrix[ 2 ])[0] + y*(rot_matrix[ 2 ])[1] + z*(rot_matrix[ 2 ])[2]

		return [xnew, ynew, znew]

script, rot_angle = argv
rot_angle = float(rot_angle)

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

angle = math.radians(30)
result = cmecloud.cmecloud(angle, 2., 5., 20., 0.4, 50.)

x = result[0, 0::2] 
y = result[1, 0::2] 
z = result[2, 0::2] 

result = rotation_matrix(x,y,z, rot_angle, 'Y')
x = result[0]
y = result[1]
z = result[2]



result = readsav('cme_cloud_points_t0.sav')
x = result['xcloud']
y = result['ycloud']
z = result['zcloud']

ax.plot(x, y, z, label='GCS Model')
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()