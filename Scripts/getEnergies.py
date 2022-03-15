import json
from tabulate import tabulate
from util.energyReader import readHSLSinOneFolder

if __name__ == "__main__":
    exportData = []
    with open("results.json") as f:
        D = json.load(f)
    for i in D["EnergyOrder"]:
        exportData.append(readHSLSinOneFolder(str(i)))

    print(tabulate([list(x.values()) for x in exportData],headers=list(exportData[0].keys()),tablefmt="grid",floatfmt=".5f"))











