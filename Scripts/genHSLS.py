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
			os.mkdir(f"{i}/HSLS/")
			os.symlink(f"../pbe.xyz",f"{i}/HSLS/pbe.xyz")
			shutil.copy("../../Scripts/util/Templates/S_3_5/pbeSP.inp",f"{i}/HSLS/")
			shutil.copy("../../Scripts/util/Templates/S_3_5/b2plyp.inp",f"{i}/HSLS/")
			shutil.copy("../../Scripts/util/Templates/S_3_5/scan.inp",f"{i}/HSLS/")
			print(f"cd {i}/HSLS;ts run_orca_50.x b2plyp.inp;ts run_orca_50.x pbeSP.inp;ts run_orca_50.x scan.inp; cd ../../;")
	if findMultiplicity("0/pbe.out") in [4,6]:
		for i in D["EnergyOrder"]:
			os.mkdir(f"{i}/HSLS/")
			os.symlink(f"../pbe.xyz",f"{i}/HSLS/pbe.xyz")
			shutil.copy("../../Scripts/util/Templates/S_4_6/pbeSP.inp",f"{i}/HSLS/")
			shutil.copy("../../Scripts/util/Templates/S_4_6/b2plyp.inp",f"{i}/HSLS/")
			shutil.copy("../../Scripts/util/Templates/S_4_6/scan.inp",f"{i}/HSLS/")
			print(f"cd {i}/HSLS;ts run_orca_50.x b2plyp.inp;ts run_orca_50.x pbeSP.inp;ts run_orca_50.x scan.inp; cd ../../;")
	
    











