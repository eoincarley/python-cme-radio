import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import math
import pdb
import glob
from sys import argv
from scipy.io.idl import readsav
from mpl_toolkits.mplot3d import Axes3D

files = glob.glob('*_h*') 
image_num=0
for f in files:

	#pdb.set_trace()	
	result = readsav(f)

	x = result['xcloud']
	y = result['ycloud']
	z = result['zcloud']

	x = [x[j] for j in range(len(x)) if j % 20==0]
	y = [y[j] for j in range(len(y)) if j % 20==0]
	z = [z[j] for j in range(len(z)) if j % 20==0]


	# Make sphere
	u = np.linspace(0, 2 * np.pi, 200)
	v = np.linspace(0, np.pi, 200)
	xsphere = np.outer(np.cos(u), np.sin(v))
	ysphere = np.outer(np.sin(u), np.sin(v))
	zsphere = np.outer(np.ones(np.size(u)), np.cos(v))

	# Plot the surface
	fig = plt.figure(figsize=(10,9))
	ax = fig.gca(projection='3d')
	ax.plot_surface(xsphere, ysphere, zsphere, color='y', linewidth=0.1)


	ax.plot(x, y, z, '.', markersize=2.0, label='GCS Model')
	ax.set_xlabel('X Solar Radii')
	ax.set_ylabel('Y Solar Radii')
	ax.set_zlabel('Z Solar Radii')

	axis_limits=3.5
	ax.set_xlim((-1.0*axis_limits, axis_limits))
	ax.set_ylim((-1.0*axis_limits, axis_limits))
	ax.set_zlim((-1.0*axis_limits, axis_limits))


	# Now plot projection
	z = [-3.5 for j in z]
	zsphere = [-3.5 for j in zsphere]
	ax.plot(x, y, z, '.', markersize=2.0, label='GCS Model', color='deepskyblue')
	ax.plot_surface(xsphere, ysphere, zsphere, color='y', linewidth=0.1)

	#for angle in range(0, 360):

	ax.view_init(30, -60)
	#plt.draw()

	#fig.savefig('/Users/eoincarley/python/cme_cloud/pngs/image_'+str(format(image_num, '03'))+'.png')   # save the figure to file
	#plt.close(fig)
	#image_num +=1
	
	plt.show()
	pdb.set_trace()
	#plt.pause(.0001)