import basf2 as b2
import generators as ge
import modularAnalysis as ma

# Generation of 100 events according to the specified DECAY table

# Defining custom path
my_path = b2.create_path()

# Setting up number of events to generate
ma.setupEventInfo(noEvents=1000000, path=my_path)

# Adding genberator
ge.add_evtgen_generator(path=my_path,
                        finalstate='signal',
                        signaldecfile=b2.find_file(
                            '../decay_file/decay.dec'))

# If the simulation and reconstruction is not performed in the sam job,
# then the Gearbox needs to be loaded with the loadGearbox() function.
ma.loadGearbox(path=my_path)

# Dump generated events as a ROOT file in the mDST format
my_path.add_module('RootOutput', outputFileName='test.root')

# Process all modules added to the path
b2.process(path=my_path)

# Print out the summary
print(b2.statistics)
