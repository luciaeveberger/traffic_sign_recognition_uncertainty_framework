# SCOPE MODELS
Traffic Sign Recognition Framework Code. This framework's objective is to detect and reject points for which they are out of scope. 
# Research Questions : 
(Q1.4) Can potentially relevant scope factor be identified?

(Q1.5) Can required scope factor evaluation results be provided by a scope model?

(Q1.6) Which approach can be used to determine the likelihood of scope compliance?  

# 5_2_1.Scope Model 
The Scope Model is contained in the `ScopeModelValidator` file. 
It is run with the `calculate_scope_probability` script for which the file path can be added for use. In this script, the points are annotated and the final updated dataframe is run. 
The concept drift is also called.  A design diagram is shown below: 

![scope_model](https://github.com/luciaeveberger/tsr_uncertainy_framework/blob/master/design_figures/scope_model.png) 

# 5_2_2 Dataset Sufficiency & Representativeness
Before running the Scope Model, it's important to look at the density of the dataset provided. 
The `Sufficience_Testing` directory has a set of three ipython files which do this. 

1) DataTestSufficieny 
2) DensityValidation 
3) WeatherStatisticalSampling
 
 The diagram below explains the login for this process. 
![data sufficiency](https://github.com/luciaeveberger/tsr_uncertainy_framework/blob/master/design_figures/analyze_representativeness_sufficiency.png)  
 
## Environmental Modules
For the environmental module, there is also the environmental directory which can be used to generate the distributions.  
