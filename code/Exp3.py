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
# Generates Fig. 6: Visually guided saccades. 
# Input to the horizontal (right) and vertical (up) circuits were: (0.67, 0.08), (0.7, 0.22), (0.74,0.4), (0.75, 0.6), (0.7, 0.9).
# These inputs were left on for 75 ms.
#
# Note that neuron activations are no longer bounded from below at zero. Instead input to each neuron was passed through a rectified  
# linear signal function. Furthermore, signal function g (equation A11 in Gancarz & Grossberg; 1998) was replaced by a sigmoid 
# function. Finally, eye position in the horizontal (vertical) direction is given by 196*TN_right (196*TN_up) rather than by 
# 260*(TN_right-0.5) [260*(TN_up-0.5)] as described in equation A12 in Gancarz & Grossberg (1998)
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

# additional variables
g_pos		= 196.			# gain eye position

# figure setup
rcParams.update({'figure.autolayout': True})

fig_name	= 'fig6.eps'
fig_size 	= np.multiply([8.5,8.5],.394)
ppi			= 1200
face	 	= 'white'
edge	 	= 'white'
fig 		= pl.figure(facecolor = face, edgecolor = edge, figsize = fig_size)
ax 			= fig.add_subplot(1,1,1)

ax.axhline(color='k',linestyle='--')
ax.axvline(color='k',linestyle='--')
ax.set_xlim([-20.,20.])
ax.set_ylim([-20.,20.])
ax.locator_params(axis='x',nbins=5)
ax.locator_params(axis='y',nbins=5)
ax.set_xlabel('horizontal eye position (deg)')
ax.set_ylabel('vertical eye position (deg)')


###########################################
#### 		set up experiment			 ##
###########################################

# input & external electric stimulation
I_horizontal  		= [.67,.70,.74,.75,.70]
I_vertical  		= [.08,.22,.40,.60,.90] 
J   				= 0.

nest.SetStatus(Ext,{'mean': J})

# timing protocol (in ms)
preStim  	=  0
Stim     	= 75
postStim 	=  0

# time vector T
t_start 	= 0
t_end   	= preStim + Stim + postStim
t_steps 	= int((t_end-t_start)/dt)-1
T       	= np.linspace(t_start,t_end,t_steps)


###########################################
#### 	set up recording devices 		 ##
###########################################

MM 		= [None]*5
for s in range(0,5):
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

	nest.Connect(MM[s], TN[1], syn_spec = {'delay': dt})
	nest.Connect(MM[s], TN[3], syn_spec = {'delay': dt})


###########################################
#### 			simulation				 ##
###########################################

# pre-stimulus period
	nest.SetStatus(TN[1],{'rate': 0.})
	nest.SetStatus(TN[3],{'rate': 0.})
	nest.Simulate(preStim)

# stimulus period
	nest.SetStatus(LLBN[1],{'mean': I_horizontal[s]})
	nest.SetStatus(LLBN[3],{'mean': I_vertical[s]})
	nest.Simulate(Stim)

# post-stimulus period
	nest.SetStatus(LLBN[1],{'mean': 0.})
	nest.SetStatus(LLBN[3],{'mean': 0.})
	nest.Simulate(postStim)


###########################################
#### 			create figure			 ##
###########################################

# gather data from recording device
	data 	 = nest.GetStatus(MM[s])
	senders  = data[0]['events']['senders']
	voltages = data[0]['events']['rate']

# compute output variables (horizontal and vertical eye position)
	theta_h = g_pos*voltages[np.where(senders == TN[1])]
	theta_v = g_pos*voltages[np.where(senders == TN[3])]
	
	ax.plot(theta_h,theta_v,linewidth=2)

pl.savefig(fig_name, format='eps', dpi=ppi)
pl.show()


