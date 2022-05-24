import json
from tabulate import tabulate
from util.energyReader import readHSLSinOneFolder, getCASSCFEnergies
import os,shutil

def findMultiplicity(fileName):
	return [int(x.split("....")[1]) for x in  open(fileName).readlines() if "Multiplicity" in x][0]

if __name__ == "__main__":
    exportData = []
    with open("results.json") as f:
        D = json.load(f)
        if findMultiplicity("0/pbe.out") in [3,5]:
            for i in D["EnergyOrder"]:
                os.mkdir(f"{i}/CASSCF/")
                os.symlink(f"../pbe.xyz",f"{i}/CASSCF/pbe.xyz")
                os.symlink(f"../pbe.qro",f"{i}/CASSCF/pbe.qro")
                shutil.copy("../../Scripts/util/Templates/S_3_5/casscf.inp",f"{i}/CASSCF/")
                shutil.copy("../../Scripts/util/Templates/S_3_5/nevpt2.inp",f"{i}/CASSCF/")
                print(f"cd {i}/CASSCF;ts run_orca_50.x casscf.inp;cd ../../;")
    
        if findMultiplicity("0/pbe.out") in [4,6]:
            for i in D["EnergyOrder"]:
                os.mkdir(f"{i}/CASSCF/")
                os.symlink(f"../pbe.xyz",f"{i}/CASSCF/pbe.xyz")
                os.symlink(f"../pbe.qro",f"{i}/CASSCF/pbe.qro")
                shutil.copy("../../Scripts/util/Templates/S_4_6/casscf.inp",f"{i}/CASSCF/")
                shutil.copy("../../Scripts/util/Templates/S_4_6/nevpt2.inp",f"{i}/CASSCF/")
                print(f"cd {i}/CASSCF;ts run_orca_50.x casscf.inp;cd ../../;")
    











