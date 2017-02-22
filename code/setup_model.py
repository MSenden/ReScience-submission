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
# Setup the Gancarz & Grossberg (1998) model in PyNEST for subsequent simulation
# -----------------------------------------------------------------------------

import nest
import numpy as np


###########################################
#### general setup & NEST initialization ##
###########################################

# simulation parameters 
dt     		= 1e-3	# time step for numerical integration (in ms)
delay  		= 1e-3	# conductance delay (in ms)
tau    		= 50.	# time constant (in ms) 
sigma  		= 0.0	# scaling factor of additive noise


# NEST kernel initialization
nest.ResetKernel()	 
nest.SetKernelStatus({'resolution': dt, 'use_wfr': False})


###########################################
#### creation of neuron & device objects ##
###########################################

# neuron parameters
# lambda			: passive decay rate 
# offset_ex			: offset in multiplicative coupling for excitatory input
# offset_in			: offset in multiplicative coupling for inhibitory input	
# g_in				: gain in multiplicative coupling for inhibitory input
# beta				: slope of sigmoid function
# bias				: inflection point of sigmoid function
# linear summation	: if false, gain function is applied to input before summation; if true, it is applied afterwards

Params_llbn = {'tau': tau,'std': sigma,'lambda':1.3,'linear_summation': False}
Params_ebn  = {'tau': tau,'std': sigma,'lambda':3.5,'offset_ex':2.,'offset_in':1.,'linear_summation': False}
Params_ibn  = {'tau': tau,'std': sigma,'lambda':2.4,'linear_summation': False}
Params_opn  = {'tau': tau,'std': sigma,'lambda':0.2,'offset_ex':1.,'offset_in':0.4,'g_in':3.5,'linear_summation': False}
Params_tn   = {'tau': tau,'std': sigma,'lambda':0.}
Params_sc   = {'tau': tau,'std': sigma}
Params_sigm = {'beta': 40., 'bias': .1}

# neurons 
LLBN 		= [None]*4
EBN  		= [None]*4
IBN  		= [None]*4
TN   		= [None]*4
OPN 		= nest.Create('rectifiedlin_rate_mult_ipn', 		# rectified linear gain function 
				params = Params_opn)
SC  		= nest.Create('lin_rate_ipn', 						# linear gain function
				params = Params_sc)

for i in range(0, 4):
    LLBN[i] = nest.Create('rectifiedlin_rate_ipn', 				# rectified linear gain function 
				params = Params_llbn)
    EBN[i]  = nest.Create('rectifiedlin_rate_mult_ipn',			# rectified linear gain function 
				params = Params_ebn)
    IBN[i]  = nest.Create('rectifiedlin_rate_ipn',				# rectified linear gain function 
				params = Params_ibn)
    TN[i]   = nest.Create('lin_rate_ipn',						# linear gain function 
				params = Params_tn)


# bias units (send constant activity)
E_plus 		= nest.Create(
    		 'lin_rate_ipn', 									# linear gain function 
				params={'tau': dt, 'mean': 1., 'std': sigma})	# constant input to EBN
P_plus 		= nest.Create(
    		 'lin_rate_ipn', 									# linear gain function 
				params={'tau': dt, 'mean': 1.2, 'std': sigma})	# constant input to OPN
Ext 		= nest.Create(
    		 'lin_rate_ipn', 									# linear gain function 
				params={'tau': dt, 'std': sigma}) 				# external stimulation of OPN

# output functions (EBNs and OPN)
gS  		= nest.Create('piecewiselin_out_function')			# piecewise linear gain function 
gP  		= nest.Create('sigmoid_out_function', 				# sigmoid gain function 
				params = Params_sigm)
gL  		= [None]*4
for i in range(0,4):
    gL[i] 	= nest.Create('sigmoid_out_function', 				# sigmoid gain function 
				params = Params_sigm)
    


###########################################
#### 			connections				 ##
###########################################

k 		= [1,0,3,2]
for i in range(0,4):
# to LLBNs
    nest.Connect(IBN[i], LLBN[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': -2.0})
# to EBNs
    nest.Connect(LLBN[i], EBN[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': 5.0})
    nest.Connect(E_plus, EBN[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': 1.0})
    nest.Connect(LLBN[k[i]], EBN[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': -10.0})
    nest.Connect(gP, EBN[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': -20.0}) 
# to IBNs
    nest.Connect(EBN[i], IBN[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': 3.0})
# to TNs
    nest.Connect(EBN[i], TN[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': .1})
    nest.Connect(EBN[k[i]], TN[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': -.1})
# to OPN
    nest.Connect(gL[i], OPN, 'all_to_all', {
                'model': 'rate_connection', 'weight': -1.0})

# to output functions
    nest.Connect(LLBN[i], gL[i], 'all_to_all', {
                'model': 'rate_connection', 'weight': 1.0})

# to OPN (cont'd)
nest.Connect(P_plus, OPN, 'all_to_all', {
                'model': 'rate_connection', 'weight': 1.0})
nest.Connect(Ext, OPN, 'all_to_all', {
                'model': 'rate_connection', 'weight': 1.0})

# to output functions (cont'd)
nest.Connect(OPN, gP, 'all_to_all', {
                'model': 'rate_connection', 'weight': 1.0})
nest.Connect(SC, gS, 'all_to_all', {
                'model': 'rate_connection', 'weight': 1.0})
