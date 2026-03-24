# Intellectual Property Checker 
 
> **FR** - Outil interactif en ligne de commande pour comprendre qui détient les droits sur une création professionnelle.  
 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform: macOS | Linux | Windows](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)]()
 
---
 
##  À quoi ça sert ?
 
Tu as créé quelque chose dans le cadre de ton travail - un logiciel, un design, un texte, une invention - et tu te demandes à qui appartiennent les droits dessus ? Ce formulaire t'aide à y voir plus clair.
 
En répondant à une série de questions simples, tu obtiens :
- une **analyse de ta situation** selon ton statut (salarié, alternant, stagiaire, agent public, freelance)
- des **références aux articles de loi** qui s'appliquent à ton cas
- des **alertes automatiques** si ta situation présente des points de vigilance
- des **conseils concrets** sur ce que tu peux faire
- un **export de ton diagnostic** en fichier texte si tu veux le garder
 
Le questionnaire couvre le **droit d'auteur** (œuvres, logiciels), le **droit des brevets** (inventions) et les **bases de données**.
 
>  Outil d'orientation uniquement - pas un avis juridique. Pour une situation complexe ou un litige, consulte un professionnel du droit.
 
---
 
##  Ce que le formulaire analyse
 
| Domaine | Couverture |
|---|---|
|  Logiciels & code | Régime salarié (art. L113-9 CPI), freelance, stagiaire, alternant, agent public |
|  Œuvres classiques | Textes, visuels, design, musique, vidéo - absence de cession automatique |
|  Inventions | Mission inventive, hors mission connexe, hors mission totale (art. L611-7 CPI) |
|  Bases de données | Droit d'auteur + droit sui generis (art. L341-1 CPI) |
|  Intelligence artificielle | Analyse de la contribution humaine et impact sur la protection |
|  Clauses contractuelles | Analyse de la précision et de la validité des clauses de cession |
 
---
 
##  Prérequis
 
**Python 3.8 ou supérieur.** C'est tout. Aucune bibliothèque externe à installer.
 
### Vérifier si Python est installé
 
Ouvre un terminal et tape :
 
```bash
python3 --version
```
 
Si tu vois quelque chose comme `Python 3.11.2`, c'est bon. Si tu obtiens une erreur, suis la section [Installer Python](#-installer-python) ci-dessous.
 
---
 
##  Installer Python
 
<details>
<summary><strong>macOS</strong></summary>
 
**Option 1 - Site officiel (recommandé pour les débutants)**
 
