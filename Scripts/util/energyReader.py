
def readMultEnergy(filename):
    """
    This will read a two-step job output file; High spin first, low spin second
    """
    M = [int(x.split()[-1]) for x in open(filename).readlines() if "Multiplicity" in x]
    E = [float(x.split()[-1]) for x in open(filename).readlines() if "FINAL SINGLE" in x]

    return {M[0] : E[0], M[1] : E[1]}

def getCASSCFEnergies(pathFile):
    N  = open(f"./{pathFile}/CASSCF/nevpt2.out").readlines()

    print(f"./{pathFile}/CASSCF/nevpt2.out")
    c  = [c for c,x in enumerate(N) if "SA-CASSCF TRANSITION ENERGIES" in x ][0]
    Data = {"ID"     : pathFile,
            "CAS-E"  : float(N[c+3].split()[7]),
            "CAS-C"  : N[c+3].split()[3],
            "CAS-M"  : N[c+3].split()[5].replace(")",""),
            "CAS-EX" : float(N[c+6].split()[3])}
    c  = [c for c,x in enumerate(N) if "NEVPT2 TRANSITION ENERGIES" in x ][0]
    Data["NEV-E"]     =  N[c+3].split()[7]
    Data["CAS-ROOT"]  =  N[c+3].split()[3].replace(",","")
    Data["NEV-M"]     =  N[c+3].split()[5].replace(")","")
    Data["NEV-EX"]    =  float(N[c+6].split()[3])
    c = [c for c,x in enumerate(N) if "EFFECTIVE HAMILTONIAN SPIN-ORBIT COUPLING CONTRIBUTION" in x][0]
    Data["D"]      = float([x.split()[2] for x in N[c:c+200] if "D   =" in x][0])
    Data["EoverD"] = float([x.split()[2] for x in N[c:c+200] if "E/D =" in x][0])

    return Data


def readHSLSinOneFolder(pathNumber):
    b2plyp = []
    pbeSP  = []
    scan   = [] 

    opt = (int([x.split()[-1] for x in open(f"{pathNumber}/pbe.out").readlines() if "Multiplicity" in x][-1]),
           float([x.split()[-1] for x in open(f"{pathNumber}/pbe.out").readlines() if "FINAL SINGLE" in x][-1]))

    #print("Optimization was done for:")
    #print(f"Mult  : {opt[0]}")
    #print(f"Ener  : {opt[1]}")

    b2plyp = readMultEnergy(f"{pathNumber}/HSLS/b2plyp.out")
    pbeSP  = readMultEnergy(f"{pathNumber}/HSLS/pbeSP.out")
    scan   = readMultEnergy(f"{pathNumber}/HSLS/scan.out")

    #print(f"B2PLYP: {b2plyp}")
    #print(f"PBE   : {pbeSP} ")
    #print(f"SCAN  : {scan}  ")

    badCounter  = 0
    goodCounter = 0 

    for i,s in zip([b2plyp,pbeSP,scan],["B2PLYP","PBE","SCAN"]):
        """
        K - is the key of the other 
        """
        K = list(i.keys() - [opt[0]])[0]
        if i[opt[0]] < i[K]:
            #print(f"{s} predicts mult {opt[0]} to be more stable than {K}, good news")
            goodCounter += 1
        else:
            #print(f"{s} predicts mult {K} to be more stable than {opt[0]}, bad news ")
            badCounter += 1
    """
    if badCounter > goodCounter:
        print("This candidate can be sorted out!")
    else:
        print("This is a promising candidate")
    """
    return {"ID"      : pathNumber,
            "OPT-M"   : opt[0],
            "PBE-OPT" : opt[1],
            f"PBE-{list(pbeSP.items())[0][0]}" : list(pbeSP.items())[0][1],
            f"PBE-{list(pbeSP.items())[1][0]}" : list(pbeSP.items())[1][1],
            f"B2PLYP-{list(b2plyp.items())[0][0]}" : list(b2plyp.items())[0][1],
            f"B2PLYP-{list(b2plyp.items())[1][0]}" : list(b2plyp.items())[1][1],
            f"SCAN-{list(scan.items())[0][0]}" : list(scan.items())[0][1],
            f"SCAN-{list(scan.items())[1][0]}" : list(scan.items())[1][1]}









