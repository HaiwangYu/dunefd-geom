import numpy as np
import pandas as pd
import sys, os
from collections import defaultdict
ifile = sys.argv[1]
ofile = sys.argv[2]
crmdb = defaultdict(list)
with open(ifile) as fp:
    for line in fp.readlines():
        if line.startswith("#"):
            continue
        line = line.strip()
        if not line:
            continue
        chunks = line.split()
        ch, crm, plane = [int(x) for x in chunks[:3]]
        key = int( 2*crm+plane )
        crmdb[key].append(chunks)
ofp = open(ofile, 'w')
ofp.write("# channel   tpc plane   wire    sx  sy  sz  ex  ey  ez\n")
ch=0;
for crm in range(36):
    for plane in range(3):
        newplane=plane+1
        if plane>0:
            key = 2*crm+(plane-1)
        else:
            key = 2*crm
        chunks_array = crmdb[key]
        for chunks in chunks_array:
            line = "%d\t%d\t%d\t" % ( ch, crm, plane )
            line += "\t".join(chunks[3:])
            ofp.write(line+"\n")
            ch += 1
ofp.close()
