#!/bin/bash
python ../ClusterGen/GenAndMutate.py -F Au14Fe -m 5 -c 0 -db Au14Fe_5_0.db -p 20 -l 15.0
python ../ClusterGen/GenAndMutate.py -F Au14Fe -m 3 -c 0 -db Au14Fe_3_0.db -p 20 -l 15.0

python ../ClusterGen/GenAndMutate.py -F Au15Fe -m 6 -c 0 -db Au15Fe_6_0.db -p 20 -l 15.0
python ../ClusterGen/GenAndMutate.py -F Au15Fe -m 4 -c 0 -db Au15Fe_4_0.db -p 20 -l 15.0

python ../ClusterGen/GenAndMutate.py -F Au16Fe -m 5 -c 0 -db Au16Fe_5_0.db -p 20 -l 15.0
python ../ClusterGen/GenAndMutate.py -F Au16Fe -m 3 -c 0 -db Au16Fe_3_0.db -p 20 -l 15.0

