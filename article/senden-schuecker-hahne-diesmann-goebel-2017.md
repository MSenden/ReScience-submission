---
Title: "A neural model of the saccade generator in the reticular formation"
Author:
  - name: Mario Senden
    affiliation: 1, 2
  - name: Jannis Schuecker,
    affiliation: 3
  - name: Jan Hahne,
    affiliation: 4
  - name: Markus Diesmann,
    affiliation: 3, 5, 6
  - name: Rainer Goebel,
    affiliation: 1, 2, 7
Address:
  - code:    1
    address: Department of Cognitive Neuroscience, Faculty of Psychology and Neuroscience,
			Maastricht University, 6201BC Maastricht, The Netherlands
  - code:    2
    address: Maastricht Brain Imaging Centre, Faculty of Psychology and Neuroscience, 
			Maastricht University, P.O. Box 616, 6200 MD Maastricht, The Netherlands
  - code:    3
    address: Institute of Neuroscience and Medicine (INM-6) and Institute for Advanced Simulation (IAS-6) 
             and JARA BRAIN Institute I, Jülich Research Centre, 52428 Jülich, Germany
  - code:    4
    address: School of Mathematics and Natural Sciences, Bergische Universit\"at Wuppertal,
			Wuppertal, Germany
  - code:    5
    address: Department of Psychiatry, Psychotherapy and Psychosomatics, Medical Faculty, 
             RWTH Aachen University, 52062 Aachen, Germany
  - code:    6
    address: Department of Physics, Faculty 1, RWTH Aachen University, 52062 Aachen, Germany
  - code:    7
    address: Department of Neuroimaging and Neuromodeling, Netherlands Institute for Neuroscience, 
			an Institute of the Royal Netherlands Academy of Arts and Sciences (KNAW), 1105BA Amsterdam, The Netherlands
Contact:
  - mario.senden@maastrichtuniversity.nl
Editor:
  - Name Surname
Reviewer:
  - Name Surname
  - Name Surname
Publication:
  received:  Month,  Day, 2017
  accepted:  Month, Day, 2017
  published: Month, Day, 2017
  volume:    "**1**"
  issue:     "**1**"
  date:      Month 2017
Repository:
  article:   "http://github.com/rescience/rescience-submission/article"
  code:      "http://github.com/rescience/rescience-submission/code"
  data:
  notebook:
Reproduction:
  - "*A neural model of the saccade generator in the reticular formation*, G. Gancarz,
	S. Grossberg, Neural Networks, 1159-1174, 1998"
Bibliography:
  bibliography.bib

---

# Introduction

We provide an implementation of the saccade generator (SG); a rate neuron model of the neural circuitry in the reticular formation proposed by Gancarz & Grossberg [@Gancarz1998]. The same group has recently sucessfully embedded the SG into a larger model of the eye movement network [@Grossberg2012] showcasing its compatible nature. This compatibility of the SG model might prove useful in the future for studying the interplay of neural (sub)systems of visuo-motor integration. It is thus of interest to implement the model in publicly available, widely used, and actively developed neural simulation frameworks such as NEST [@Gewaltig2007]. We show that the model translates well to the NEST framework as our implementation faithfully reproduces most simulation results reported in the original publication. Our code uses the Python interface [@Eppler2008] for legibility with both model and analysis scripts being implemented using Python 2.7.12.

# Methods

