import pandas as pd
import numpy as np
import argparse
import tensorflow as tf
import root_pandas

pd.options.mode.chained_assignment = None  # default='warn'



parser = argparse.ArgumentParser()
parser.add_argument("dataset_in", help="Path to the data.", type=str)
parser.add_argument("dataset_out", help="Path and filename where to save the predctions", type=str)
parser.add_argument("threshold", help="Threshold for the decision.", type=float)
parser.add_argument("drop_0", default=False, help="Should the tuples labeld 0 be dropped.", type=bool)
args = parser.parse_args()

variables = ['clusterAbsZernikeMoment40_1', 'clusterAbsZernikeMoment40_2',
       'clusterAbsZernikeMoment51_1', 'clusterAbsZernikeMoment51_2',
       'clusterErrorTiming_1', 'clusterErrorTiming_2', 'clusterLAT_1',
       'clusterLAT_2', 'clusterTiming_1', 'clusterTiming_2',
       'clusterZernikeMVA_1', 'clusterZernikeMVA_2', 'phi_1', 'phi_2', 'pz_1',
       'pz_2', 'b2bPhi_1', 'b2bPhi_2',
       'cosAngleBetweenMomentumAndVertexVector_1',
       'cosAngleBetweenMomentumAndVertexVector_2',
       'cosAngleBetweenMomentumAndVertexVectorInXYPlane_1',
       'cosAngleBetweenMomentumAndVertexVectorInXYPlane_2', 'pRecoilPhi_1',
       'pRecoilPhi_2', 'pxErr_1', 'pxErr_2', 'pyErr_1', 'pyErr_2', 'pzErr_1',
       'pzErr_2', 'minC2TDist_1', 'minC2TDist_2']

path_to_model = 'final_model_v1.h5'

# Load model
model = tf.keras.models.load_model(path_to_model)

# Load the dataset
def load_dataset(path):
    dataset = root_pandas.read_root(path)
    return dataset

# Only for test !
dataset = load_dataset(args.dataset_in)

# Seperate the variables needed for predictions from the other variables
dataset_other = dataset.drop(variables, axis=1)
dataset_main = dataset[variables]

# Predict the label with the loaded classifier
dataset_main['prediction_continuous'] = model.predict(dataset_main)

# Method to get the label based on the wanted threshold
def predict(x, threshold):
    if x >= threshold:
        return 1
    return 0

# Create the label for every tuple based on the threshold
vfunc = np.vectorize(predict)
dataset_main['prediction'] = vfunc(dataset_main['prediction_continuous'], args.threshold)

# Reconcatenate the dataset
dataset = pd.concat([dataset_main, dataset_other], axis=1)

# If wanted drop only keep the tuples labeled 1
if args.drop_0:
    dataset = dataset.loc[dataset['prediction'] == 1 ]

# Save the result
root_pandas.to_root(dataset, args.dataset_out)
#dataset.to_pickle(args.dataset_out)