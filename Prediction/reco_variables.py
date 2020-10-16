import variables

# Variables needed for prediction

variables.variables.addAlias('clusterAbsZernikeMoment40_1', 'daughter(0, clusterAbsZernikeMoment40)')
variables.variables.addAlias('clusterAbsZernikeMoment40_2', 'daughter(1, clusterAbsZernikeMoment40)')

variables.variables.addAlias('clusterAbsZernikeMoment51_1', 'daughter(0, clusterAbsZernikeMoment51)')
variables.variables.addAlias('clusterAbsZernikeMoment51_2', 'daughter(1, clusterAbsZernikeMoment51)')

variables.variables.addAlias('clusterTiming_1', 'daughter(0, clusterTiming)')
variables.variables.addAlias('clusterTiming_2', 'daughter(1, clusterTiming)')

variables.variables.addAlias('clusterErrorTiming_1', 'daughter(0, clusterErrorTiming)')
variables.variables.addAlias('clusterErrorTiming_2', 'daughter(1, clusterErrorTiming)')

variables.variables.addAlias('clusterLAT_1', 'daughter(0, clusterLAT)')
variables.variables.addAlias('clusterLAT_2', 'daughter(1, clusterLAT)')

variables.variables.addAlias('clusterZernikeMVA_1', 'daughter(0, clusterZernikeMVA)')
variables.variables.addAlias('clusterZernikeMVA_2', 'daughter(1, clusterZernikeMVA)')

variables.variables.addAlias('phi_1', 'daughter(0, phi)')
variables.variables.addAlias('phi_2', 'daughter(1, phi)')

variables.variables.addAlias('b2bPhi_1', 'daughter(0, b2bPhi)')
variables.variables.addAlias('b2bPhi_2', 'daughter(1, b2bPhi)')

variables.variables.addAlias('pRecoilPhi_1', 'daughter(0, pRecoilPhi)')
variables.variables.addAlias('pRecoilPhi_2', 'daughter(1, pRecoilPhi)')

variables.variables.addAlias('cosAngleBetweenMomentumAndVertexVector_1', 'daughter(0, cosAngleBetweenMomentumAndVertexVector)')
variables.variables.addAlias('cosAngleBetweenMomentumAndVertexVector_2', 'daughter(1, cosAngleBetweenMomentumAndVertexVector)')

variables.variables.addAlias('cosAngleBetweenMomentumAndVertexVectorInXYPlane_1', 'daughter(0, cosAngleBetweenMomentumAndVertexVectorInXYPlane)')
variables.variables.addAlias('cosAngleBetweenMomentumAndVertexVectorInXYPlane_2', 'daughter(1, cosAngleBetweenMomentumAndVertexVectorInXYPlane)')

variables.variables.addAlias('pz_1', 'daughter(0, pz)')
variables.variables.addAlias('pz_2', 'daughter(1, pz)')

variables.variables.addAlias('pxErr_1', 'daughter(0, pxErr)')
variables.variables.addAlias('pxErr_2', 'daughter(1, pxErr)')

variables.variables.addAlias('pyErr_1', 'daughter(0, pyErr)')
variables.variables.addAlias('pyErr_2', 'daughter(1, pyErr)')

variables.variables.addAlias('pzErr_1', 'daughter(0, pzErr)')
variables.variables.addAlias('pzErr_2', 'daughter(1, pzErr)')

variables.variables.addAlias('minC2TDist_1', 'daughter(0, minC2TDist)')
variables.variables.addAlias('minC2TDist_2', 'daughter(1, minC2TDist)')


var_pi0 = ['clusterAbsZernikeMoment40_1', 'clusterAbsZernikeMoment40_2', 'clusterAbsZernikeMoment51_1', 'clusterAbsZernikeMoment51_2', 'clusterErrorTiming_1', 'clusterErrorTiming_2', 'clusterLAT_1', 'clusterLAT_2', 'clusterTiming_1', 'clusterTiming_2', 'clusterZernikeMVA_1', 'clusterZernikeMVA_2', 'phi_1', 'phi_2', 'pz_1', 'pz_2', 'b2bPhi_1', 'b2bPhi_2', 'cosAngleBetweenMomentumAndVertexVector_1', 'cosAngleBetweenMomentumAndVertexVector_2', 'cosAngleBetweenMomentumAndVertexVectorInXYPlane_1', 'cosAngleBetweenMomentumAndVertexVectorInXYPlane_2', 'pRecoilPhi_1', 'pRecoilPhi_2', 'pxErr_1', 'pxErr_2', 'pyErr_1', 'pyErr_2', 'pzErr_1', 'pzErr_2', 'minC2TDist_1', 'minC2TDist_2']
