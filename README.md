# FACTURE

## Description

Ce script Python permet d'extraire des informations spécifiques à partir de factures au format PDF stockées dans un dossier nommé "facture". Les informations extraites sont ensuite stockées dans un fichier Excel (.xlsx).

## Utilisation

1. Assurez-vous d'avoir tous les fichiers PDF nécessaires dans un dossier appelé "facture".
2. Exécutez le script Python. Le script parcourra tous les fichiers PDF dans le dossier "facture".

## Dépendances

Ce script nécessite les packages Python suivants :
* os
* re
* PyPDF2
* pandas

Vous pouvez installer ces dépendances en utilisant pip :

```bash
pip install PyPDF2 pandas
```

## Détails du fonctionnement

Le script fonctionne de la manière suivante :

Il crée d'abord un DataFrame pandas vide avec les colonnes spécifiques requises.
Il parcourt ensuite tous les fichiers du dossier "facture".
Pour chaque fichier PDF, il l'ouvre et extrait le texte de la première page.
Il utilise des expressions régulières pour rechercher des informations spécifiques dans le contenu du fichier PDF.
Il ajoute ces informations au DataFrame pandas.
Enfin, il écrit le DataFrame dans un fichier .xlsx nommé "factures.xlsx".

## Limitations
Ce script fonctionne sur l'hypothèse que toutes les factures ont un format similaire et contiennent toutes les informations nécessaires. Si une facture n'a pas une certaine information, le script enregistrera "No match found" pour cette information.

De plus, le script extrait uniquement le texte de la première page de chaque facture. Si les informations nécessaires se trouvent sur d'autres pages, elles ne seront pas extraites.# exercice_okayo
