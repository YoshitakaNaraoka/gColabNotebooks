from rdkit.Chem import Descriptors
from Mol_List import mol_list

mols = [x for x in mol_list if x is not None]
len(mols) # 2
### TPSAの計算
declist = Descriptors.descList
calc = {}
for (i,j) in declist:
    calc[i] = j
tpsa = [calc['TPSA'](i) for i in mols]