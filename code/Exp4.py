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
# Generates Fig. 7: Oblique staircase simulation. 
# Inputs to the horizontal and vertical circuits were held at (0.2, 0.33) for 300 ms
#
# Note that neuron activations are no longer bounded from below at zero. Instead input to each neuron was passed through a rectified  
# linear signal function. Furthermore, signal function g (equation A11 in Gancarz & Grossberg; 1998) was replaced by a sigmoid 
# function. In contrast to what is reported in the original study, given the present stimulation parameters, our model produces 2
# rather than 3 saccades. Finally, eye position in the horizontal (vertical) direction is given by 150*TN_right (150*TN_up) rather
# than by 260*(TN_right-0.5) [260*(TN_up-0.5)] as described in equation A12 in Gancarz & Grossberg (1998)
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
g_pos		= 150.			# gain eye position
sr 			= 5000 			# sampling rate

# figure setup
rcParams.update({'figure.autolayout': True})

fig_name	= 'fig7.eps'
fig_size 	= np.multiply([8.5,11.6],.394)
ppi			= 1200
face	 	= 'white'
edge	 	= 'white'
fig 		= pl.figure(facecolor = face, edgecolor = edge, figsize = fig_size)
ax 			= fig.add_subplot(1,1,1)

ax.set_xlim([0.,10.])
ax.set_ylim([0.,15.5])
ax.set_xlabel('horizontal eye position (deg)')
ax.set_ylabel('vertical eye position (deg)')


###########################################
#### 		set up experiment			 ##
###########################################

# input & external electric stimulation
I_horizontal = .20
I_vertical   = .33 
J   		 = .0

# timing protocol (in ms)
preStim  	 =   0
Stim     	 = 300
postStim 	 =   0

# time vector T
t_start 	 = 0
t_end   	 = preStim + Stim + postStim
t_steps 	 = int((t_end-t_start)/dt)-1
T       	 = np.linspace(t_start,t_end,t_steps)


###########################################
#### 	set up recording devices 		 ##
###########################################

multimeter = nest.Create('multimeter')
nest.SetStatus(multimeter, {'interval': dt, 'record_from': ['rate']})


###########################################
#### 		equilibration				 ##
###########################################

# let system reach equilibrium
# in the absence of input and stimulation
nest.Simulate(150)

###########################################
#### 	connect recording devices  		 ##
###########################################

nest.Connect(multimeter, TN[1], syn_spec = {'delay': dt})
nest.Connect(multimeter, TN[3], syn_spec = {'delay': dt})


###########################################
#### 			simulation				 ##
###########################################

# pre-stimulus period
nest.Simulate(preStim)

# stimulus period
nest.SetStatus(LLBN[1],{'mean': I_horizontal})
nest.SetStatus(LLBN[3],{'mean': I_vertical})
nest.SetStatus(OPN,{'mean': J})
nest.Simulate(Stim)

# post-stimulus period
nest.SetStatus(LLBN[1],{'mean': 0.})
nest.SetStatus(LLBN[3],{'mean': 0.})
nest.Simulate(postStim)


###########################################
#### 			create figure			 ##
###########################################

# gather data from recording device
data 	 = nest.GetStatus(multimeter)
senders  = data[0]['events']['senders']
voltages = data[0]['events']['rate']

# compute output variables (horizontal and vertical eye position)
theta_h = g_pos*voltages[np.where(senders == TN[1])]
theta_v = g_pos*voltages[np.where(senders == TN[3])]

ax.plot(theta_h[::sr],theta_v[::sr],'k.')


pl.savefig(fig_name, format='eps', dpi=ppi)
pl.show()