1. Va sur [python.org/downloads](https://www.python.org/downloads/)
2. Clique sur **"Download Python 3.x.x"**
3. Ouvre le fichier `.pkg` téléchargé et suis les instructions
4. Vérifie l'installation : `python3 --version`
 
**Option 2 - Homebrew (si tu l'as déjà)**
```bash
brew install python3
```
 
</details>
 
<details>
<summary><strong>Linux (Ubuntu / Debian)</strong></summary>
 
Python est souvent déjà installé. Vérifie :
```bash
python3 --version
```
 
Si ce n'est pas le cas :
```bash
sudo apt update
sudo apt install python3
```
 
</details>
 
<details>
<summary><strong>Windows</strong></summary>
 
1. Va sur [python.org/downloads](https://www.python.org/downloads/)
2. Clique sur **"Download Python 3.x.x"**
3. Lance l'installeur
4.  **Coche bien la case "Add Python to PATH"** avant de cliquer sur Install
5. Vérifie l'installation dans PowerShell : `python --version`
 
</details>
 
---
 
##  Télécharger le projet
 
### Option A - Télécharger directement (le plus simple)
 
1. Sur cette page GitHub, clique sur le bouton vert **`<> Code`** en haut à droite
2. Clique sur **"Download ZIP"**
3. Extrais le dossier ZIP où tu veux sur ton ordinateur
 
### Option B - Cloner avec Git
 
Si tu as Git installé :
 
```bash
git clone https://github.com/sa0/ip_checker.git
cd ip_checker
```
 
---
 
##  Lancer le formulaire
 
### macOS et Linux
 
1. Ouvre un terminal
2. Navigue jusqu'au dossier du projet :
```bash
cd chemin/vers/ip_checker
```
3. Lance le script :
```bash
python3 ip_checker.py
```
 
### Windows
 
1. Ouvre PowerShell ou l'invite de commandes
2. Navigue jusqu'au dossier :
```powershell
cd C:\chemin\vers\ip_checker
```
3. Lance le script :
```powershell
python ip_checker.py
```
 
>  **Astuce navigation** : tu peux aussi ouvrir directement un terminal dans le bon dossier. Sur macOS, fais un clic droit sur le dossier → "Nouveau terminal au dossier". Sur Windows, Shift + clic droit → "Ouvrir PowerShell ici".
 
---
 
##  Structure du projet
 
```
ip_checker/
├── ip_checker.py     ← le script principal - c'est lui qu'on lance
├── README.md         ← ce fichier
└── LICENSE           ← licence MIT
```
 
Le script génère un fichier de résultats horodaté dans le même dossier si tu choisis de l'exporter à la fin du diagnostic :
 
```
ip_checker_resultat_20240115_143200.txt
```
 
---
 
##  Déroulement du formulaire
 
Le formulaire est divisé en **8 blocs** de questions, dans cet ordre :
 
```
1. Ton statut
   └── Salarié / Alternant / Stagiaire / Agent public / Freelance
 
2. Ta création
   └── Logiciel / Œuvre classique / Invention / Base de données / Plusieurs
 
3. Rôle de l'intelligence artificielle
   └── Aucun / Outil d'aide / Contribution significative / Rôle dominant
   → Sortie anticipée avec analyse dédiée si l'IA a tout produit
 
4. Contexte de création
   └── Origine / Temps de travail / Ressources utilisées
 
5. Questions liées à ton statut
   └── Questions spécifiques selon que tu es salarié, alternant, stagiaire, etc.
 
6. Contrat et clauses
   └── Existence et précision des clauses de cession ou de licence
 
7. Utilisation par l'entreprise
   └── Usage actuel / Mention de ton nom / Accord donné
 
8. Valeur et enjeux
   └── Valeur économique identifiable
```
 
À la fin : analyse, alertes automatiques, conseils, références légales, et option d'export.
 
---
 
##  Aperçu
 
```
================================================================================
                        INTELLECTUAL PROPERTY CHECKER
================================================================================
 
Ce questionnaire t'aide à comprendre qui détient les droits sur une création
réalisée pendant, autour ou à côté de ton activité professionnelle.
 
────────────────────────────────────────────────────────────────────────────────
                            1 / 8  -  TON STATUT
────────────────────────────────────────────────────────────────────────────────
 
Quel est ton statut principal ?
 
  1. Salarié(e)  -  CDI, CDD ou autre contrat de travail
  2. Alternant(e)  -  apprentissage ou contrat de professionnalisation
  3. Stagiaire  -  convention de stage
  4. Agent(e) public(que)  -  fonctionnaire ou contractuel public
  5. Travailleur(euse) indépendant(e)  -  freelance / auto-entrepreneur(euse)
 
>>>
```
 
---
 
##  Références juridiques couvertes
 
Le formulaire s'appuie sur les textes suivants :
 
- **Code de la propriété intellectuelle (CPI)**
  - Art. L111-1 - Droit d'auteur et création de l'esprit
  - Art. L113-9 - Logiciels créés par les salariés
  - Art. L121-1 - Droits moraux (inaliénables)
  - Art. L131-3 - Exigences formelles de la cession de droits
  - Art. L131-3-1 - Agents publics
  - Art. L341-1 - Droit sui generis des bases de données
  - Art. L611-7 - Inventions de salariés (brevets)
  - Art. L613-8 - Cession de brevet
 
---
 
##  Avertissement important
 
Cet outil constitue **uniquement une analyse préliminaire et vulgarisée**. Il ne remplace en aucun cas un avis juridique professionnel.
 
Pour une évaluation personnalisée, il est recommandé de consulter :
- un **syndicat** ou un **représentant du personnel**
- le **service juridique** de ton entreprise ou établissement
- un **avocat spécialisé en propriété intellectuelle**
 
---
 
##  Auteur / Author
 
**sa0**  
Droit du numérique · Propriété intellectuelle
 
---
 
##  Licence
 
Ce projet est distribué sous licence **MIT**.  
Voir le fichier [LICENSE](LICENSE) pour le détail.
 
Ce projet a été inspiré et assisté avec l'aide d'outils d'intelligence artificielle pour la rédaction du code.
