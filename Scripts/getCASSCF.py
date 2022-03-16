import json
from tabulate import tabulate
from util.energyReader import readHSLSinOneFolder

def getCASSCFEnergies(pathFile):
    N  = open(f"./{pathFile}/CASSCF/nevpt2.out").readlines()

    
    c  = [c for c,x in enumerate(N) if "SA-CASSCF TRANSITION ENERGIES" in x ][0]
    CAS = {"E"  : N[c+3].split()[7],
           "C"  : N[c+3].split()[3],
           "M"  : N[c+3].split()[5].replace(")",""),
           "EX" : N[c+6].split()[3]}
    
    c  = [c for c,x in enumerate(N) if "NEVPT2 TRANSITION ENERGIES" in x ][0]
    NEV = {"E"  : N[c+3].split()[7],
           "C"  : N[c+3].split()[3].replace(",",""),
           "M"  : N[c+3].split()[5].replace(")",""),
           "EX" : N[c+6].split()[3]}

    c = [c for c,x in enumerate(N) if "EFFECTIVE HAMILTONIAN SPIN-ORBIT COUPLING CONTRIBUTION" in x][0]

    D      = float([x.split()[2] for x in N[c:c+200] if "D   =" in x][0])
    EoverD = float([x.split()[2] for x in N[c:c+200] if "E/D =" in x][0])

    
    print(f"{pathFile} {CAS['C']} {CAS['M']} {CAS['E']} {CAS['EX']} {NEV['C']} {NEV['M']} {NEV['E']} {NEV['EX']} {D} {EoverD}")


if __name__ == "__main__":
    exportData = []
    with open("results.json") as f:
        D = json.load(f)
    for i in D["EnergyOrder"]:
        getCASSCFEnergies(i)

    print(tabulate([list(x.values()) for x in exportData],headers=list(exportData[0].keys()),tablefmt="grid",floatfmt=".5f"))











