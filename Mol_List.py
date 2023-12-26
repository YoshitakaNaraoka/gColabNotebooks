# MolFromSmilesで生成した分子を構造式表示するにはdisplayコマンド
from rdkit import Chem
mol_list = [
benzene = Chem.MolFromSmiles("c1ccccc1"),
alanine = Chem.MolFromSmiles('CC(C(=O)O)N'),
phenylalanine = Chem.MolFromSmiles('c1ccccc1CC(C(=O)O)N'),
crown = Chem.MolFromSmiles('C1COCCOCCOCCOCCOCCO1'),
ciguatoxin = Chem.MolFromSmiles('CC1CC2C(CC3C(O2)C(C(C4C(O3)C(C(C5(O4)CC(CO5)O)C)C)O)C)OC6CC7C(C(CC8C(O7)CC=CCC9C(O8)C=CC2C(O9)C=CC3C(O2)CC2C(O3)C(C3C(O2)CC=CC(O3)C=CC(CO)O)O)O)(OC6C1)C'),
]
