# SCOPE MODELS
Traffic Sign Recognition Framework Code. This framework's objective is to detect and reject points for which they are out of scope. 
# Research Questions : 
(Q1.4) Can potentially relevant scope factor be identified?

(Q1.5) Can required scope factor evaluation results be provided by a scope model?

(Q1.6) Which approach can be used to determine the likelihood of scope compliance?  

# Scope Model 
The Scope Model is contained in the `ScopeModelValidator` file. 
It is run with the `calculate_scope_probability` script for which the file path can be added for use. In this script, the points are annotated and the final updated dataframe is run. 
The concept drift is also called.  The Scope Model is composed of several objects which are Environmental, ImageBased and Geographical.

# Dataset Sufficiency & Representativeness
Before running the Scope Model, it's important to look at the density of the dataset provided. 
The `Sufficience_Testing` directory has a set of three ipython files which do this. 

1) DataTestSufficieny: checks the parameters of the input dataset
2) DensityValidation: checks the coordinates are with in density parameters
3) WeatherStatisticalSampling: checks the statistical profile of the air temp. and precipiation which is used by the Scope Model.
 
 The data required for this is the `UC1_Testset_Germany/contextInfo.csv` which is provided by Lisa Joekel. 
 The data for the weatherStatistical sampling is https://drive.google.com/open?id=1jmzApLxrFp7q78ZiWYfgvZXEE5jfRmXe. Feel free to download. It is a composition of opensource precipitation and air temperature data across Germany.
