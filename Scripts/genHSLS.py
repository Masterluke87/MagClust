import json
from tabulate import tabulate
from util.energyReader import readHSLSinOneFolder, getCASSCFEnergies
import os,shutil

if __name__ == "__main__":
    exportData = []
    with open("results.json") as f:
        D = json.load(f)
    for i in D["EnergyOrder"]:
        os.mkdir(f"{i}/HSLS/")
        os.symlink(f"../pbe.xyz",f"{i}/HSLS/pbe.xyz")
        shutil.copy("../../Au10Fe/Au10Fe_3_0/0/HSLS/pbeSP.inp",f"{i}/HSLS/")
        shutil.copy("../../Au10Fe/Au10Fe_3_0/0/HSLS/b2plyp.inp",f"{i}/HSLS/")
        shutil.copy("../../Au10Fe/Au10Fe_3_0/0/HSLS/scan.inp",f"{i}/HSLS/")
        print(f"cd {i}/HSLS;ts run_orca_50.x b2plyp.inp;ts run_orca_50.x pbeSP.inp;ts run_orca_50.x scan.inp; cd ../../;")
    











