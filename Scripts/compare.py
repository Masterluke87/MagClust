from util.OrcaComparator import checkStructuresInsideFolder, readXYZandEnergy
import json

X,l = checkStructuresInsideFolder(10)
E = [readXYZandEnergy(f"{i}/pbe.xyz").info["energy"] for i in l]


jsonStr = json.dumps({"SimMat" : X.tolist(),
                     "EnergyOrder" : l,
                     "Energies"  : E},indent = 4, sort_keys=True)

with open("results.json","w") as jsonFile:
    jsonFile.write(jsonStr)               



