import math
import numpy
import pdb
from numpy import cos
from numpy import sin
from numpy import tan
from shellskeleton import shellskeleton

	# a = math.radians(30.0)
	# oc=cmecloud(30.*!dtor,2.,5,20,0.4,50)

def cmecloud(hang, distjuncin, nbvertsl, nbvertcirc, k, nbvertcircshell, distjuncisleadingedge=None):

	if distjuncisleadingedge is not None:
		distjunc=distjuncin*(1.-k)*cos(hang)/(1.+sin(hang))
	else:
		distjunc=distjuncin

	result=shellskeleton(hang, distjunc, nbvertsl, nbvertcirc, k)
	p = result[0]
	r = result[1]
	ca = result[2]
	##################
	#pdb.set_trace()
	##################
	nbp= p.shape[1]
	
	theta=numpy.linspace(0, 360.-360./nbvertcircshell, nbvertcircshell)
	#pdb.set_trace()
	theta = numpy.radians(theta)
	sintheta=sin(theta)

	OC=numpy.zeros((3,nbvertcircshell*nbp))

	for i in numpy.arange(0, nbp-1):
		OCtmp=r[i]*numpy.vstack( (cos(theta), sintheta*cos(ca[i]), sintheta*sin(ca[i]) ))

		for j in numpy.arange(0,nbvertcircshell-1):
			OCtmp[::,j]=OCtmp[::,j]+p[::,i]

		OC[::,(i*nbvertcircshell):((i+1)*nbvertcircshell)]=OCtmp	

	return OC