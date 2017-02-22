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
# Generates Fig. 5: Cell activity profiles in the reticular formation. 
# LLBN and EBN discharge rates for 5, 10, and 20 degree saccades. 
# Input to left SG was set equal to 1, 1.75, and 2.5; in each case for 85 ms
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

fig_name	= 'fig5.eps'
fig_size 	= np.multiply([8.5,11.6],.394)
fig_rows 	= 2
fig_cols 	= 1
fig_plots	= fig_rows*fig_cols
ppi			= 1200
face	 	= 'white'
edge	 	= 'white'

ax 		 	= [None]*fig_plots
fig 		= pl.figure(facecolor = face, edgecolor = edge, figsize = fig_size)
for i in range(0,fig_plots):
	col 	= np.mod(i,2)	
	ax[i] 	= fig.add_subplot(fig_rows,fig_cols,i+1)
	ax[i].set_ylim([-1.,1.5])
	ax[i].locator_params(axis='y',nbins=3)


###########################################
#### 		set up experiment			 ##
###########################################

# input & external electric stimulation
I  			= [1.,1.75,2.5] 
J   		= 0.

nest.SetStatus(Ext,{'mean': J})

# timing protocol (in ms)
preStim  	= 50
Stim     	= 85
postStim 	= 65

# time vector T
t_start 	= 0
t_end   	= preStim + Stim + postStim
t_steps 	= int((t_end-t_start)/dt)-1
T       	= np.linspace(t_start,t_end,t_steps)


###########################################
#### 	set up recording devices 		 ##
###########################################

MM 		= [None]*3
for s in range(0,3):
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

	nest.Connect(MM[s], LLBN[0], syn_spec = {'delay': dt})
	nest.Connect(MM[s], EBN[0], syn_spec  = {'delay': dt})


###########################################
#### 			simulation				 ##
###########################################

# pre-stimulus period
	nest.Simulate(preStim)

# stimulus period
	nest.SetStatus(LLBN[0],{'mean': I[s]})
	nest.Simulate(Stim)

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
	ax[0].plot(T,voltages[np.where(senders == LLBN[0])],linewidth=2)
	ax[0].get_xaxis().set_visible(False)
	ax[0].set_title('LLBN')

	ax[1].plot(T,voltages[np.where(senders == EBN[0])],linewidth=2)
	ax[1].set_title('EBN')
	ax[1].set_xlabel('time (ms)')	

pl.savefig(fig_name, format='eps', dpi=ppi)
pl.show()


	



