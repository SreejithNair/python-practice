
'''
Use the LinearRegressor class in TensorFlow to predict median housing price, at the granularity of city blocks, based on one input feature
Evaluate the accuracy of a model's predictions using Root Mean Squared Error (RMSE)
Improve the accuracy of a model by tuning its hyperparameters
'''
import __future__

import math
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.python.data import Dataset
from IPython import display
from matplotlib import cm, gridspec
from matplotlib import pyplot as plt
from sklearn import metrics
from tensorflow.keras import optimizers


pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.2f}'.format

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

'''
We'll randomize the data, just to be sure not to get any pathological ordering effects that might harm the performance of Stochastic Gradient Descent.
Additionally, we'll scale median_house_value to be in units of thousands, so it can be learned a little more easily with learning rates
 in a range that we usually use.
'''
california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0

print(california_housing_dataframe)
print(california_housing_dataframe.describe())

# Define the input feature: total_rooms.
my_feature = california_housing_dataframe[['total_rooms']]
#configure a numeric feature column for total_room
feature_column = [tf.feature_column.numeric_column('total_rooms')]

#define target / label
targets =  california_housing_dataframe['median_house_value']

'''
Next, we'll configure a linear regression model using LinearRegressor. We'll train this model using the GradientDescentOptimizer,
which implements Mini-Batch Stochastic Gradient Descent (SGD). The learning_rate argument controls the size of the gradient step.

To be safe, we also apply gradient clipping to our optimizer via clip_gradients_by_norm. Gradient clipping ensures the magnitude 
of the gradients do not become too large during training, which can cause gradient descent to fail.
'''

# my_optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.0000001)
# my_optimizer = tf.compat.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
sgd = optimizers.SGD(lr=0.0000001, clipvalue=5.0)

linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_column, optimizer=sgd)

def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """Trains a linear regression model of one feature.
  
    Args:
      features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the data.
      num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """
  
    # Convert pandas data into a dict of np arrays.
    features = {key:np.array(value) for key,value in dict(features).items()}                                           
 
    # Construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features,targets)) # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)
    
    # Shuffle the data, if specified.
    if shuffle:
      ds = ds.shuffle(buffer_size=10000)
    
    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

# Create an input function for predictions.
# Note: Since we're making just one prediction for each example, we don't 
# need to repeat or shuffle the data here.
prediction_input_fn =lambda: my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)

# Call predict() on the linear_regressor to make predictions.
predictions = linear_regressor.predict(input_fn=prediction_input_fn)

# Format predictions as a NumPy array, so we can calculate error metrics.
predictions = np.array([item['predictions'][0] for item in predictions])

print()