from ase.ga.standard_comparators import InteratomicDistanceComparator
from ase.io import read,write
import numpy as np
import sys


class myComp(InteratomicDistanceComparator):
    def __init__(self, n_top=None, pair_cor_cum_diff=0.015,
                 pair_cor_max=0.7, dE=0.02, mic=False):
        InteratomicDistanceComparator.__init__(self,n_top=n_top, pair_cor_cum_diff=pair_cor_cum_diff,
                 pair_cor_max=pair_cor_max, dE=dE, mic=mic)
    def looks_like(self, a1, a2):
        """ Return if structure a1 or a2 are similar or not. """
        if len(a1) != len(a2):
            raise Exception('The two configurations are not the same size')

        # first we check the energy criteria
        dE = abs(a1.info["energy"] - a2.info["energy"])
        if dE >= self.dE:
            return False

        # then we check the structure
        a1top = a1[-self.n_top:]
        a2top = a2[-self.n_top:]
        cum_diff, max_diff = self.__compare_structure__(a1top, a2top)

        return (cum_diff < self.pair_cor_cum_diff
                and max_diff < self.pair_cor_max)

def compareTwoXYZStructures(pathA,pathB):
    A = read(pathA)
    A.info["energy"] = float([x.split()[4] for x in open(pathA.replace("xyz","out")).readlines() if "FINAL SINGLE POINT ENERGY"in x ][-1])

    B = read(pathB)
    B.info["energy"] = float([x.split()[4] for x in open(pathB.replace("xyz","out")).readlines() if "FINAL SINGLE POINT ENERGY"in x ][-1])

    comp = myComp(n_top=len(A),pair_cor_cum_diff=0.015,pair_cor_max=0.7,dE=0.02,mic=False)

    return comp.looks_like(A,B)


def readXYZandEnergy(pathA):
    A = read(pathA)
    A.info["energy"] = float([x.split()[4] for x in open(pathA.replace("xyz","out")).readlines() if "FINAL SINGLE POINT ENERGY"in x ][-1])
    return A



def checkStructuresInsideFolder(nStructures,prefix="pbe"):
    X = np.zeros((nStructures,nStructures))
    unique = [] 
    for i in range(nStructures):
        for j in range(nStructures):
            X[i,j]=compareTwoXYZStructures(f"{i}/{prefix}.xyz",f"{j}/{prefix}.xyz")
            print("{} {} {}".format(i,j, X[i,j]))
    unique = [i for i in range(nStructures) if not (1.0 in X[i,:i])]
    sort = sorted(unique,key=lambda x: readXYZandEnergy(f"{x}/pbe.xyz").info["energy"])
    return X,sort


