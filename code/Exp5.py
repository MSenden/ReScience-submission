# -----------------------------------------------------------------------------
# Distributed under the GNU General Public License.
#
# Contributors: Mario Senden mario.senden@maastrichtuniversity.nl
# -----------------------------------------------------------------------------
# References:
#
# Gancarz, G., Grossberg, S. "A Neural Model of the Saccade Generator in the Reticular Formation."
# Neural Networks 11, no. 7-8 (October 1998): 1159-74. doi:10.1016/S0893-6080(98)00096-3.
# -----------------------------------------------------------------------------
# File description:
# 
# Simulates reimplemented Gancarz & Grossberg (1998) model.
# Generates Fig. 8: Tuning curve for an excitatory burst neuron (EBN). 
# Inputs to the horizontal and vertical circuits: 
# (.2, 0., .63, .0),(0., 0., .7, 0.),(0., .2, .63, 0.),(0., .45, .45, 0.),
# (0., .7, 0., 0.),(0., .45, 0., .45),(0., .2, 0., .63),(0., 0., 0., .7),
# (.2, 0., 0., .63),(.45, 0., 0., .45),(0.63, 0., 0., .2),(0.7, 0., 0., 0.),
# (0.63, 0., .2, 0.),(0.45, 0., .45, 0.).
# The input was on for 50 ms.
#
# Note that neuron activations are no longer bounded from below at zero. Instead input to each neuron was passed through a rectified  
# linear signal function. Furthermore, signal function g (equation A11 in Gancarz & Grossberg; 1998) was replaced by a sigmoid 
# function. Finally, eye position in the horizontal (vertical) direction is given by 196*TN_right (196*TN_up) rather than by 
# 260*(TN_right-0.5) as described in equation A12 in Gancarz & Grossberg (1998)
# -----------------------------------------------------------------------------

import pylab as pl
from matplotlib import rcParams


###########################################
#### 		set up model				 ##
###########################################

execfile('setup_model.py')


###########################################
#### 			auxiliary				 ##
###########################################

# declare outcome variables:
# EBN activity (r) per saccade angle (a)
r			= np.zeros(15)
a			= np.zeros(15)

# figure setup
rcParams.update({'figure.autolayout': True})

fig_name	= 'fig8.eps'
fig_size 	= np.multiply([8.5,8.5],.394)
ppi			= 1200
face	 	= 'white'
edge	 	= 'white'
fig 		= pl.figure(facecolor = face, edgecolor = edge, figsize = fig_size)
ax 			= fig.add_subplot(1,1,1, projection='polar')
ax.set_rticks([.02, .11, .2])


###########################################
#### 		set up experiment			 ##
###########################################

# input & external electric stimulation
I			= [[.2, 0., .63, .0],[0., 0., .7, 0.],[0., .2, .63, 0.],[0., .45, .45, 0.],
				[0., .7, 0., 0.],[0., .45, 0., .45],[0., .2, 0., .63],[0., 0., 0., .7],
				[.2, 0., 0., .63],[.45, 0., 0., .45],[0.63, 0., 0., .2],[0.7, 0., 0., 0.],
				[0.63, 0., .2, 0.],[0.45, 0., .45, 0.]]
J   		= 0.

# timing protocol (in ms)
preStim  	=  0
Stim     	= 50
postStim 	=  0

# time vector T
t_start 	= 0
t_end   	= preStim + Stim + postStim
t_steps 	= int((t_end-t_start)/dt)-1
T       	= np.linspace(t_start,t_end,t_steps)


###########################################
#### 	set up recording devices 		 ##
###########################################

MM 			= [None]*14
for s in range(0,14):
	MM[s] = nest.Create('multimeter')
	nest.SetStatus(MM[s], {'interval': dt, 'record_from': ['rate']})


###########################################
#### 		equilibration				 ##
###########################################

# let system reach equilibrium
# in the absence of input and stimulation
	nest.Simulate(150)

###########################################
#### 	connect recording devices  		 ##
###########################################

	nest.Connect(MM[s], EBN[0], syn_spec = {'delay': dt})


###########################################
#### 			simulation				 ##
###########################################

# pre-stimulus period
	nest.Simulate(preStim)

# stimulus period
	nest.SetStatus(LLBN[0],{'mean': I[s][0]})
	nest.SetStatus(LLBN[1],{'mean': I[s][1]})
	nest.SetStatus(LLBN[2],{'mean': I[s][2]})
	nest.SetStatus(LLBN[3],{'mean': I[s][3]})
	nest.SetStatus(OPN,{'mean': J})
	nest.Simulate(Stim)

# post-stimulus period
	nest.SetStatus(LLBN[0],{'mean': 0.})
	nest.SetStatus(LLBN[1],{'mean': 0.})
	nest.SetStatus(LLBN[2],{'mean': 0.})
	nest.SetStatus(LLBN[3],{'mean': 0.})
	nest.Simulate(postStim)


###########################################
#### 			create figure			 ##
###########################################

# gather data from recording device
	data 	 = nest.GetStatus(MM[s])
	senders  = data[0]['events']['senders']
	voltages = data[0]['events']['rate']

# compute output variables 
	a[s] = np.math.atan2(I[s][3]-I[s][2],I[s][1]-I[s][0])
	r[s] = np.mean(np.maximum(voltages[np.where(senders == EBN[0])],0.))
	
r[-1] = r[0]
a[-1] = a[0]

ax.plot(a, r,'-ko',linewidth=2)

pl.savefig(fig_name, format='eps', dpi=ppi)
pl.show()

