import math
import numpy
import pdb
from math import cos
from math import sin
from math import tan

def shellskeleton(alpha, distjunc, nbvertsl, nbvertcirc, k):

	pi = math.pi

	# -------- compute entire loop length
	looplength=distjunc*(1.0+(alpha+pi/2.0)*tan(alpha))

	# -------- compute circular part half length
	hcirclenght=distjunc*tan(alpha)*(2.0*alpha+pi)/2.0

	# ---- calculate the points of the straight line part
	pRstart=[sin(alpha),cos(alpha)]   # start on the limb
	pLstart=[-sin(alpha),cos(alpha)]
	pslR = numpy.zeros((3,nbvertsl))
	pslL = numpy.zeros((3,nbvertsl))
	rsl=numpy.zeros((nbvertsl))		# shell radius for the feet
	casl=numpy.zeros((nbvertsl))	# tilt angle of the plane of the circle
	step=(distjunc-1.)/(nbvertsl-1.)	# start on the limb

	gamma=math.asin(k)

	for i in numpy.arange(0, nbvertsl):
		xxx=i*step*sin(alpha)+pRstart[0]
		yyy=i*step*cos(alpha)+pRstart[1]
		pslR[1,i]=xxx
		pslR[2,i]=yyy
		pslL[1,i]=-pslR[1,i]
		pslL[2,i]=pslR[2,i]
		rsl[i]=tan(gamma)*math.sqrt(xxx*xxx + yyy*yyy)
		casl[i]=-alpha

	# ---- calculate the points of the circular part
	# rc=fltarr(nbvertcirc) ; radius of the shell for the circular part
	# cac=fltarr(nbvertcirc) ; tilt angle of the shell circle
	pcR=numpy.zeros((3,nbvertcirc))
	pcL=numpy.zeros((3,nbvertcirc))
	step=(alpha+pi/2.)/(nbvertcirc-1.)

	beta=numpy.linspace(-alpha, pi/2., nbvertcirc)
	hf=distjunc
	h=hf/cos(alpha)
	rho=hf*tan(alpha)
	
	X0=(rho+h*k**2*numpy.sin(beta))/(1.-k**2)
	rc=numpy.sqrt((h**2*k**2-rho**2)/(1.-k**2)+X0**2)
	cac=beta

	pcR[1::]=X0*numpy.cos(beta) 
	pcR[2::]=h+X0*numpy.sin(beta) 

	pcL[1::]=-pcR[1::]
	pcL[2::]=pcR[2::]

	r=numpy.concatenate((rsl, rc[1::], rc[len(rc)-2::-1], rsl[len(rsl)-2::-1]))
	ca=numpy.concatenate((casl, cac[1::], pi-cac[len(cac)-2::-1], pi-casl[len(casl)-2::-1]))

	pcL_rev = pcL[::, len(pcL[0, ::])-2::-1]
	pslL_rev = pslL[::, len(pslL[0, ::])-2::-1] 

	p=numpy.concatenate((pslR, pcR[::, 1::], pcL_rev, pslL_rev), axis=1)

	return [p, r, ca]