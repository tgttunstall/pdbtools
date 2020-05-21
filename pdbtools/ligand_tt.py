#!/usr/bin/env python

# Copyright 2008, Michael J. Harms
# This program is distributed under General Public License v. 3.  See the file
# COPYING for a copy of the license.

__description__ = \
"""
pdb_ligand_tt.py

Spits out a dict containing pdb code as key and ligands within the pdb id as a list.
"""
__author__ = "Tanushree Tunstall"
__date__ = ""

import os
from biopandas.pdb import PandasPdb

BORING_LIGANDS = ["HOH","CA","SO4","IOD","NA","CL","GOL","PO4"]

#def pdbLigand(pdb, skip_boring = False):
def pdbLigand(pdb):
    """
    """
    ligands_dict = {}
    #print('input in ligand_tt:', pdb)
    pdb_id = pdb.code
    #print('dict key:', pdb.code)
    het = pdb.df['HETATM']
    het_list = list(set(het['residue_name']))
    ligands = [l for l in het_list if l not in BORING_LIGANDS]
    lig_dict = {pdb_id:ligands}
    #lig_dict = {pdb_id:het_list} # include BORING_LIGANDS
    ligands_dict.update(lig_dict)
    
    return(ligands_dict)


