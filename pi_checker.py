import time
import os
import random
import sys
import textwrap

# =======================
# PARTIE 1 : LA BANNIÈRE 
# =======================

# Palette couleurs disponibles
PALETTE_COULEURS = [
    (190, 166, 255),  # Violet
    (100, 204, 142),  # Vert
    (136, 189, 252),  # Bleu
]

# Sélection aléatoire d'une couleur
rouge, vert, bleu = random.choice(PALETTE_COULEURS)
COULEUR_CHOISIE = f"\033[38;2;{rouge};{vert};{bleu}m"
REINITIALISATION = "\033[0m"

# Contenu texte
PHRASE = "per aspera, ad astra ✶"
NOM_SCRIPT = "INTELLECTUAL PROPERTY CHECKER" 

# Logo
logo_gauche = r"""
                      █████
                     ███░░░███
  █████   ██████   ███   ░░███
 ███░░   ░░░░░███ ░███    ░███
░░█████   ███████ ░███    ░███
 ░░░░███ ███░░███ ░░███   ███
 ██████ ░░████████ ░░░█████░
░░░░░░   ░░░░░░░░    ░░░░░░
""".splitlines()

logo_droite = r"""
⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣷⣄⠀⠀⠀⢀⣠⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⠤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⣀⣀
⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢷⣶⣶⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠒
⠀⠀⠀⠀⠀⣠⠟⠋⠁⠀⠀⠀⠙⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
""".splitlines()

