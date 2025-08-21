
# Dynamiques de recherche sur les virus en Afrique : une analyse pré- et post-COVID-19

---

## 📌 Contexte
En Afrique, les maladies virales représentent un enjeu de santé publique majeur, avec des pathologies telles que le VIH, les hépatites B et C, la fièvre jaune ou encore Ebola. La récente pandémie de COVID-19 a mis en lumière, de manière encore plus évidente, la nécessité d’approfondir la recherche et la compréhension des virus.

Ce projet vise à analyser les tendances de la recherche scientifique sur les virus étudiés en Afrique, en s’appuyant sur des données extraites d’articles scientifiques et de bases spécialisées telles que PubMed, afin de mieux comprendre l’évolution de l’intérêt scientifique porté à ces virus avant et après la pandémie de COVID-19

---

## 🎯 Objectifs du projet
- Analyser la répartition géographique des recherches menées sur les virus à travers le continent.
- Identifier les virus ayant fait l’objet du plus grand nombre d’études scientifiques en Afrique.    
- Étudier l’évolution temporelle des publications afin de dégager les tendances de recherche avant et après la pandémie de COVID-19.  
- Explorer les co-occurrences entre différents virus pour mieux comprendre les thématiques associées dans les travaux scientifiques.  
---

## 🛠️ Outils & Technologies
- **Python** (Pandas) → manipulation et nettoyage des données [lien du code](https://github.com/nabil1said/Nabil-Said-Data_Analyst-Portfolio/blob/main/les%20etapes%20pour%20pour%20ce%20%20projet.md)  
- **Visualisation** : Matplotlib, Plotly, HoloViews  
- **Text mining** : SpaCy, FlashText  
- **Environnement** : Jupyter Notebook / Google Colab
- **Scrapping** : pubmed e-utilities  
---

## 📊 Dataset
- **Source** :
  -  Articles scientifiques pubmed (2016–2024)
  -  Noms de virus extrait de https://viralzone.expasy.org/678)
- **Taille** : 29933 articles, 11 colonnes ('PMID', 'Pays', 'Affiliation', 'Authors_Countries','Detected_Viruses', 'Detected_Families','clé_composite', 'year', 'pandemie)  
- **Nettoyage effectué** :  
  - Normalisation des noms de virus  
  - Harmonisation des noms de pays auteurs
  - Extraction des entités biologiques (NLP)  
---

## 🔍 Analyse & Résultats

- 🏆 **Évolution du nombre d’articles publiés par année et par pays**

   <img width="1395" height="525" alt="article  par pays et par année" src="https://github.com/user-attachments/assets/fc6378b6-8435-45a7-8d37-b34912f789a0" />

- 📈 **Nombre d'articles impliquant au moins une institution par pays, avant et après la pandémie (2016 - 2020)**
  
  <img width="1350" height="591" alt="pays article" src="https://github.com/user-attachments/assets/8ba498bd-7dce-456b-8af1-e3d46ac93519" />
  
- 📈 **Tendance temporelle** : Dynamique des publications entre 2016 et 2020
  
<img width="1395" height="525" alt="covid graph" src="https://github.com/user-attachments/assets/7471a9b6-9761-4aa0-9735-2df3f7749ff5" />

- 🏆 ** Virus et familles virales étudiés (2016–2024) **
 - les virus

     <img width="800" height="400" alt="nuage_virus" src="https://github.com/user-attachments/assets/ddd45756-e4e7-45c9-ac37-7123ed89b954" />
   
 - les familles etudiés
   
   <img width="2249" height="1687" alt="famille_viral_etudié" src="https://github.com/user-attachments/assets/680da409-81a2-4055-bc19-d9a1ef961d2c" />

  
- 🏆 ** Top 10 des Virus les plus étudiés avant et  apres la pandemie COVID-19**
  
  <img width="1000" height="500" alt="Top 8 de virus etudie avant et apres le covid (2)" src="https://github.com/user-attachments/assets/a4332e0a-2c48-450e-b87e-f8f410be6b7a" />


- 🔗 **Top virus pairs most frequently studied** 
  - 🔝 Top 10 co-occurring virus pairs
  <img width="1073" height="525" alt="Most frequently studied pairs of viruses" src="https://github.com/user-attachments/assets/3fa81a4c-b14f-421a-a670-47c4f8be5fad" />

  - 🌍 Chord Diagram of All Virus Co-occurrences [lien vers le interctif graph](Click here to view the interactive graph)
 
# Concluision
  L’analyse montre que la production scientifique dans la zone Afrique a fortement augmenté après l’émergence du coronavirus (2020-2024), avec une croissance moyenne de 39,3 % et un pic en 2020. Cependant, en excluant les articles impliquant le SARS-COV-2, l’augmentation réelle n’est que de 8 %.
 Ces résultats mettent en évidence l’impact direct de la pandémie de COVID-19 sur les dynamiques de publication, révélant une réorientation massive vers le SARS-CoV-2, tandis que la recherche sur les autres virus a progressé de manière plus modeste mais régulière.
En résumé, la pandémie a constitué un facteur déterminant dans l’évolution récente des publications scientifiques, mais l’augmentation globale reste beaucoup plus nuancée lorsqu’on isole les thématiques non liées au coronavirus.


