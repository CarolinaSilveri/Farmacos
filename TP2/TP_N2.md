

## TP2: Evaluación in silico de propiedades ADMET y filtros de selección de candidatos a fármaco

**Profesora**: Dra. Ana Julia Velez Rueda

En el diseño de fármacos, una de las principales causas de fracaso en fases clínicas es la falta de propiedades farmacocinéticas adecuadas o la aparición de toxicidad inesperada. Para minimizar costos y tiempo, se aplican métodos in silico que permiten predecir la Absorción, Distribución, Metabolismo, Excreción y Toxicidad (ADMET) de moléculas candidatas.

Además, se utilizan filtros de “drug-likeness”, como las reglas de Lipinski y Veber, junto con los filtros de PAINS, para descartar compuestos con baja probabilidad de éxito o con estructuras problemáticas.

### CONSIGNAS PRÁCTICOS
 1. Selección de compuestos:
    a. Ingresar a PubChem (https://pubchem.ncbi.nlm.nih.gov). 
    Utilizar la barra de búsqueda, para encontrar información de los siguientes compuesto: aspirin, paracetamol y caffeine. Obtener el “Canonical SMILES” del compuesto para los pasos anteriores

    1. Aspirin: CC(=O)OC1=CC=CC=C1C(=O)O
    2. Paracetamol: CC(=O)NC1=CC=C(C=C1)O
    3. Caffeine: CN1C=NC2=C1C(=O)N(C(=O)N2C)C

    b. Seleccionar 3 fármacos conocidos y 2 experimentales utilizando las palabras clave: anticancer candidate, natural product, experimental drug.

    1. Fármacos conocidos:
        1. Doxorubicin: C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=C(C4=O)C(=CC=C5)OC)O)(C(=O)CO)O)N)O
            Es un fármaco aprobado y conocido para el tratamiento de cáncer y se utiliza como parte de la quimioterapia estándar. Pertenece al grupo de las antraciclinas, que son antibióticos antitumorales. Interfiere en la sintesís de ADN de las células cancerosas.
        2. Paclitaxel: CC1=C2[C@H](C(=O)[C@@]3([C@H](C[C@@H]4[C@]([C@H]3[C@@H]([C@@](C2(C)C)(C[C@@H]1OC(=O)[C@@H]([C@H](C5=CC=CC=C5)NC(=O)C6=CC=CC=C6)O)O)OC(=O) C7=CC=CC=C7)(CO4)OC(=O)C)O)C)OC(=O)C
            Este fármaco, inhibe la despolimerización de los microtúbulos, bloqueando la división celular.
        3. Vincristine:  CC[C@@]1(C[C@@H]2C[C@@](C3=C(CCN(C2)C1)C4=CC=CC=C4N3)(C5=C(C=C6C(=C5)[C@]78CCN9[C@H]7[C@@](C=CC9)([C@H]([C@@]([C@@H]8N6C=O)(C(=O)OC)O)OC(=O)C)CC)OC)C(=O)OC)O
            Interfiere con la formación del huso mitótico, impidiendo la mitosis.
    2. Fármacos experimentales:
        1. Irofulven: CC1=C(C2=C(C3(CC3)[C@@](C(=O)C2=C1)(C)O)C)CO
            Interfiere con la replicación del ADN.
        2. Trabectedina: CC1=CC2=C([C@@H]3[C@@H]4[C@H]5C6=C(C(=C7C(=C6[C@@H](N4[C@H]([C@H](C2)N3C)O)COC(=O)[C@@]8(CS5)C9=CC(=C(C=C9CCN8)O)OC)OCO7)C)OC(=O)C)C(=C1OC)O
            Se une al ADN y afecta la maquinaria de reparación, provocando muerte celular.



 2. Realizar la predicción de propiedades fisicoquímicas de las moléulas obtenidas en el punto 1.a, mediante el uso de la herramienta SwissADME (http://www.swissadme.ch). Utilizando los SMILES obtenidos en el punto anterior, obtener de ambos fármacos:

    a. Peso molecular --> g/mol

    b. LogP (índice de lipofilicidad) --> Utilizo el promedio de los cinco, es decir, Consensus LogP

    c. H-bond acceptors 

    d. H-bond donors

    e. TPSA (Superficie polar)

    f. Rotatable bonds

    |  Compuesto  | Peso Molecular | LogP | H-bond acceptors | H-bond donors | TPSA  | Rotatable bonds |
    |:-----------:|:--------------:|:----:|:----------------:|:-------------:|:-----:|:---------------:|
    |   Aspirin   |     180.16     | 1.28 |        4         |       1       | 63.60 |        3        |
    | Paracetamol |     151.16     | 0.93 |        2         |       2       | 49.33 |        2        |
    |  Caffeine   |     194.19     | 0.08 |        3         |       0       | 61.82 |        0        |
   



3. Identificar subestructuras indeseables de los compuestos del punto 1.ay 1.b usando la la siguiente módulo de python creado para tal fin siguiendo el tutorial:

```python
$ pip install rdkit-pypi molvs requests pandas numpy matplotlib seaborn
$ pip install deepchem 
$ python
Python 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from admet_module import analisis_completo
>>> mis_moleculas = {'molecula': 'COc1ccccc1C=O'}
>>> resultados = analisis_completo(mis_moleculas)
>>> print(resultados.keys())
>>> print(resultados['propiedades'])
```

4. Realizar la predicción de toxicidad in silico utilizando ProTox-II (https://tox-new.charite.de/protox_II/). Utilizando los SMILES de moléculas del punto 1.a y 1.b, obtener: 

    a. Predicted LD50 (mg/kg) y clase de toxicidad (I–VI).

    b. Riesgo de hepatotoxicidad, mutagenicidad, carcinogenicidad.

    ¿Cuál de las moléculas seleccionadas muestra menor toxicidad según ProTox-II?

5. Construir una ficha técnica de cada compuesto que considere las respuestas a las siguientes preguntas: ¿Qué compuestos cumplen mejor con los filtros de Lipinski y Veber? ¿Aparecieron moléculas con alertas PAINS? ¿Cuál es su toxicidad?
