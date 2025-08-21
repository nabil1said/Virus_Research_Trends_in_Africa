# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 21:54:01 2025

@author: NTOYB
"""

# %% 

# %% 
!pip install -q https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz
!pip install -q https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz
!pip install -q https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bionlp13cg_md-0.5.4.tar.gz


# %% 

# code optimisé pour multiprocessing
import spacy
import pandas as pd
import os
import zipfile
#from google.colab import files
import shutil

import concurrent.futures
from tqdm import tqdm

print("bibliotheque importe")

# %% 


# 🧠 CHARGEMENT DES MODÈLES
try:
    nlp_models = {
        "sci": spacy.load("en_core_sci_sm"),
        "bc5cdr": spacy.load("en_ner_bc5cdr_md"),
        "bionlp": spacy.load("en_ner_bionlp13cg_md")
    }
except OSError as e:
    raise Exception(f"❌ Modèle spaCy manquant. Veuillez installer les modèles requis: {str(e)}")

# 🔍 FONCTION D'EXTRACTION MULTIMODÈLE
def extraire_entites(pmid, text):
    entites = {"PMID": pmid}
    for model_name, nlp in nlp_models.items():
        doc = nlp(str(text))
        entites[f"Entities_{model_name}"] = ", ".join(sorted(set(ent.text for ent in doc.ents)))
    return entites

# 📂 CHEMIN DU FICHIER ZIP LOCAL
zip_filename = "pubmed_fichier_excels_step1.zip"  # Remplacez par le chemin de votre fichier ZIP local

# 📂 EXTRACTION DU ZIP
extract_dir = "extracted_files"
os.makedirs(extract_dir, exist_ok=True)
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# 🔍 RÉCUPÉRER TOUS LES FICHIERS .xlsx
excel_files = [
    os.path.join(root, file)
    for root, _, files in os.walk(extract_dir)
    for file in files if file.lower().endswith(".xlsx")
]

if not excel_files:
    raise Exception("❌ Aucun fichier .xlsx trouvé dans le ZIP.")

# 📂 DOSSIER DE SORTIE
output_dir = "fichiers_traites"
os.makedirs(output_dir, exist_ok=True)


# 🧪 TRAITEMENT DE CHAQUE FICHIER
for path in excel_files:
    file = os.path.basename(path)
    print(f"\n📄 Traitement de : {file}")

    try:
        df = pd.read_excel(path)
        df = df.rename(columns={"Titre (TI)": "Titre", "Résumé (AB)": "Résumé"})

        if not {'PMID', 'Titre', 'Résumé'}.issubset(df.columns):
            print(f"⚠️ Le fichier {file} ne contient pas les colonnes requises. Ignoré.")
            continue

        # Combinaison des colonnes
        df["titre_resume"] = df["Titre"].fillna("") + " " + df["Résumé"].fillna("")

        # Parallélisation avec ThreadPoolExecutor et barre de progression
        entites_list = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(extraire_entites, pmid, text): idx
                for idx, (pmid, text) in enumerate(zip(df["PMID"], df["titre_resume"]))
            }

            for future in tqdm(concurrent.futures.as_completed(futures),
                             total=len(futures),
                             desc=f"🔄 Traitement de {file}"):
                try:
                    entites_list.append(future.result())
                except Exception as e:
                    print(f"⚠️ Erreur lors du traitement d'une entrée: {str(e)}")
                    continue

        # Création du DataFrame final
        df_entites = pd.DataFrame(entites_list)
        df_final = pd.merge(df, df_entites, on="PMID", how="left")

        # Sauvegarde du résultat
        output_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}_entites.xlsx")
        df_final.to_excel(output_path, index=False)
        print(f"✅ Fichier traité sauvegardé: {output_path}")

    except Exception as e:
        print(f"❌ Erreur lors du traitement du fichier {file}: {str(e)}")
        continue

# 📦 ZIPPAGE FINAL
if os.listdir(output_dir):  # Vérifie si le dossier n'est pas vide
    shutil.make_archive("resultats_entites", 'zip', output_dir)
    files.download("resultats_entites.zip")
    print("\n✅ Tous les fichiers ont été traités et sont disponibles dans resultats_entites.zip")
else:
    print("\n⚠️ Aucun fichier n'a été traité avec succès.")












