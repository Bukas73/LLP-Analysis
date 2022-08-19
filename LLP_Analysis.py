import uproot
import random
import awkward as ak
#from uproot_methods import TLorentzVectorArray
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys, os
from scipy import constants
import math
from math import pi
import pickle

noBIBFile = uproot.open(f"LLP_full.root")
noBIBTree = noBIBFile["LCTupleDefault"]

fullBIBFile = uproot.open("lctuple_2992_trackerSimHits.root")
fullBIBTree =  fullBIBFile["MyLCTuple"]

MCPHits = noBIBTree["stmcp"].array()
MCPDG = noBIBTree["mcpdg"].array()
MCParent = noBIBTree["mcpa0"].array()
MCvtx = noBIBTree["mcvtx"].array()
MCvty = noBIBTree["mcvty"].array()
MCvtz = noBIBTree["mcvtz"].array()

#Boolean filter for whether we are interested in certain tracks
BoolFilter = ak.ArrayBuilder()
print("Begin Building Bool Filter")
for eventNum, event in enumerate(MCPDG):
    BoolFilter.begin_list()
    for partNum, particle in enumerate(event):

        pdg = MCPDG[eventNum][partNum]

        parentInd = MCParent[eventNum][partNum]
        parentpdg = MCPDG[eventNum][parentInd]

        if  (partNum in MCPHits[eventNum]) and \
            (pdg == 11 or pdg == -11 or pdg == 13 or pdg == -13) and \
            (parentpdg == 35):
            
                BoolFilter.append(True)
                
        else:
            BoolFilter.append(False)

    BoolFilter.end_list()

print("End Building Bool Filter")

print(ak.count(MCPDG))
MCPDG = MCPDG[BoolFilter]
print(ak.count(MCPDG))