# Animation 
def effacer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_banniere(progression=None):
    hauteur_totale = max(len(logo_gauche), len(logo_droite))
    logo_gauche_centre = [""] * ((hauteur_totale - len(logo_gauche)) // 2) + logo_gauche
    logo_droite_centre = [""] * ((hauteur_totale - len(logo_droite)) // 2) + logo_droite

    for ligne_gauche, ligne_droite in zip(logo_gauche_centre, logo_droite_centre):
        if progression:
            ligne_a_afficher = ligne_gauche[:progression].ljust(30) + ligne_droite
        else:
            ligne_a_afficher = ligne_gauche.ljust(30) + ligne_droite
        print(COULEUR_CHOISIE + ligne_a_afficher + REINITIALISATION)

def afficher_en_tete(nom_script):
    """Affiche un en-tête stylisé avec le nom du script"""
    print(COULEUR_CHOISIE + "=" * 80 + REINITIALISATION)
    print(COULEUR_CHOISIE + nom_script.center(80) + REINITIALISATION)
    print(COULEUR_CHOISIE + "=" * 80 + REINITIALISATION)
    print("\n")

def executer_animation_intro():
    """Exécute la séquence complète"""
    # Phase 1: Clignotement mantra
    for _ in range(16):
        effacer_ecran()
        print(COULEUR_CHOISIE + PHRASE.center(80) + REINITIALISATION)
        time.sleep(0.08)
        effacer_ecran()
        time.sleep(0.08)

    # Logo de gauche à droite
    largeur_maximale = max(len(ligne) for ligne in logo_gauche)
    for progression in range(1, largeur_maximale + 1):
        effacer_ecran()
        afficher_banniere(progression=progression)
        time.sleep(0.05)

    # Final
    effacer_ecran()
    afficher_banniere()

def lancer_intro_banniere():
    """Fonction qui gère le déroulé de la bannière"""
    executer_animation_intro()
    time.sleep(1)
    afficher_en_tete(NOM_SCRIPT)

# ===========================
# PARTIE 2 : LE FORMULAIRE 
# ===========================

class FormulaireDroitsSalaries:
    def __init__(self):
        self.reponses = {}
        self.resultat = [] 
        self.width = 80

    def afficher_titre(self):
        print(textwrap.fill("Ce formulaire interactif vous aide à comprendre qui est propriétaire de vos créations (logiciels, inventions, designs, textes...) selon votre situation. Les réponses sont basées sur le droit français et les règlements européens compatibles.", width=self.width))
        print("-" * self.width)
        print("IMPORTANT : Ce résultat est informatif et ne remplace pas l'avis d'un avocat.")
        print("="*self.width + "\n")

    def poser_question(self, cle, question, options):
        """Affiche une question et retourne l'index de la réponse choisie."""
        print(f"\n {question}")
        for i, option in enumerate(options):
            print(f"   {i + 1}. {option}")

        while True:
            choix = input(f"\n   >>> Votre choix (1-{len(options)}) : ")
            if choix.isdigit():
                idx = int(choix) - 1
                if 0 <= idx < len(options):
                    self.reponses[cle] = idx
                    return idx
            print("   /!\\ Choix invalide. Merci de taper le numéro correspondant.")

    def animer_analyse(self):
        print("\nAnalyse de votre situation en cours", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")

    def ajouter_resultat(self, titre, explication, conseil, base_legale):
        self.resultat.append({
            "titre": titre,
            "explication": explication,
            "conseil": conseil,
            "ref": base_legale
        })

    def afficher_rapport(self):
        print("\n" + "#"*self.width)
        print(f"{'VOTRE DIAGNOSTIC PERSONNALISÉ':^{self.width}}")
        print("#"*self.width + "\n")

        for res in self.resultat:
            print(f"RÉSULTAT : {res['titre'].upper()}")
            print("-" * 30)
            print(textwrap.fill(res['explication'], width=self.width))
            print("\n💡 CONSEIL PRATIQUE :")
            print(textwrap.fill(res['conseil'], width=self.width))
            print(f"\n⚖️  Base légale : {res['ref']}")
            print("\n" + "-"*self.width + "\n")

    # --- LOGIQUE MÉTIER ---

    def demarrer(self):
        self.afficher_titre()

        # NIVEAU 1 : STATUT
        opts_statut = ["Salarié (Secteur Privé)", "Agent Public / Fonctionnaire", "Stagiaire", "Journaliste", "Freelance / Indépendant"]
        statut = self.poser_question("statut", "Quel est votre contrat ou statut actuel?", opts_statut)

        if statut == 4: # Freelance
            self.ajouter_resultat(
                "Vous restez propriétaire (sauf cession écrite)",
                "En tant qu'indépendant, le fait d'être payé ne transfère pas vos droits au client. Vous restez propriétaire de tout ce que vous créez, sauf si vous avez signé un contrat de 'cession de droits' spécifique.",
                "Vérifiez vos devis et contrats. Si rien n'est écrit sur la cession des droits, votre client n'a théoriquement pas le droit d'exploiter votre travail sans payer un supplément.",
                "Art. L.111-1 Code de la Propriété Intellectuelle (CPI)"
            )
            self.afficher_rapport()
            return

        # NIVEAU 2 : TYPE DE CRÉATION
        opts_crea = ["Logiciel / Code informatique", "Invention technique (Brevetable)", "Design / Modèle", "Texte / Photo / Création artistique"]
        type_crea = self.poser_question("type_crea", "Qu'avez-vous créé?", opts_crea)

        # BRANCHEMENT
        self.animer_analyse()

        if type_crea == 0:
            self.traiter_logiciel(statut)
        elif type_crea == 1:
            self.traiter_invention(statut)
        elif type_crea == 2:
            self.traiter_design(statut)
        else: # Texte/Art
            self.traiter_oeuvre_classique(statut)

        self.afficher_rapport()

    # --- SCÉNARIOS SPÉCIFIQUES ---

    def traiter_logiciel(self, statut):
        # Cas Stagiaire (Spécifique depuis 2021)
        if statut == 2:
            recherche = self.poser_question("stagiaire_rech", "Votre stage se déroule-t-il dans une structure de RECHERCHE (Labo, Université)?", ["Oui", "Non"])
            if recherche == 0:
                self.ajouter_resultat(
                    "Propriété de la structure d'accueil (Probable)",
                    "Depuis une ordonnance de 2021, si vous êtes stagiaire dans un organisme de recherche et que vous percevez une gratification, vos logiciels appartiennent à l'organisme.",
                    "Demandez si une contrepartie financière spécifique est prévue au-delà de la gratification de stage.",
                    "Art. L.113-9-1 CPI"
                )
            else:
                self.ajouter_resultat(
                    "Vous êtes propriétaire (sauf clause contraire)",
                    "En tant que stagiaire dans une entreprise classique (hors recherche), le code du travail ne s'applique pas totalement. Vous restez propriétaire de votre code, sauf si vous avez signé une clause de cession spécifique.",
                    "L'entreprise vous fera probablement signer une cession de droits avant votre départ pour sécuriser son logiciel.",
                    "Arrêt Jurisprudence 'Puech' / L.111-1 CPI"
                )
            return

        # Cas Salarié / Agent Public
        opts_contexte = ["Dans l'exercice de mes fonctions (au travail)", "Sur mon temps libre avec mes moyens personnels"]
        contexte = self.poser_question("soft_contexte", "Avez-vous créé ce logiciel...", opts_contexte)

        if contexte == 0:
            proprio = "L'EMPLOYEUR" if statut == 0 else "L'ÉTAT / L'ADMINISTRATION"
            bonus = "Pas de prime obligatoire (sauf convention collective rare)" if statut == 0 else "Prime d'intéressement obligatoire (pour les agents publics)"

            self.ajouter_resultat(
                f"C'est la propriété de {proprio}",
                "Pour les logiciels, la loi est stricte : si c'est fait au travail, les droits sont transférés automatiquement à l'employeur. Vous ne pouvez pas empêcher l'entreprise de le vendre ou le modifier.",
                f"{bonus}. Votre nom n'a pas obligation d'être cité sur le logiciel.",
                "Art. L.113-9 CPI"
            )
        else:
            self.ajouter_resultat(
                "C'est VOTRE propriété",
                "Si le logiciel n'a aucun lien avec votre mission et est fait avec vos moyens personnels, il vous appartient.",
                "Attention : N'utilisez jamais le code ou les bibliothèques de votre entreprise dans votre projet personnel.",
                "A contrario Art. L.113-9 CPI"
            )

    def traiter_invention(self, statut):
        if statut == 3: # Journaliste
             print("Note : Le statut de journaliste ne change rien aux règles des brevets.")

        # Le cœur du sujet Inventions
        mission = self.poser_question("inv_mission", "Votre contrat de travail prévoit-il une 'mission inventive' (ex: Ingénieur R&D, Chercheur)?", ["Oui", "Non"])

        if mission == 0: # Invention de mission
            remuneration = "Rémunération Supplémentaire OBLIGATOIRE"
            if statut == 1:
                remuneration = "Prime d'intéressement (50% des revenus de l'invention pour l'agent public)"

            self.ajouter_resultat(
                "Appartient à l'Employeur + VOUS GAGNEZ UNE PRIME",
                f"C'est une 'Invention de Mission'. L'employeur dépose le brevet à son nom. En échange, vous avez droit à une {remuneration}.",
                "Si votre contrat ou la convention collective ne donne pas de montant, c'est un juge ou une commission (CNIS) qui peut le fixer. Ne signez pas de renonciation à cette prime.",
                "Art. L.611-7 (1) CPI"
            )
        else:
            lien = self.poser_question("inv_lien", "L'invention a-t-elle un lien avec l'entreprise (domaine d'activité, utilisation de machines de l'entreprise)?", ["Oui", "Non"])

            if lien == 0: # Hors mission attribuable
                self.ajouter_resultat(
                    "A vous... mais l'employeur peut l'acheter (Droit d'attribution)",
                    "C'est une invention 'Hors Mission Attribuable'. Elle est à vous au départ, mais l'employeur a le droit de se l'attribuer (de vous la prendre) s'il le souhaite.",
                    "S'il la prend, il doit vous payer un 'JUSTE PRIX' (souvent plus élevé qu'une simple prime). Vous DEVEZ déclarer l'invention à votre employeur pour qu'il se décide.",
                    "Art. L.611-7 (2) CPI"
                )
            else: # Hors mission non attribuable
                self.ajouter_resultat(
                    "Propriété EXCLUSIVE du salarié",
                    "C'est une invention libre. L'employeur n'a aucun droit dessus.",
                    "Vous pouvez la breveter à votre nom ou créer votre entreprise (attention à la non-concurrence).",
                    "Art. L.611-7 (2) CPI"
                )

    def traiter_design(self, statut):
        print("\n--- Analyse Spéciale Design ---")
        print("Le design (objet, vêtement, interface) est complexe car protégé par deux droits : Droit d'auteur + Dessins et Modèles.")

        clause = self.poser_question("design_clause", "Votre contrat contient-il une clause disant que 'tous les modèles créés appartiennent à l'entreprise'?", ["Oui, c'est écrit", "Non, rien de précis"])

        if clause == 0:
            self.ajouter_resultat(
                "Probable Propriété Employeur (via le contrat)",
                "Bien que vous soyez l'auteur, vous avez signé une cession. De plus, le droit de l'Union Européenne considère que l'employeur est propriétaire des modèles créés par les salariés.",
                "Vérifiez que la clause est bien rédigée (délimitation géographique, durée...).",
                "Règlement CE 6/2002 (Art 14) vs L.111-1 CPI"
            )
        else:
            self.ajouter_resultat(
                "Situation Hybride (Conflit France / Europe)",
                "En droit français pur, vous restez auteur. Mais en droit européen, l'employeur est titulaire du modèle. En pratique, l'employeur exploitera le design.",
                "Sans clause de cession écrite, vous pourriez théoriquement réclamer des droits d'auteur, mais c'est une procédure complexe face au droit européen.",
                "Conflit L.111-1 CPI / Règlement CE"
            )

    def traiter_oeuvre_classique(self, statut):
        # Journalistes
        if statut == 3:
            # Correction: Ajout des options manquantes
            opts_usage = ["Dans le titre initial (journal/site d'origine)", "Dans un autre titre du groupe", "Utilisation commerciale (pub, livre, produit dérivé)"]
            usage = self.poser_question("journ_usage", "L'article/photo sera utilisé où?", opts_usage)
            if usage == 0:
                self.ajouter_resultat("Cession incluse dans le salaire", "Votre salaire couvre déjà le droit de publier votre article dans le journal.", "C'est normal.", "L.132-36 CPI")
            elif usage == 1:
                self.ajouter_resultat("Droit à rémunération complémentaire", "Pour une utilisation dans un autre journal du groupe, vous devez toucher un complément.", "Vérifiez les accords d'entreprise.", "L.132-39 CPI")
            else:
                self.ajouter_resultat("Accord obligatoire + Paiement", "Toute utilisation hors presse nécessite votre accord écrit et un paiement spécifique en droits d'auteur.", "Ne laissez pas faire sans contrat.", "L.132-40 CPI")
            return

        # Cas général (Salarié lambda qui écrit un rapport, fait une photo, un logo...)
        collectif = self.poser_question("class_coll", "S'agit-il d'une 'Œuvre Collective' (ex: un dictionnaire, un site web complexe) où votre travail est fondu dans l'ensemble sans qu'on puisse distinguer votre part?", ["Oui, c'est fusionné", "Non, mon travail est distinct"])

        if collectif == 0:
             self.ajouter_resultat(
                 "Propriété de l'Employeur (Œuvre Collective)",
                 "L'œuvre collective appartient à la personne (entreprise) qui l'édite et la divulgue. Vous n'avez pas de droit dessus.",
                 "C'est l'exception majeure au droit d'auteur français.",
                 "Art. L.113-5 CPI"
             )
        else:
             cession = self.poser_question("class_cess", "Votre contrat prévoit-il une cession des droits (Clause de Propriété Intellectuelle)?", ["Oui", "Non"])
             if cession == 0:
                 self.ajouter_resultat(
                     "Propriété Employeur (selon la clause)",
                     "L'employeur détient les droits, mais SEULEMENT ceux listés dans le contrat. La 'cession globale des œuvres futures' est interdite en France.",
                     "Si la clause dit 'tout appartient à l'entreprise sans limite', elle peut être illégale. La cession doit être précise (durée, lieu, type de droit).",
                     "Art. L.131-3 CPI"
                 )
             else:
                 self.ajouter_resultat(
                     "VOUS êtes propriétaire",
                     "En l'absence de clause ou d'œuvre collective, le salarié reste propriétaire de ses textes, photos ou formations, même faits au travail.",
                     "L'employeur doit régulariser la situation et vous faire signer une cession s'il veut exploiter votre œuvre.",
                     "Art. L.111-1 CPI"
                 )

# ==============================
# EXÉCUTION GLOBALE DU SCRIPT
# ==============================

if __name__ == "__main__":
    try:
        # ÉTAPE 1 : Lancement bannière perso
        lancer_intro_banniere()

        # ÉTAPE 2 : Transition et lancement du formulaire
        app = FormulaireDroitsSalaries()
        app.demarrer()

    except KeyboardInterrupt:
        print(f"\n\n{COULEUR_CHOISIE}Programme interrompu. Au revoir !{REINITIALISATION}")

    except KeyboardInterrupt:

        print(f"\n\n{COULEUR_CHOISIE}Programme interrompu. Au revoir !{REINITIALISATION}")
