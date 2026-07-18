import numpy
import pandas
import rdkit
import prolif
import pymol
import MDAnalysis

from rdkit import Chem

print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("RDKit:", Chem.rdBase.rdkitVersion)
print("ProLIF:", prolif.__version__)
print("MDAnalysis:", MDAnalysis.__version__)
print("PyMOL: OK")
