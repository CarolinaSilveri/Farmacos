# analisis_moleculas.py
from admet_module import analisis_completo
import pandas as pd

# 1) Tus moléculas (Nombre: SMILES)
mols = {
    "Aspirin": "CC(=O)OC1=CC=CC=C1C(=O)O",
    "Paracetamol": "CC(=O)NC1=CC=C(C=C1)O",
    "Caffeine": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
    "Doxorubicin": "C[C@H]1C2=C(C(=O)c3c(O)c4C(=O)c5c(O)cccc5C(=O)c4cc(O)c3O)C(O)=C(C(=O)CO)C[C@H](O)[C@@H](N)[C@H]1O",
    "Paclitaxel": "CC(C)C(=O)O[C@H]1C[C@@H]2OC(=O)[C@]3(CC[C@@H]4[C@@H](OC(=O)c5ccccc5)[C@H](O)C[C@]34C)[C@H]2C[C@@H]1OC(=O)c1ccccc1",
    "Vincristine": "CCN1CC[C@@]23C(=O)N4[C@H](CC[C@@H]5[C@@]2(O)Cc6c7cccc(O)c7[nH]c6[C@@H]5OC(=O)C)C[C@H]3C[C@@]14OC(=O)C",
    "Irofulven": "CC1=C2C[C@]3(O)C(=O)OC[C@@H]3C(=O)C2=CO1",
    "Trabectedin": "COc1ccc2c(c1)C1=C(C(=O)O)C3=C4C(=O)OCCN4CCc5ccc(OC)c(c5)[C@@]3(OC)C(OC)=O"
}

# 2) Correr tu análisis
r = analisis_completo(mols)

# 3) Calcular VEeber fuera del módulo (clásico: RB ≤10 y TPSA ≤140)
prop = r["propiedades"].copy()
prop["Veber_Pass"] = (prop["RotatableBonds"] <= 10) & (prop["TPSA"] <= 140)

# (opcional) Versión “original Veber”: RB ≤10 y (TPSA ≤140 **o** HBA+HBD ≤12)
prop["Veber_Pass_Alt"] = (prop["RotatableBonds"] <= 10) & (
    (prop["TPSA"] <= 140) | ((prop["HBA"] + prop["HBD"]) <= 12)
)

# 4) PAINS y Toxicidad ya los da tu módulo:
pains = r["pains"][["Name","PAINS_Alerts","PAINS_Details"]]
tox   = r["toxicidad"][["Name","Toxicity_Alerts","Predicted_Toxicity","Estimated_LD50"]]

# 5) Tabla resumen: Veber + PAINS + Toxicidad
resumen = (prop[["Name","MW","LogP","HBA","HBD","TPSA","RotatableBonds","Veber_Pass"]]
           .merge(pains, on="Name")
           .merge(tox, on="Name"))

# 6) Mostrar
pd.set_option("display.max_colwidth", 120)
print(resumen.to_string(index=False))

# 7) (opcional) Guardar a CSV para pegar en el TP
resumen.to_csv("resumen_veber_pains_toxicidad.csv", index=False, encoding="utf-8")
print("\nArchivo generado: resumen_veber_pains_toxicidad.csv")
