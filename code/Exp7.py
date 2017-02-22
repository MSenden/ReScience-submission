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
# Generates Fig. 10: Trading velocity and duration while keeping amplitude constant. 
# Only the shape of the input signal to the modelwas varied
# The weight W was set equal to 2. For the high velocity trial (dotted line), stimulation frequency F was 3,
# and stimulation duration was 62 ms. 
# For the low velocity trial (solid line), F was 1.3, and stimulation duration was 112 ms.
#
# Note that neuron activations are no longer bounded from below at zero. Instead input to each neuron was passed through a rectified  
# linear signal function. Furthermore, signal function g (equation A11 in Gancarz & Grossberg; 1998) was replaced by a sigmoid 
# function. Finally, simulation time was reduced compared to what was reported in the original paper: 82 ms for high velocity
# simulations and 117 ms for low velocity simulations. In contrast to the originally reported simulations, 
# in our simulations both combinations of stimulation frequency and duration lead to two consecutive saccades rather than one.
# -----------------------------------------------------------------------------

import pylab as pl
from matplotlib import rcParams
from itertools import cycle


###########################################
#### 		set up model				 ##
###########################################

execfile('setup_model.py')


###########################################
#### 			auxiliary				 ##
###########################################

# figure setup
rcParams.update({'figure.autolayout': True})

fig_name	= 'fig10.eps'
fig_size 	= np.multiply([8.5,11.6],.394)
fig_rows 	= 5
fig_cols 	= 1
fig_plots	= fig_rows*fig_cols
ppi			= 1200
face	 	= 'white'
edge	 	= 'white'

ax 		 	= [None]*fig_plots
fig 		= pl.figure(facecolor = face, edgecolor = edge, figsize = fig_size)
for i in range(0,fig_plots):
	ax[i] 	= fig.add_subplot(fig_rows,fig_cols,i+1)
	ax[i].get_xaxis().set_visible(False)
	ax[i].set_ylim([-1.,1.5])
	ax[i].locator_params(axis='y',nbins=3)

lines = ['k--','k-']
linecycler = cycle(lines)


###########################################
#### 		set up experiment			 ##
###########################################

# input & external electrict stimulation
F			= [3.,1.3]
W 			= 2.
J   		= 0.
nest.Connect(gS, LLBN[0], 'all_to_all', {'model': 'rate_connection', 'weight': W})
nest.SetStatus(Ext,{'mean': J})


# timing protocol (in ms)
preStim  	= 50
Stim		= [62,112]
postStim 	= [138,88]

# time vector T
t_start 	= 0
t_end   	= preStim + Stim[0] + postStim[0]
t_steps 	= int((t_end-t_start)/dt)-1
T       	= np.linspace(t_start,t_end,t_steps)


###########################################
#### 	set up recording devices 		 ##
###########################################

MM 			= [None]*2
for s in range(0,2):
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

	nest.Connect(MM[s], gS, syn_spec	  = {'delay': dt})
	nest.Connect(MM[s], OPN, syn_spec	  = {'delay': dt})
	nest.Connect(MM[s], LLBN[0], syn_spec = {'delay': dt})
	nest.Connect(MM[s], EBN[0], syn_spec  = {'delay': dt})
	nest.Connect(MM[s], TN[0], syn_spec   = {'delay': dt})


###########################################
#### 			simulation				 ##
###########################################

# pre-stimulus period
	nest.SetStatus(SC,{'mean': 0.})
	nest.Simulate(preStim)

# stimulus period
	nest.SetStatus(SC,{'mean': F[s]})
	nest.Simulate(Stim[s])

# post-stimulus period
	nest.SetStatus(SC,{'mean': 0.})
	nest.Simulate(postStim[s])

# reset rates for next simulation
	nest.SetStatus(SC,{'rate': 0.})
	nest.SetStatus(TN[0],{'rate': 0.})
	nest.SetStatus(TN[1],{'rate': 0.})
	

###########################################
#### 			create figure			 ##
###########################################

# gather data from recording device
	data 	 = nest.GetStatus(MM[s])
	senders  = data[0]['events']['senders']
	voltages = data[0]['events']['rate']

	l = next(linecycler)	
	
	ax[0].plot(T,voltages[np.where(senders == gS)],l)
	ax[0].set_ylabel('Input')

	ax[1].plot(T,voltages[np.where(senders == LLBN[0])],l)
	ax[1].set_ylabel('LLBN')

	ax[2].plot(T,voltages[np.where(senders == EBN[0])],l)
	ax[2].set_ylabel('EBN')

	ax[3].plot(T,voltages[np.where(senders == OPN)],l)
	ax[3].set_ylabel('OPN')

	ax[4].plot(T,voltages[np.where(senders == TN[0])],l)
	ax[4].get_xaxis().set_visible(True)
	ax[4].set_xlabel('time (ms)')
	ax[4].set_ylabel('TN')

pl.savefig(fig_name, format='eps', dpi=ppi)
pl.show()



