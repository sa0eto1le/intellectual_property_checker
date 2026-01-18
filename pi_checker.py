import time
import os
import random
import sys
import textwrap

# =======================
# CONFIGURATION & TEXTES
# =======================

# Palette couleurs
PALETTE_COULEURS = [
    (190, 166, 255),  # Violet
    (100, 204, 142),  # Vert
    (136, 189, 252),  # Bleu
]
rouge, vert, bleu = random.choice(PALETTE_COULEURS)
COULEUR_CHOISIE = f"\033[38;2;{rouge};{vert};{bleu}m"
REINITIALISATION = "\033[0m"

PHRASE = "per aspera, ad astra ✶"
NOM_SCRIPT = "INTELLECTUAL PROPERTY CHECKER (EXPERT V3)"

# Dictionnaire de traduction (FR / EN)
TEXTES = {
    "fr": {
        "titre_intro": "DIAGNOSTIC DE PROPRIÉTÉ INTELLECTUELLE AVANCÉ",
        "intro_desc": "Analyse de conformité L.111-1, L.131-3 (Formalisme) et L.113-9 CPI.",
        "intro_warning": "IMPORTANT : Résultat informatif. Ne remplace pas un avocat.",
        "q_langue": "Select Language / Choisissez la langue :",
        "opt_langue": ["Français", "English"],
        "invalid_choice": "Choix invalide / Invalid choice.",
        "analyse_cours": "Analyse des clauses et de la jurisprudence",
        "result_titre": "RAPPORT JURIDIQUE DÉTAILLÉ",
        "rec_titre": "💡 STRATÉGIE & LEVIERS :",
        "ref_titre": "⚖️ Fondement légal :",
        "moral_titre": "🛡️ NOTE SUR LES DROITS MORAUX :",
        "moral_desc": "Inaliénables et perpétuels. Même si vous avez tout cédé, vous conservez le droit au respect de votre nom (paternité) et de l'intégrité de l'œuvre (pas de modification dénaturante sans accord).",

        # Questions Communes
        "q_contrat_dispo": "Avez-vous votre contrat sous les yeux ?",
        "opt_contrat_dispo": ["Oui, je l'ai", "Non, je réponds de mémoire", "Je n'ai pas de contrat écrit"],

        "q_ia": "Utilisation d'IA générative (ChatGPT, Midjourney) ?",
        "opt_ia": ["Non, 100% humain", "Oui, aide mineure/instrumentale", "Oui, l'IA a généré l'essentiel"],

        "q_statut": "Statut contractuel :",
        "opt_statut": ["Salarié (Secteur Privé)", "Agent Public", "Stagiaire", "Journaliste", "Freelance / Indépendant"],

        "q_crea": "Typologie de l'œuvre :",
        "opt_crea": ["Logiciel / Code / BDD", "Invention (Brevetable)", "Design / Modèle", "Création Artistique / Littéraire / Graphique"],

        # Questions Expert L.131-3 (Clauses)
        "q_clause_gen": "Votre contrat contient-il une clause de cession de droits ?",
        "opt_clause_gen": ["Oui, une clause écrite", "Non, rien sur la PI", "Je ne sais pas"],

        "q_l1313_details": "La clause mentionne-t-elle PRÉCISÉMENT ces 3 éléments distincts ?",
        "l1313_list": "1. Étendue (Reproduction/Représentation)\n 2. Durée (ex: 'pour la durée légale' ou '10 ans')\n 3. Territoire (ex: 'Monde' ou 'France')",
        "opt_l1313": [
            "Oui, les 3 sont clairement définis",
            "C'est vague (ex: 'Tous droits cédés' sans détails)",
            "Il manque la durée ou le territoire",
            "Je ne suis pas sûr"
        ],

        "q_usage_reel": "L'employeur/client utilise-t-il DÉJÀ l'œuvre commercialement ?",
        "opt_usage_reel": [
            "Oui, c'est déjà public/vendu",
            "Non, c'est un projet interne ou futur",
            "Ils veulent l'utiliser mais je bloque"
        ],

        # Questions Spécifiques
        "q_soft_contexte": "Contexte de développement (Logiciel) :",
        "opt_soft_contexte": ["Mission pro / Instructions employeur", "Au bureau mais projet perso", "Chez moi / Matériel perso"],

        "q_inv_mission": "Mission inventive explicite (R&D) ?",
        "opt_inv_mission": ["Oui (Invention de mission)", "Non", "Pas de contrat"],

        # Résultats
        "res_ia_public": "DOMAINE PUBLIC (ABSENCE D'AUTEUR)",
        "exp_ia_public": "La jurisprudence refuse le droit d'auteur aux créations générées principalement par IA.",

        "res_l1313_ok": "CESSION VALIDE (FORMALISME RESPECTÉ)",
        "exp_l1313_ok": "La clause respecte le 'Triangle d'Or' de l'art. L.131-3. L'employeur détient les droits patrimoniaux dans les limites écrites.",

        "res_l1313_fail": "CESSION NULLE OU LIMITÉE (FAILLE L.131-3)",
        "exp_l1313_fail": "Une clause 'Tous droits cédés' est illégale en France. La cession doit être délimitée. En cas de litige, le juge peut annuler la cession : les droits reviennent à l'auteur.",
        "cons_l1313_fail": "C'est un levier de négociation majeur. Si l'œuvre est un succès, vous pouvez demander une régularisation financière.",

        "res_free_no_contract": "ABSENCE DE CESSION = CONTREFAÇON",
        "exp_free_no_contract": "Sans contrat écrit de cession (le devis ne suffit pas), vous restez propriétaire à 100%. L'utilisation par le client est techniquement une contrefaçon.",
        "cons_free_urgent": "URGENT : Proposez un contrat de cession maintenant. Vous êtes en position de force car le client exploite déjà l'œuvre illégalement.",
        "cons_free_prevent": "Ne bloquez pas brutalement si vous voulez garder le client, mais facturez la régularisation des droits.",

        "res_soft_auto": "DÉVOLUTION AUTOMATIQUE (L.113-9)",
        "exp_soft_auto": "Pour le logiciel, pas besoin de clause détaillée L.131-3. Les droits vont à l'employeur automatiquement si créé dans l'exercice des fonctions.",

        "res_moral_alert": "N'oubliez pas vos droits moraux : vous pouvez exiger que votre nom figure sur l'œuvre (Paternité).",
    },

    "en": {
        "titre_intro": "ADVANCED INTELLECTUAL PROPERTY DIAGNOSTIC",
        "intro_desc": "Compliance check for French IP Law (L.111-1, L.131-3 Formalism).",
        "intro_warning": "IMPORTANT: Informative result only. Not legal advice.",
        "q_langue": "Select Language / Choisissez la langue :",
        "opt_langue": ["Français", "English"],
        "invalid_choice": "Invalid choice.",
        "analyse_cours": "Analyzing clauses and case law",
        "result_titre": "DETAILED LEGAL REPORT",
        "rec_titre": "💡 STRATEGY & LEVERAGE:",
        "ref_titre": "⚖️ Legal Basis:",
        "moral_titre": "🛡️ NOTE ON MORAL RIGHTS:",
        "moral_desc": "Inalienable and perpetual. Even if you transferred all economic rights, you keep the right to credit (paternity) and integrity (no modification strictly forbidden).",

        "q_contrat_dispo": "Do you have your contract available?",
        "opt_contrat_dispo": ["Yes, in front of me", "No, answering from memory", "No written contract"],

        "q_ia": "Did you use Generative AI (ChatGPT, Midjourney)?",
        "opt_ia": ["No, 100% human", "Yes, minor aid", "Yes, AI generated most content"],

        "q_statut": "Status:",
        "opt_statut": ["Employee", "Public Servant", "Intern", "Journalist", "Freelance"],

        "q_crea": "Type of work:",
        "opt_crea": ["Software / Code", "Invention (Patent)", "Design", "Artistic / Literary / Graphic Work"],

        "q_clause_gen": "Is there an IP assignment clause in the contract?",
        "opt_clause_gen": ["Yes, written clause", "No, nothing on IP", "I don't know"],

        "q_l1313_details": "Does the clause PRECISELY mention these 3 distinct elements?",
        "l1313_list": "1. Scope (Reproduction/Representation)\n 2. Duration (e.g., 'legal duration' or '10 years')\n 3. Territory (e.g., 'World' or 'France')",
        "opt_l1313": [
            "Yes, all 3 are clearly defined",
            "It's vague (e.g., 'All rights transferred')",
            "Missing duration or territory",
            "Not sure"
        ],

        "q_usage_reel": "Is the employer/client ALREADY using the work commercially?",
        "opt_usage_reel": [
            "Yes, already public/sold",
            "No, internal/future project",
            "They want to, but I'm blocking"
        ],

        "q_soft_contexte": "Software context:",
        "opt_soft_contexte": ["Work mission", "Workplace / Personal project", "Home / Personal gear"],

        "q_inv_mission": "Explicit inventive mission?",
        "opt_inv_mission": ["Yes", "No", "No contract"],

        "res_ia_public": "PUBLIC DOMAIN (NO AUTHOR)",
        "exp_ia_public": "Case law denies copyright to AI-generated works without significant human input.",

        "res_l1313_ok": "VALID ASSIGNMENT",
        "exp_l1313_ok": "The clause respects Art. L.131-3 standards. Employer owns the rights within the written limits.",

        "res_l1313_fail": "VOID OR LIMITED ASSIGNMENT (L.131-3 FAILURE)",
        "exp_l1313_fail": "A 'transfer all rights' clause is void in France. Assignment must be specific. A judge could cancel the transfer, returning rights to you.",
        "cons_l1313_fail": "Major negotiation leverage. If the work is successful, you can ask for financial regularization.",

        "res_free_no_contract": "NO ASSIGNMENT = INFRINGEMENT",
        "exp_free_no_contract": "Without a written assignment contract (quote is not enough), you own 100%. Client use is technically infringement.",
        "cons_free_urgent": "URGENT: Propose an assignment contract now. You have leverage since the client is already using it illegally.",
        "cons_free_prevent": "Don't block aggressively if you want to keep the client, but bill for the rights assignment.",

        "res_soft_auto": "AUTOMATIC DEVOLUTION (L.113-9)",
        "exp_soft_auto": "Specific regime for software: rights go to the employer automatically if created during mission. No need for detailed L.131-3 clause.",

        "res_moral_alert": "Don't forget Moral Rights: you can claim credit/attribution for your work.",
    }
}

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

