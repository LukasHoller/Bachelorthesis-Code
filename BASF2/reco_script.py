from basf2 import *
from modularAnalysis import * 
from stdV0s import stdKshorts
from variables import variables
import pdg
import os.path
import sys
from vertex import *
from reconstruction import *
from ROOT import Belle2
from glob import glob
from stdPi0s import *
from stdPhotons import *
from basf2 import use_central_database
import variables
from variables import variables as v
import basf2_mva
from reco_variables import *
import argparse
import numpy as np

# TODO check if all imports are needed

# User sets files (format) for loading and saving the data
parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="Total path to input file.", type=str)
parser.add_argument("ntuple", help="Total path to output file.", type=str)
args = parser.parse_args()

set_log_level(LogLevel.ERROR)

# Iterate over all runs
for i in np.arange(1,101,1):
    print('\n', '='*30, '\n', 'RUN ', str(i), '\n', '='*30, '\n' , sep='')

    # Create path
    xxx = create_path()

    # Set current filename
    filename = args.inputfile + '' + str(i) + '.root'

    # Load data
    inputMdst("default", filename, path=xxx)

    # Load all measured photons
    fillParticleLists([('gamma:all', '')], path=xxx)

    # Compare all photons with the true photons from the MC simulation
    matchMCTruth('gamma:all', path=xxx)

    # Reconstruct the pi0 -> gamma gamma decay
    reconstructDecay('pi0:pi0 -> gamma:all gamma:all', '', path=xxx)
    matchMCTruth('pi0:pi0', path=xxx)

    # Save the reconstructed pi0's 
    variablesToNtuple('pi0:pi0', var_mother + var_pi0 + ['p', 'dM', 'isSignal', 'daughter(0, mdstSource)', 'daughter(1, mdstSource)'], filename=args.ntuple + '_' + str(i) + "_pi0.root", path=xxx)

    # Register module to plot the progress of the reconstruction
    progress = register_module('Progress')
    xxx.add_module(progress)

    # Process the modules
    process(xxx)

    # Print out the summary
    print(statistics)

