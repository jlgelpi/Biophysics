#! /usr/bin/python3

""" Example to remove selected chains and save the resulting structure in a PDB file """

from Bio.PDB.PDBIO import PDBIO
from Bio.PDB.PDBParser import PDBParser

parser = PDBParser()

st = parser.get_structure('6AXG', '6axg.pdb')

print (len(st[0]), " chains found")

for ch in st[0]:
    print (ch.id)

# More compact "python" way

print (','.join([ch.id for ch in st[0]]))

chains_ok = ['A', 'C']

for chn in st[0]:
    if chn.id not in chains_ok:
        st[0].detach_child(chn.id)

output_pdb_path = "chainsAC.pdb"

pdbio = PDBIO()

pdbio.set_structure(st)
pdbio.save(output_pdb_path)

