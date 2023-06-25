import os
import re
from PyPDF2 import PdfReader
import pandas as pd

# Créez un DataFrame vide avec les colonnes requises
df = pd.DataFrame(columns=["Ref", "Date facturation", "Date échéance", "Client Code", "Total HT", "Total TTC"])

# Parcourez tous les fichiers PDF dans le dossier "facture"
for filename in os.listdir("facture"):
    if filename.endswith(".pdf"):
        # Ouvrez le fichier PDF
        with open(os.path.join("facture", filename), "rb") as file:
            reader = PdfReader(file)
            content = reader.pages[0].extract_text()

            #Permet de voir comment est fait le pdf en 1 coup d'oeil 
            #print("===== Raw Content =====")
            #print(content)
            #print("=======================")

            # Recherchez les informations requises dans le contenu du fichier PDF
            ref_match = re.search(r"Réf\. : (\d{2}\s*\d{2}-\d{4})", content)
            ref = ref_match.group(1) if ref_match is not None else "No match found"
            date_facturation_match = re.search(r"Date facturation : (\d{2}/\d{2}/\d{4})", content)
            date_facturation = date_facturation_match.group(1) if date_facturation_match is not None else "No match found"
            date_echeance_match = re.search(r"Date échéance : (\d{2}/\d{2}/\d{4})", content)
            date_echeance = date_echeance_match.group(1) if date_echeance_match is not None else "No match found"
            client_code_match = re.search(r"Code client : ([A-Z]{2}\s*\d{4}-\d{4})", content)
            client_code = client_code_match.group(1) if client_code_match is not None else "No match found"
            total_ht_match = re.search(r"Total HT ([\d\s]*,\d{2})", content)
            total_ht = total_ht_match.group(1) if total_ht_match is not None else "No match found"
            total_ttc_match = re.search(r"Total TTC ([\d\s]*,\d{2})", content)
            total_ttc = total_ttc_match.group(1) if total_ttc_match is not None else "No match found"

            # Ajoutez les informations au DataFrame
            df.loc[len(df)] = [ref, date_facturation, date_echeance, client_code, total_ht, total_ttc]

# Écrivez le DataFrame dans un fichier .xlsx
df.to_excel("factures.xlsx", index=False)
