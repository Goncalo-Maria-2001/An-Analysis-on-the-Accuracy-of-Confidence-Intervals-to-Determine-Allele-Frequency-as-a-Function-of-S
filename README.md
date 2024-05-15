# Code used in the An analysis on the accuracy of confidence intervals to determine allele frequency as a function of sample size poster
In this repository you can find the python code used to obtain the graphs shown in the poster:

The Data_Gen_random_p_1_80.py and Data_gen_deviation_1_45.py files were used to generate the margins of error for alpha = 0,05 for each n from 1 to 80 and 1 to 45 respectively, additionally Data_Gen_random_p_1_80.py was used for the simulatioons where p is random and Data_gen_deviation_1_45.py was used in the cases where p = 1/4 + d for d in [-n/10, n/10]. These scripts were translated from the R code provided by T. Fung and K. Keenan.

Group_and_mean_MoE.py was used to determine the mean margins of error for each n sample size.

Graph_MoE_random_p_1_80.py and Graph_MoE_Deviation_1_45.py were used to plot the graphs for the case where p is random and p = 1/4 + d respectively.

In the case of the proportion confidence intervals only two .py files were used: 
Proportion_Intervals_MoE_p_deviation.py and Proportion_Intervals_MoE_random_p.py these scripts do all the above processes for the case where p = 1/4 + d and p is random respectively.

Adittionally Typesetter_array.py was used in the cases where the outputs of the data generating scripts were not arrays.
