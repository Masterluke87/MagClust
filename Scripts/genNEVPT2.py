import json
from tabulate import tabulate
from util.energyReader import readHSLSinOneFolder, getCASSCFEnergies
import os,shutil

if __name__ == "__main__":
    exportData = []
    with open("results.json") as f:
        D = json.load(f)
    for i in D["EnergyOrder"]:
        #os.mkdir(f"{i}/CASSCF/")
        #os.symlink(f"../pbe.xyz",f"{i}/CASSCF/pbe.xyz")
        #os.symlink(f"../pbe.qro",f"{i}/CASSCF/pbe.qro")
        #shutil.copy("../../Au10Fe/Au10Fe_3_0/0/CASSCF/casscf.inp",f"{i}/CASSCF/")
        #shutil.copy("../../Au10Fe/Au10Fe_3_0/0/CASSCF/nevpt2.inp",f"{i}/CASSCF/")
        print(f"cd {i}/CASSCF;ts run_orca_50.x nevpt2.inp;cd ../../;")
    











