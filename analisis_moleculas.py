from admet_module import analisis_completo
mis_moleculas = {'Aspirin': 'CC(=O)OC1=CC=CC=C1C(=O)O', 'Paracetamol': 'CC(=O)NC1=CC=C(C=C1)O', 'Caffeine':'CN1C=NC2=C1C(=O)N(C(=O)N2C)C', 'Doxorubicin': 'C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=C(C4=O)C(=CC=C5)OC)O)(C(=O)CO)O)N)O', 'Paclitaxel':'CC1=C2[C@H](C(=O)[C@@]3([C@H](C[C@@H]4[C@]([C@H]3[C@@H]([C@@](C2(C)C)(C[C@@H]1OC(=O)[C@@H]([C@H](C5=CC=CC=C5)NC(=O)C6=CC=CC=C6)O)O)OC(=O)C7=CC=CC=C7)(CO4)OC(=O)C)O)C)OC(=O)C', 'Vincristine1':'CC[C@@]1(C[C@@H]2C[C@@](C3=C(CCN(C2)C1)C4=CC=CC=C4N3)(C5=C(C=C6C(=C5)[C@]78CCN9[C@H]7[C@@](C=CC9)([C@H]([C@@]([C@@H]8N6C=O)(C(=O)OC)O)OC(=O)C)CC)OC)C(=O)OC)O', 'Irofulven':'CC1=C(C2=C(C3(CC3)[C@@](C(=O)C2=C1)(C)O)C)CO', 'Trabectedina':' CC1=CC2=C([C@@H]3[C@@H]4[C@H]5C6=C(C(=C7C(=C6[C@@H](N4[C@H]([C@H](C2)N3C)O)COC(=O)[C@@]8(CS5)C9=CC(=C(C=C9CCN8)O)OC)OCO7)C)OC(=O)C)C(=C1OC)O'}
resultados = analisis_completo(mis_moleculas)
print(resultados.keys())
print(resultados['propiedades'])
