## Directory of the Quality Models
To use quality models, a GPU is required.


The Quality Models are 

1.	Annotations Creator `QUALITY_MODELS/DATA_PROCESSING/CreateAnnotations.ipny`: create p files
2.	DeepCNN: `QUALITY_MODELS/DeepCNN.ipynb`: quantifies the strength of the quality effects 
3.	VGGNett: `QUALITY_MODELS/VGGNET.ipynb`: classifies the sign type 
4.	QualityImpactModel: `QUALITY_MODELS/QualityImpactModel.ipynb`: decision tree models the uncertainty relationship
5.	ConfidenceIntervals: `QUALITY_MODELS/GenerateConfidenceIntervals.ipynb` generates confidence intervals for model accuracy as well as per node or leaf
6. Model Predictions: Template file for making randomized predictions from H files `ModelPredictions.ipynb`.


### DEEP CNN: 
1.	Input data is the quality factor of choice 
2.	The original data is kept in the data_output/TSD/p_files
3.	The mixed effects are kept in the data_output/TSD/mixed_p_files * feel free to add more permutations if desired
The p-files are dictionaries which contain the data required for the DeepCNN and VGNETT. 
The keys included are {"data":[], "labels":[], "quality_data_label": []}
The script will set the labels. 

### VGGNett CNN: 
1.	Boiler-plate VGGNett with some modifications
2.	The final validation finals can be used on a trained model
3.	P files are also used as input data 

### Quality Impact Model:
1.	Uses the annotated p file from the VGNett. Can be easily swamped for other training data.
2.	Different approaches are contained in the script (random forest, etc)
3.	Requires a GPU for the random forest traini