# ===========================
# PARTIE 2 : LE FORMULAIRE
# ===========================

class FormulaireDroitsSalaries:
    def __init__(self, lang="fr"):
        self.reponses = {}
        self.resultat = []
        self.width = 80
        self.lang = lang
        self.txt = TEXTES[lang]

    def t(self, key):
        return self.txt.get(key, f"MISSING KEY: {key}")

    def afficher_titre(self):
        print("\n" + self.t("titre_intro"))
        print(textwrap.fill(self.t("intro_desc"), width=self.width))
        print("-" * self.width)
        print(f"{COULEUR_CHOISIE}{self.t('intro_warning')}{REINITIALISATION}")
        print("="*self.width + "\n")

    def poser_question(self, cle, question_key, options_key, extra_info=""):
        question = self.t(question_key)
        options = self.t(options_key)

        print(f"\n {question}")
        if extra_info:
            print(f" \033[3m({extra_info})\033[0m") # Italique pour info

        for i, option in enumerate(options):
            print(f"   {i + 1}. {option}")

        while True:
            choix = input(f"\n   >>> (1-{len(options)}) : ")
            if choix.isdigit():
                idx = int(choix) - 1
                if 0 <= idx < len(options):
                    self.reponses[cle] = idx
                    return idx
            print(f"   /!\\ {self.t('invalid_choice')}")

    def animer_analyse(self):
        print(f"\n{self.t('analyse_cours')}", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")

    def ajouter_resultat_dict(self, titre_key, exp_key, cons_key="", ref="", moral=False):
        self.resultat.append({
            "titre": self.t(titre_key),
            "explication": self.t(exp_key),
            "conseil": self.t(cons_key) if cons_key else "",
            "ref": ref,
            "moral": moral
        })

    def afficher_rapport(self):
        print("\n" + "#"*self.width)
        print(f"{self.t('result_titre'):^{self.width}}")
        print("#"*self.width + "\n")

        moral_needed = False

        for res in self.resultat:
            print(f"{COULEUR_CHOISIE}RÉSULTAT : {res['titre'].upper()}{REINITIALISATION}")
            print("-" * 30)
            print(textwrap.fill(res['explication'], width=self.width))
            if res['conseil']:
                print(f"\n{self.t('rec_titre')}")
                print(textwrap.fill(res['conseil'], width=self.width))
            if res['ref']:
                print(f"\n{self.t('ref_titre')} {res['ref']}")
            if res['moral']:
                moral_needed = True
            print("\n" + "-"*self.width + "\n")

        if moral_needed:
            print(f"{self.t('moral_titre')}")
            print(textwrap.fill(self.t('moral_desc'), width=self.width))
            print("\n" + "="*self.width + "\n")

    # --- LOGIQUE MÉTIER ---

    def demarrer(self):
        self.afficher_titre()

        contrat_dispo = self.poser_question("contrat_ok", "q_contrat_dispo", "opt_contrat_dispo")

        # Filtre IA
        ia_usage = self.poser_question("ia_usage", "q_ia", "opt_ia")
        if ia_usage == 2:
            self.ajouter_resultat_dict("res_ia_public", "exp_ia_public", "", "Jurisprudence Thaler/DABUS")
            self.afficher_rapport()
            return

        statut = self.poser_question("statut", "q_statut", "opt_statut")
        type_crea = self.poser_question("type_crea", "q_crea", "opt_crea")

        self.animer_analyse()

        if statut == 4: # Freelance
            self.traiter_freelance(type_crea, contrat_dispo)
        elif type_crea == 0: # Logiciel
            self.traiter_logiciel(statut)
        elif type_crea == 1: # Invention
            self.traiter_invention(statut)
        else: # Art / Texte / Design
            self.traiter_oeuvre_classique(statut, contrat_dispo)

        self.afficher_rapport()

    # --- SCÉNARIOS AVANCÉS ---

    def traiter_freelance(self, type_crea, contrat_dispo):
        # 1. Vérification de la clause
        clause = self.poser_question("clause", "q_clause_gen", "opt_clause_gen")

        usage = self.poser_question("usage", "q_usage_reel", "opt_usage_reel")
        conflit_potentiel = (usage == 0) # Si usage public déjà en cours

        if clause == 1 or clause == 2: # Non ou ne sait pas
            if conflit_potentiel:
                # DANGER ET OPPORTUNITÉ : Client utilise sans droit
                self.ajouter_resultat_dict("res_free_no_contract", "exp_free_no_contract", "cons_free_urgent", "L.111-1", moral=True)
            else:
                self.ajouter_resultat_dict("res_free_no_contract", "exp_free_no_contract", "cons_free_prevent", "L.111-1", moral=True)

        else: # Clause existante, vérification des détails (L.131-3)
            if type_crea == 0: # Logiciel Freelance
                # L.131-3 moins strict pour logiciel, mais il faut une cession écrite quand même
                self.ajouter_resultat_dict("res_l1313_ok", "exp_l1313_ok", "", "Code Civil / CPI", moral=False)
            else:
                # Check Formalisme
                details = self.poser_question("details", "q_l1313_details", "opt_l1313", extra_info=self.t("l1313_list"))

                if details == 0: # Tout est bon
                    self.ajouter_resultat_dict("res_l1313_ok", "exp_l1313_ok", "", "L.131-3", moral=True)
                else: # Clause vague ou incomplète
                    self.ajouter_resultat_dict("res_l1313_fail", "exp_l1313_fail", "cons_l1313_fail", "L.131-3", moral=True)

    def traiter_oeuvre_classique(self, statut, contrat_dispo):
        # Pour Salariés (Design, Art, Texte)

        # Check usage employeur
        usage = self.poser_question("usage", "q_usage_reel", "opt_usage_reel")

        if contrat_dispo == 2: # Pas de contrat écrit
             self.ajouter_resultat_dict("res_free_no_contract", "exp_free_no_contract", "cons_free_urgent", "L.111-1", moral=True)
             return

        clause = self.poser_question("clause", "q_clause_gen", "opt_clause_gen")

        if clause == 0: # Clause présente
            # Vérification Triangle d'or L.131-3
            details = self.poser_question("details", "q_l1313_details", "opt_l1313", extra_info=self.t("l1313_list"))

            if details == 0:
                self.ajouter_resultat_dict("res_l1313_ok", "exp_l1313_ok", "", "L.131-3", moral=True)
            else:
                self.ajouter_resultat_dict("res_l1313_fail", "exp_l1313_fail", "cons_l1313_fail", "Nullité Relative L.131-3", moral=True)
        else:
             # Pas de clause = Salarié propriétaire (sauf Art Appliqué parfois discuté, mais règle de base L111-1)
             self.ajouter_resultat_dict("res_free_no_contract", "exp_free_no_contract", "cons_free_prevent", "L.111-1", moral=True)

    def traiter_logiciel(self, statut):
        contexte = self.poser_question("soft_contexte", "q_soft_contexte", "opt_soft_contexte")
        if contexte == 0:
            self.ajouter_resultat_dict("res_soft_auto", "exp_soft_auto", "", "L.113-9", moral=False)
        else:
            self.ajouter_resultat_dict("res_free_no_contract", "exp_free_no_contract", "", "L.111-1", moral=False)

    def traiter_invention(self, statut):
        mission = self.poser_question("inv_mission", "q_inv_mission", "opt_inv_mission")
        if mission == 0:
             self.ajouter_resultat_dict("res_l1313_ok", "exp_soft_auto", "Rémunération supp obligatoire", "L.611-7", moral=True) # Moral = Droit au nom d'inventeur
        else:
             self.ajouter_resultat_dict("res_free_no_contract", "exp_free_no_contract", "", "L.611-7", moral=True)

# ==============================
# EXÉCUTION
# ==============================

def choisir_langue():
    print(TEXTES['fr']['q_langue'])
    print("1. Français")
    print("2. English")
    while True:
        c = input(">>> ")
        if c == "1": return "fr"
        if c == "2": return "en"

if __name__ == "__main__":
    try:
        lancer_intro_banniere()
        time.sleep(1)
        afficher_en_tete(NOM_SCRIPT)

        langue_choisie = choisir_langue()
        app = FormulaireDroitsSalaries(lang=langue_choisie)
        app.demarrer()

    except KeyboardInterrupt:
        print(f"\n\n{COULEUR_CHOISIE}Programme interrompu. Au revoir ! {REINITIALISATION}")

