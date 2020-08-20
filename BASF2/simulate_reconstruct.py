import basf2 as b2
import mdst as mdst
import simulation as si
import reconstruction as re
import modularAnalysis as ma


# Use curently best values for the reconstruction
b2.conditions.disable_globaltag_replay()

# Create path
my_path = b2.create_path()

# Load input ROOT file
ma.inputMdst(environmentType='default', filename='', path=my_path)

# Simulation
si.add_simulation(path=my_path)

# Reconstruction
re.add_reconstruction(path=my_path)

# Dump in MDST format
mdst.add_mdst_output(path=my_path,
                     mc=True)

# Show progress of processing
progress = b2.register_module('ProgressBar')
my_path.add_module(progress)

# Process the events
b2.process(my_path)

# Print out the summary
print(b2.statistics)
