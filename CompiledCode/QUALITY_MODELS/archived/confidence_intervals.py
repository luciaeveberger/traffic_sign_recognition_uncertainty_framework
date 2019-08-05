import numpy
import numpy as np
import pandas as pd
from sklearn.utils import resample
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from matplotlib import pyplot
import pickle
import ast
import seaborn as sns
import os

root_directory = os.path.dirname(os.getcwd())

def generate_ds_from_p_file(pickle_file_path):
    with open (pickle_file_path, mode='rb') as f:
        annotated_data = pickle.load(f)
    X = np.array(list(zip(
        annotated_data['BACKLIGHT'],
        annotated_data['DARKNESS'],
        annotated_data['DIRTLENS'],
        annotated_data['MOTIONBLUR'],
        annotated_data['RAIN'],
        annotated_data['VGG_is_correct']
    )))
    print(X[0])

    return X

pickle_file = root_directory + "/TSD/validation_p_files/VALIDATION_ANNOTATED.p"
values = generate_ds_from_p_file(pickle_file)
print(values.shape)
# configure bootstrap
n_iterations = 1000
n_size = int(len(values) * 0.70)
# run bootstrap

def create_bootstrap_per_class(testing_class, graph=False):
    stats = list()
    for i in range(n_iterations):
        # prepare train and test sets
        train = resample(values, n_samples=n_size)
        test = resample(values, n_samples=3500)
        # fit model
        model = DecisionTreeClassifier("entropy", max_features=None,
                                       max_leaf_nodes=10,
                                       min_samples_leaf=15,
                                       min_samples_split=2, min_weight_fraction_leaf=0.0,
                                       presort=False, random_state=None)
        model.fit(train[:,:-1], train[:,-1])
        # evaluate model
        predictions = model.predict(test[:,:-1])
        score = accuracy_score(test[:,-1], predictions)
        #none_score = model.predict_proba([testing_class])
        #stats.append(numpy.amax(none_score))
        stats.append(score)
        #print(none_score)

    #plot scores
    if graph:
        sns.distplot(stats, hist=True, kde=True,
                     bins=int(180/5), color = 'darkblue',
                     hist_kws={'edgecolor':'black'},
                     kde_kws={'linewidth': 4})

        pyplot.show()
        #sns.show()
    alpha = 0.95
    p = ((1.0-alpha)/2.0) * 100
    lower = max(0.0, numpy.percentile(stats, p))
    p = (alpha+((1.0-alpha)/1.0)) * 100
    upper = min(1.0, numpy.percentile(stats, p))
    print('%.1f confidence interval %.1f%% and %.1f%%' % (alpha*100, lower*100, upper*100))
    return lower*100

create_bootstrap_per_class(None, True)


# ## for all nones
# look_up_dict = pd.read_csv(root_directory + "TSD/lookup_dict.csv")
# print(look_up_dict.columns)
# lower_bounds_all = list()
# # converts this to
# look_up_dict['Value'] = look_up_dict['Value'].apply(ast.literal_eval)
# count = 0
# for row in look_up_dict['Value']:
#     lower_bound = create_bootstrap_per_class(row)
#     lower_bounds_all.append(lower_bound)
#     count = count + 1
#     print(count)
# look_up_dict['lower_bounds'] = lower_bounds_all
# look_up_dict.to_csv(root_directory + "TSD/confidence_intervals1.csv")
