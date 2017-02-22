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

We provide an implementation of the saccade generator (GM) model of the neural circuitry in the reticular formation
underlying saccadic eye movements proposed by Gancarz & Grossberg [@Gancarz1998]. The model forms part of 
(e.g. is it an important paper in the domain ?). The original implementation is not publicly available. T
he implementation we propose is coded in the NEST [@Gewaltig2007] framework, one of the modern actively developed simulation platforms that
is publicly available. The code uses the Python interface [@Eppler2008] for legibility. The model
and analysis scripts are implemented using Python 2.7.12.

# Methods

The methods section should explain how you replicated the original results:

* did you use paper description
* did you contact authors ?
* did you use original sources ?
* did you modify some parts ?
* etc.

If relevevant in your domain, you should also provide a new standardized
description of the work.


# Results
Results should be compared with original results and you have to explain why
you think they are the same or why they may differ (qualitative result vs
quantitative result). Note that it is not necessary to redo all the original
analysis of the results.

## Saccadic staircase simulation
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig3.eps){#fig:fig_1 height="8.5cm" width="11.6cm"}

## Cell activity profiles in the reticular formation
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig5.eps){#fig:fig_2 height="11.6cm" width="8.5cm"}

## Visually guided saccades
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig6.eps){#fig:fig_3}

## Oblique staircase simulation
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig7.eps){#fig:fig_4}

## Tuning curve of excitatory burst neuron (EBN)
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig8.eps){#fig:fig_5}

## Effects of frequency of external stimulation
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig9.eps){#fig:fig_6}

## Trading saccade velocity and duration
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig10.eps){#fig:fig_7}

## Smooth staircase simulation
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig11.eps){#fig:fig_8}

## Interrupted saccade simulation
Bli Bla Blub

![**Figure caption for part (A) and part (B) .** 
Description of stuff happening  in the original implementation of Gancarz & Grossberg [@Gancarz1998].](../code/fig12.eps){#fig:fig_9}

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