The SG model described by Gancarz & Grossberg [@Gancarz1998] consists of a horizontal and a vertical component with two long-lead burst neurons (LLBNs), excitatory burst neurons (EBNs), inhibitory burst neurons (IBNs), and tonic neurons (TNs) in each. Within each component, the two directions (left-right, up-down) interact antagonistically. Additionally, both components share a single omnipause neuron (OPN) which tonically inhibits each EBN as long as no saccade is being initiated.
In implementing this model, we largely follow the descriptions provided in the original publication with a number of well-motivated exceptions. First, in the original description, neuron activations are bounded from below at zero resulting in their rectification at every step in the numerical integration. Since this effectively alters neuron dynamics from their original description, we refrained from this practice. Instead, input received by each neuron from other neurons was passed through a rectified linear gain function before summation. This assured that neuron dynamics accorded with their description. Second, the gain function 
$$ g(x) = {\frac{x^4}{0.1^4+x^4}} $$ {#eq:1}
(equation A11) in the original publication was replaced by
$$ g(x) = {\frac{1}{e^{-40(x-0.1)}}} $$ {#eq:2}
to prevent positive responses to negative net input but otherwise preserve the shape of the curve for $\mathrm{x>0}$. Third, according to equation A12 in the original publication horizontal eye position $\theta$ is given by $\mathrm{\theta=260({TN}_{r}-0.5)}$. However, activation of TNs is 0 rather than 0.5 when the eye is at the center of its range and a factor of 260 produces saccades of excessively high amplitudes. We found a factor of 150 to reproduce original simulations better. Finally, the original implementation uses the fourth order Runge–Kutta method for numerical integration. Instead, we used the Exponential Euler method which is standardly implemented in NEST for the numerical integration of rate neurons [@Hahne2016].

In addition to these changes, the original model description has two features which cannot be straightforwardly translated to NEST. First, whether a nonlinear gain function is applied to a neuron's input can depend on the origin of said input. This is notably the case for EBNs and the OPN. Since NEST only applies a single gain function per neuron to each of its input, we opted for using a linear gain function for EBNs and the OPN and to pass those inputs requiring an additional nonlinear gain function through an auxiliary unit instantaneously applying the desired nonlinearity. Second, constant input to a neuron was provided by an appropriately weighted bias node.

# Results

In the remainder we present the results of our simulations for all nine experiments reported in the original publication. While our results generally accord very well with those of Gancarz & Grossberg [@Gancarz1998], some simulations required slightly divergent parameter values to reproduce original results.

## 1) Saccadic staircase simulation

The first simulation reported by Gancarz & Grossberg [@Gancarz1998] showcases the evolution of activity for each neuron type in the horizontal SG to a constant input ($\mathrm{I=1}$) applied to the left long-lead burst neuron (LLBN) for $265\,\mathrm{ms}$.


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig3.eps){#fig:fig_1}


## Cell activity profiles in the reticular formation

blubber


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig5.eps){#fig:fig_2 height="8.5cm" width="6.375cm" align="left"}


## Visually guided saccades

Bli Bla Blub


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig6.eps){#fig:fig_3 height="8.5cm" width="8.5cm"}


## Oblique staircase simulation

Bli Bla Blub


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig7.eps){#fig:fig_4 height="11.6cm" width="8.5cm"}


## Tuning curve of excitatory burst neuron (EBN)

Bli Bla Blub


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig8.eps){#fig:fig_5
height="8.5cm" width="8.5cm"}


## Effects of frequency of external stimulation

Bli Bla Blub


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig9.eps){#fig:fig_6 height="5.0cm" width="11.6cm"}


## Trading saccade velocity and duration

Bli Bla Blub


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig10.eps){#fig:fig_7
height="11.6cm" width="8.5cm"}


## Smooth staircase simulation

Bli Bla Blub


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig11.eps){#fig:fig_8
height="11.6cm" width="8.5cm"}


## Interrupted saccade simulation

Bli Bla Blub


![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig12.eps){#fig:fig_9 height="11.6cm" width="8.5cm"}


# Conclusion

Conclusion, at the very minimum, should indicate very clearly if you were able
to replicate original results. If it was not possible but you found the reason
why (error in the original results), you should exlain it.


Heading 1                          Heading 2
---------- ----------- ----------- ----------- ----------- -----------
cell1 row1 cell2 row 1 cell3 row 1 cell4 row 1 cell5 row 1 cell6 row 1
cell1 row2 cell2 row 2 cell3 row 2 cell4 row 2 cell5 row 2 cell6 row 2
cell1 row3 cell2 row 3 cell3 row 3 cell4 row 3 cell5 row 3 cell6 row 3
---------- ----------- ----------- ----------- ----------- -----------

Table: Table caption {#tbl:table}

A reference to table @tbl:table.
A reference to figure @fig:logo.
A reference to equation @eq:1.
A reference to citation @markdown.

![Figure caption](rescience-logo.pdf){#fig:logo}

$$ A = \sqrt{\frac{B}{C}} $$ {#eq:1}

# Acknowledgments 
All network simulations carried out with NEST (http://www.nest-simulator.org).

# References

