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
# Generates Fig. 12: Interrupted saccade simulation. 
# Input to left side of saccade generator was set to 0.7 for 100 ms. 
# OPN stimulation J was set to 1.8 for 5 ms.
#
# Note that neuron activations are no longer bounded from below at zero. Instead input to each neuron was passed through a rectified  
# linear signal function. Furthermore, signal function g (equation A11 in Gancarz & Grossberg; 1998) was replaced by a sigmoid 
# function.
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

# figure setup
rcParams.update({'figure.autolayout': True})

fig_name	= 'fig12.eps'
fig_size 	= np.multiply([8.5,17.6],.394)
fig_rows 	= 6
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
	ax[i].set_xlim([0,200])
	ax[i].set_ylim([-1.,1.5])
	ax[i].locator_params(axis='y',nbins=3)


###########################################
#### 		set up experiment			 ##
###########################################

# input & external electrict stimulation
I  			=  .7
J   		= [1.8,0.]

# timing protocol (in ms)
preStim  	=  50
Stim_1     	=  45
Stim_2     	=   5
Stim_3     	=  55
postStim 	=  50

# time vector T
t_start 	= 0
t_end   	= preStim + Stim_1 + Stim_2 + Stim_3 + postStim
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

	nest.Connect(MM[s], OPN, syn_spec	  = {'delay': dt})
	nest.Connect(MM[s], Ext, syn_spec	  = {'delay': dt})
	nest.Connect(MM[s], LLBN[0], syn_spec = {'delay': dt})
	nest.Connect(MM[s], EBN[0], syn_spec  = {'delay': dt})
	nest.Connect(MM[s], TN[0], syn_spec   = {'delay': dt})


###########################################
#### 			simulation				 ##
###########################################

# pre-stimulus period
	nest.SetStatus(TN[0],{'rate': 0.})
	nest.SetStatus(TN[1],{'rate': 0.})
	nest.Simulate(preStim)

# stimulus period 1
	nest.SetStatus(LLBN[0],{'mean': I})
	nest.Simulate(Stim_1)

# stimulus period 2
	nest.SetStatus(Ext,{'mean': J[s]})
	nest.Simulate(Stim_2)

# stimulus period 3
	nest.SetStatus(Ext,{'mean': 0.})
	nest.Simulate(Stim_3)

# post-stimulus period
	nest.SetStatus(LLBN[0],{'mean': 0.})
	nest.Simulate(postStim)
	

###########################################
#### 			create figure			 ##
###########################################

# gather data from recording device
	data 	 = nest.GetStatus(MM[s])
	senders  = data[0]['events']['senders']
	voltages = data[0]['events']['rate']

#
	if (s<1):

		Input = np.zeros(t_end-t_start)
		Input[preStim+1:t_end-postStim] = I

		ax[0].plot(range(t_start,t_end),Input,'k')
		ax[0].set_ylabel('Input')

		ax[1].plot(T,voltages[np.where(senders == LLBN[0])],'k')
		ax[1].set_ylabel('LLBN')

		ax[2].plot(T,voltages[np.where(senders == EBN[0])],'k')
		ax[2].set_ylabel('EBN')

		ax[3].plot(T,voltages[np.where(senders == OPN)],'k')
		ax[3].set_ylabel('OPN')

		ax[4].plot(T,voltages[np.where(senders == TN[0])],'k')
		ax[4].set_ylim([-.01,.1])
		ax[4].set_ylabel('TN')

		ax[5].plot(T,voltages[np.where(senders == Ext)],'k')
		ax[5].get_xaxis().set_visible(True)
		ax[5].set_ylim([-1.,1.])
		pl.xlabel('time (ms)')
		pl.ylabel('OPNSTIM')

	else:
		ax[4].plot(T,voltages[np.where(senders == TN[0])],'k--')

pl.savefig(fig_name, format='eps', dpi=ppi)
pl.show()


