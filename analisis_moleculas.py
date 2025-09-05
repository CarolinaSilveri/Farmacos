from admet_module import analisis_completo
mis_moleculas = {'Aspirin': 'CC(=O)OC1=CC=CC=C1C(=O)O', 'Paracetamol': 'CC(=O)NC1=CC=C(C=C1)O', 'Caffeine':'CN1C=NC2=C1C(=O)N(C(=O)N2C)C'}
resultados = analisis_completo(mis_moleculas)
print(resultados.keys())
print(resultados['propiedades'])
