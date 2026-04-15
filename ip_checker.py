#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Intellectual Property Checker
Outil interactif en ligne de commande permettant à tout salarié, alternant,
stagiaire, agent public ou freelance de comprendre sa situation en matière
de droits de propriété intellectuelle sur ses créations professionnelles.
Ce projet a été inspiré et assisté avec l'aide d'outils d'intelligence artificielle
pour la rédaction du code.

Auteur : sa0

Licence : MIT
"""

import time
import os
import random
import sys
import textwrap
from datetime import datetime


# =========================
# PALETTE & COULEURS
# =========================

def _supports_truecolor():
    """
    Détecte si le terminal supporte les couleurs 24-bit (true color).
    Vérifie COLORTERM, TERM_PROGRAM et le flag NO_COLOR.
    Compatible macOS, Linux, Windows Terminal.
    """
    if not sys.stdout.isatty():
        return False
    if os.environ.get("NO_COLOR"):
        return False
    colorterm = os.environ.get("COLORTERM", "").lower()
    if colorterm in ("truecolor", "24bit"):
        return True
    term_program = os.environ.get("TERM_PROGRAM", "").lower()
    if term_program in ("iterm.app", "hyper", "vscode", "warp"):
        return True
    term = os.environ.get("TERM", "").lower()
    if "256color" in term or "truecolor" in term:
        return True
    return False


def _rgb_to_256(r, g, b):
    """
    Convertit une couleur RGB en code ANSI 256 couleurs (meilleur fallback).
    Utilise la grille 6x6x6 (codes 16-231) de la palette xterm-256.
    """
    ri = round(r / 255 * 5)
    gi = round(g / 255 * 5)
    bi = round(b / 255 * 5)
    code = 16 + 36 * ri + 6 * gi + bi
    return f"\033[38;5;{code}m"


# Palette RGB — trois options de couleur
PALETTE_COULEURS = [
    (190, 166, 255),   # Violet pastel
    (100, 204, 142),   # Vert menthe
    (136, 189, 252),   # Bleu ciel
]

_r, _g, _b = random.choice(PALETTE_COULEURS)

if not sys.stdout.isatty():
    # Pas de terminal interactif — pas de couleur du tout
    COULEUR_CHOISIE = ""
    REINITIALISATION = ""
    GRAS = ""
elif _supports_truecolor():
    # Terminal 24-bit — couleur exacte
    COULEUR_CHOISIE = f"\033[38;2;{_r};{_g};{_b}m"
    REINITIALISATION = "\033[0m"
    GRAS = "\033[1m"
else:
    # Fallback ANSI 256 — compatible Terminal.app macOS, xterm, etc.
    COULEUR_CHOISIE = _rgb_to_256(_r, _g, _b)
    REINITIALISATION = "\033[0m"
    GRAS = "\033[1m"

PHRASE = "per aspera, ad astra ✶"
NOM_SCRIPT = "INTELLECTUAL PROPERTY CHECKER"


# =========================
# BANNIÈRE ASCII
# =========================

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
⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣷⣄⠀⠀⠀⢀⣠⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⠤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⣀⣀
⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢷⣶⣶⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠒
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈"
""".splitlines()


# =========================
# UTILITAIRES
# =========================

WIDTH = 80
resultats_log = []  # Stockage pour export


def wrap(txt):
    return textwrap.fill(txt, WIDTH)


def pause(d=0.3):
    time.sleep(d)


def effacer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')


def afficher_banniere(progression=None):
    hauteur = max(len(logo_gauche), len(logo_droite))
    lg = [""] * ((hauteur - len(logo_gauche)) // 2) + logo_gauche
    ld = [""] * ((hauteur - len(logo_droite)) // 2) + logo_droite
    for g, d in zip(lg, ld):
        ligne = g[:progression].ljust(30) + d if progression else g.ljust(30) + d
        print(COULEUR_CHOISIE + ligne + REINITIALISATION)


def afficher_en_tete(nom):
    print(COULEUR_CHOISIE + "=" * WIDTH + REINITIALISATION)
    print(COULEUR_CHOISIE + GRAS + nom.center(WIDTH) + REINITIALISATION)
    print(COULEUR_CHOISIE + "=" * WIDTH + REINITIALISATION)
    print()


def executer_animation_intro():
    for _ in range(12):
        effacer_ecran()
        print(COULEUR_CHOISIE + PHRASE.center(WIDTH) + REINITIALISATION)
        time.sleep(0.08)
        effacer_ecran()
        time.sleep(0.08)
    largeur = max(len(l) for l in logo_gauche)
    for p in range(1, largeur + 1):
        effacer_ecran()
        afficher_banniere(p)
        time.sleep(0.04)
    effacer_ecran()
    afficher_banniere()


def separateur(titre=None):
    print()
    print(COULEUR_CHOISIE + "─" * WIDTH + REINITIALISATION)
    if titre:
        print(COULEUR_CHOISIE + titre.center(WIDTH) + REINITIALISATION)
        print(COULEUR_CHOISIE + "─" * WIDTH + REINITIALISATION)


def ask(question, options):
    print("\n" + wrap(question))
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        r = input("\n>>> ").strip()
        if r.isdigit() and 1 <= int(r) <= len(options):
            choix = int(r)
            resultats_log.append(f"Q: {question}")
            resultats_log.append(f"R: {options[choix - 1]}")
            resultats_log.append("")
            return choix
        print("  Réponse invalide — entre un numéro entre 1 et " + str(len(options)) + ".")


def afficher_resultat(niveau, titre, texte):
    print(f"\n{niveau}  {GRAS}{titre}{REINITIALISATION}")
    print(wrap(texte))
    resultats_log.append(f"[RÉSULTAT] {niveau} {titre}")
    resultats_log.append(wrap(texte))
    resultats_log.append("")


def afficher_article(ref, texte):
    print(f"\n  {COULEUR_CHOISIE} {ref}{REINITIALISATION}")
    lignes = textwrap.wrap(texte, WIDTH - 4)
    for l in lignes:
        print("     " + l)
    resultats_log.append(f"  [Réf.] {ref} — {texte}")
    resultats_log.append("")


def afficher_alerte(texte):
    print("\n" + wrap(texte))
    resultats_log.append(f"[ALERTE] {texte}")
    resultats_log.append("")


def exporter_resultats():
    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_fichier = f"ip_checker_resultat_{horodatage}.txt"
    try:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write("=" * WIDTH + "\n")
            f.write(NOM_SCRIPT.center(WIDTH) + "\n")
            f.write(f"Diagnostic du {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n".center(WIDTH))
            f.write("=" * WIDTH + "\n\n")
            f.write("Outil d'orientation uniquement — pas un avis juridique.\n\n")
            f.write("─" * WIDTH + "\n\n")
            for ligne in resultats_log:
                f.write(ligne + "\n")
            f.write("\n" + "─" * WIDTH + "\n")
            f.write("Pour une analyse personnalisée, consulte un professionnel du droit.\n")
        print(f"\n   Résultats exportés : {nom_fichier}")
    except Exception as e:
        print(f"\n   Export impossible : {e}")


# =========================
# PROGRAMME PRINCIPAL
# =========================

try:
    executer_animation_intro()
    pause(0.8)
    afficher_en_tete(NOM_SCRIPT)

    print(wrap(
        "Ce questionnaire t'aide à comprendre qui détient les droits sur une création "
        "réalisée pendant, autour ou à côté de ton activité professionnelle."
    ))
    print()
    print(wrap(
        "Il couvre le droit d'auteur (œuvres, logiciels), le droit des brevets (inventions) "
        "et les bases de données. Il prend en compte ton statut, le contexte de création, "
        "les clauses contractuelles et l'utilisation actuelle de ta création."
    ))
    print()
    print(COULEUR_CHOISIE + "  Outil d'orientation — pas un avis juridique." + REINITIALISATION)


    # =============================================================
    # BLOC 1 — STATUT
    # =============================================================
    separateur("1 / 8  —  TON STATUT")

    statut = ask(
        "Quel est ton statut principal ?",
        [
            "Salarié(e)  —  CDI, CDD ou autre contrat de travail",
            "Alternant(e)  —  apprentissage ou contrat de professionnalisation",
            "Stagiaire  —  convention de stage",
            "Agent(e) public(que)  —  fonctionnaire ou contractuel public",
            "Travailleur(euse) indépendant(e)  —  freelance / auto-entrepreneur(euse)"
        ]
    )


    # =============================================================
    # BLOC 2 — TYPE DE CRÉATION
    # =============================================================
    separateur("2 / 8  —  TA CRÉATION")

    creation = ask(
        "Ta création correspond principalement à :",
        [
            "Code / logiciel / script / application / algorithme",
            "Texte, visuel, vidéo, design, musique, contenu éditorial",
            "Invention technique, procédé ou dispositif potentiellement brevetable",
            "Base de données ou compilation structurée d'informations",
            "Plusieurs catégories mélangées",
            "Je ne sais pas bien comment la qualifier"
        ]
    )


    # =============================================================
    # BLOC 3 — INTELLIGENCE ARTIFICIELLE
    # =============================================================
    separateur("3 / 8  —  RÔLE DE L'INTELLIGENCE ARTIFICIELLE")

    ia = ask(
        "Une intelligence artificielle a-t-elle contribué à cette création ?",
        [
            "Non, la création est entièrement humaine",
            "Oui, comme outil d'assistance  —  suggestions, corrections, aide ponctuelle. "
            "L'essentiel de la conception et des choix vient de moi.",
            "Oui, contribution significative  —  mais j'ai guidé, orienté, sélectionné et structuré.",
            "Oui, elle a produit l'essentiel  —  mon apport personnel est limité."
        ]
    )

    # Sortie anticipée si IA a tout produit
    if ia == 4:
        separateur("RÉSULTAT")
        afficher_resultat(
            "⚪", "PROTECTION TRÈS INCERTAINE  —  RÔLE DOMINANT DE L'IA",
            "Lorsqu'une intelligence artificielle a produit l'essentiel d'une création, "
            "la protection par le droit d'auteur est aujourd'hui très incertaine en droit "
            "français et européen. Le droit d'auteur protège les créations de l'esprit qui "
            "reflètent la personnalité de leur auteur humain (art. L111-1 CPI). "
            "Sans contribution humaine originale clairement identifiable, il sera difficile "
            "de revendiquer une protection solide."
        )
        afficher_article(
            "Art. L111-1 CPI",
            "L'auteur d'une œuvre de l'esprit jouit sur cette œuvre, du seul fait de sa création, "
            "d'un droit de propriété incorporelle exclusif et opposable à tous."
        )
        print()
        print(wrap(
            "💡 Ce que tu peux faire : documente précisément ta contribution créative — "
            "les choix esthétiques ou techniques que tu as faits, les itérations, "
            "la sélection et l'assemblage des éléments générés. "
            "La jurisprudence sur ce point est encore en construction. "
            "Si la création a une valeur économique, un avis juridique individualisé est recommandé."
        ))
        separateur()
        export = ask("Veux-tu exporter ce diagnostic dans un fichier texte ?", ["Oui", "Non"])
        if export == 1:
            exporter_resultats()
        print("\n" + "=" * WIDTH)
        print("FIN DU DIAGNOSTIC".center(WIDTH))
        print("=" * WIDTH)
        print(wrap("Outil d'orientation — pas un avis juridique."))
        sys.exit()


    # =============================================================
    # BLOC 4 — CONTEXTE DE CRÉATION
    # =============================================================
    separateur("4 / 8  —  CONTEXTE DE CRÉATION")

    origine = ask(
        "Cette création vient :",
        [
            "D'une demande explicite et directe de l'entreprise ou du client",
            "D'une initiative personnelle encouragée ou activement soutenue par l'entreprise",
            "D'une initiative personnelle tolérée, mais sans demande de l'entreprise",
            "Entièrement de toi, sans lien avec ton activité professionnelle"
        ]
    )

    temps = ask(
        "Tu as travaillé dessus :",
        [
            "Uniquement pendant tes heures de travail / stage / alternance",
            "Un mélange : heures de travail et temps personnel",
            "Uniquement en dehors de tes heures de travail"
        ]
    )

    materiel = ask(
        "Avec quels équipements et ressources ?",
        [
            "Uniquement ceux de l'entreprise ou de l'organisme",
            "Un mélange de ressources professionnelles et personnelles",
            "Uniquement les miens"
        ]
    )


    # =============================================================
    # BLOC 5 — QUESTIONS SPÉCIFIQUES AU STATUT
    # =============================================================
    separateur("5 / 8  —  QUESTIONS LIÉES À TON STATUT")

    cadre_alt = None
    clause_stage = None
    type_admin = None
    mission_inventive = None

    if statut == 2:  # Alternant
        cadre_alt = ask(
            "Ce projet a été demandé par :",
            [
                "L'entreprise, dans le cadre de ta mission",
                "L'école ou le centre de formation (projet académique)",
                "Les deux simultanément  —  projet commun école-entreprise",
                "Toi seul(e), sans lien défini avec ta mission ou tes cours"
            ]
        )

    elif statut == 3:  # Stagiaire
        clause_stage = ask(
            "Ta convention de stage mentionne-t-elle la propriété intellectuelle ?",
            [
                "Oui, avec une clause claire (droits cédés, durée et territoire précisés)",
                "Oui, mais la rédaction est vague ou très générale",
                "Non, rien sur ce sujet dans la convention",
                "Je ne sais pas, je n'ai pas relu la convention"
            ]
        )

    elif statut == 4:  # Agent public
        type_admin = ask(
            "Ton activité principale relève de :",
            [
                "Administration générale  —  ministère, collectivité, établissement public classique",
                "Recherche publique ou enseignement supérieur",
                "Organisme public à vocation industrielle ou commerciale  —  EPIC, etc.",
                "Je ne sais pas exactement"
            ]
        )

    # Chemin inventions : question sur la mission inventive
    if creation == 3 and statut in [1, 2, 4]:
        mission_inventive = ask(
            "Cette invention a été développée :",
            [
                "Dans le cadre d'une mission inventive explicite  —  "
                "la recherche ou le développement figure dans ta fiche de poste",
                "Hors de ta mission stricte, mais en utilisant des connaissances "
                "ou des moyens de l'entreprise",
                "Totalement hors de ta mission et sans lien avec tes fonctions, "
                "sur ton temps et tes ressources personnels"
            ]
        )


    # =============================================================
    # BLOC 6 — CONTRAT ET CLAUSES
    # =============================================================
    separateur("6 / 8  —  CONTRAT ET CLAUSES")

    contrat = ask(
        "Tu as un contrat de travail ou une convention écrite ?",
        [
            "Oui, je peux le consulter",
            "Oui, mais je réponds de mémoire",
            "Non, rien d'écrit"
        ]
    )

    if contrat in [1, 2]:
        clause = ask(
            "Ce document contient-il une clause sur la propriété intellectuelle ?",
            [
                "Oui, rédigée en détail",
                "Oui, mais la rédaction est générale ou vague",
                "Non, aucune clause sur ce sujet",
                "Je ne sais pas"
            ]
        )
    else:
        clause = 3  # Pas de contrat = pas de clause

    details = None
    if clause == 1:
        details = ask(
            "Cette clause précise-t-elle tous ces éléments : "
            "œuvres visées, droits cédés, durée, territoire, types d'exploitation ?",
            [
                "Oui, tout est clairement détaillé",
                "Certains éléments sont présents, d'autres manquent",
                "C'est rédigé de manière très générale",
                "Je ne sais pas exactement"
            ]
        )


    # =============================================================
    # BLOC 7 — UTILISATION ACTUELLE
    # =============================================================
    separateur("7 / 8  —  UTILISATION PAR L'ENTREPRISE")

    usage = ask(
        "L'entreprise ou l'organisme utilise-t-il ta création ?",
        [
            "Oui, publiquement  —  site, produit, communication, commercialisation",
            "Oui, uniquement en interne",
            "Pas encore, mais elle envisage de le faire",
            "Non, pas à ma connaissance"
        ]
    )

    nom = ask(
        "Ton nom ou pseudonyme est-il mentionné comme auteur ou créateur ?",
        [
            "Oui, systématiquement",
            "Parfois ou de manière incomplète",
            "Non, jamais"
        ]
    )

    accord = None
    if usage in [1, 2]:
        accord = ask(
            "As-tu donné ton accord pour cette utilisation ?",
            [
                "Oui, par écrit  —  contrat, avenant ou mail",
                "Oui, oralement ou de manière implicite",
                "Non, l'entreprise utilise ma création sans que j'aie formellement accepté"
            ]
        )


    # =============================================================
    # BLOC 8 — VALEUR ÉCONOMIQUE
    # =============================================================
    separateur("8 / 8  —  VALEUR ET ENJEUX")

    valeur = ask(
        "Cette création a-t-elle une valeur économique identifiable ?",
        [
            "Oui, elle génère ou peut générer des revenus directement",
            "Oui, elle sert à vendre ou à promouvoir  —  valeur indirecte",
            "Valeur stratégique ou interne  —  gain de temps, avantage concurrentiel",
            "Faible ou difficile à estimer",
            "Aucune valeur économique apparente"
        ]
    )

    pause(0.5)


    # =============================================================
    # ANALYSE
    # =============================================================
    separateur("ANALYSE DE TA SITUATION")
    pause(0.4)


    # ------ CAS INVENTION / BREVET ------
    if creation == 3:
        print()
        print(wrap(
            "⚠️  Ta création correspond à une invention technique potentiellement brevetable. "
            "Ce régime est fondamentalement différent du droit d'auteur : "
            "c'est le droit des brevets qui s'applique (art. L611-1 et s. CPI)."
        ))
        afficher_article(
            "Art. L611-7 CPI  —  Inventions de salariés",
            "Les inventions appartiennent à l'employeur si elles sont réalisées dans l'exécution "
            "d'une mission inventive confiée au salarié (inventions de mission). "
            "Pour les inventions hors mission réalisées avec des moyens de l'entreprise, "
            "l'employeur dispose d'un droit d'attribution contre juste prix. "
            "Pour les inventions totalement hors mission et sans moyens de l'entreprise, "
            "le salarié conserve tous ses droits mais doit en informer l'employeur."
        )
        if mission_inventive == 1:
            afficher_resultat(
                "🔴", "INVENTION DE MISSION  —  DROITS À L'EMPLOYEUR",
                "L'invention relève d'une mission inventive explicite confiée par l'employeur. "
                "Elle lui appartient de plein droit dès sa réalisation. "
                "Le salarié a néanmoins droit à une rémunération supplémentaire, "
                "dont les modalités doivent être prévues par accord collectif ou contrat individuel."
            )
        elif mission_inventive == 2:
            afficher_resultat(
                "🟡", "INVENTION HORS MISSION CONNEXE  —  DROIT D'ATTRIBUTION",
                "L'invention a été développée hors mission stricte, mais avec des moyens "
                "ou des connaissances de l'entreprise. "
                "L'employeur peut se faire attribuer la propriété ou la jouissance de l'invention "
                "contre versement d'un juste prix, à condition d'en informer le salarié "
                "dans les délais légaux. "
                "Tu as l'obligation de déclarer l'invention à l'employeur par écrit."
            )
        elif mission_inventive == 3:
            afficher_resultat(
                "🟢", "INVENTION HORS MISSION  —  DROITS AU SALARIÉ",
                "L'invention est totalement étrangère à tes fonctions et réalisée "
                "sans moyens de l'entreprise. Elle t'appartient. "
                "Tu dois néanmoins en informer l'employeur par écrit pour établir clairement "
                "le caractère hors-mission et éviter tout litige ultérieur."
            )
        else:
            afficher_resultat(
                "🟡", "INVENTION  —  QUALIFICATION À PRÉCISER",
                "Le régime exact dépend de la qualification de l'invention : "
                "mission inventive, hors mission connexe, ou hors mission totale. "
                "Une analyse au cas par cas est nécessaire."
            )
        if statut == 5:  # Freelance
            afficher_resultat(
                "🟡", "FREELANCE  —  DROIT DES BREVETS ET CONTRAT",
                "Pour un freelance, les droits sur une invention dépendent intégralement "
                "du contrat. En l'absence de clause de cession ou de licence précise, "
                "tu restes titulaire de l'invention. "
                "Une cession de brevet doit être faite par écrit et inscrite au registre national "
                "des brevets pour être opposable aux tiers (art. L613-8 CPI)."
            )


    # ------ CAS BASE DE DONNÉES ------
    elif creation == 4:
        afficher_resultat(
            "🟡", "BASE DE DONNÉES  —  DOUBLE RÉGIME POSSIBLE",
            "Les bases de données peuvent relever d'une double protection : le droit "
            "d'auteur si le choix ou la disposition des matières est original, et le "
            "droit sui generis du producteur si la constitution, la vérification ou la "
            "présentation du contenu atteste d'un investissement financier, matériel ou "
            "humain substantiel (art. L341-1 CPI). Le producteur n'est pas simplement "
            "celui qui finance : c'est la personne qui prend l'initiative et le risque "
            "des investissements correspondants. En pratique, dans un cadre professionnel, "
            "il s'agit souvent de l'employeur, de l'organisme ou du client porteur du "
            "projet, mais il faut l'identifier concrètement. La structure originale de "
            "la base peut, elle, rester protégée par le droit d'auteur selon les règles "
            "applicables à ton statut."
        )
        afficher_article(
            "Art. L341-1 CPI  —  Droit sui generis",
            "Le producteur d'une base de données bénéficie d'une protection du contenu "
            "lorsque la constitution, la vérification ou la présentation de ce contenu "
            "atteste d'un investissement financier, matériel ou humain substantiel."
        )


    # ------ CAS LOGICIEL ------
    elif creation == 1:

        if statut == 1:  # Salarié
            if origine == 1 and temps in [1, 2] and materiel in [1, 2]:
                afficher_resultat(
                    "🔴", "LOGICIEL SALARIÉ  —  DROITS PATRIMONIAUX À L'EMPLOYEUR",
                    "Le logiciel a été créé dans l'exercice de tes fonctions et/ou d'après "
                    "les instructions de l'employeur. L'article L113-9 CPI prévoit alors, "
                    "sauf dispositions statutaires ou stipulations contraires, la dévolution "
                    "à l'employeur des droits patrimoniaux sur le logiciel et sa documentation. "
                    "Attention : pour les logiciels, le droit moral de l'auteur existe mais il "
                    "est légalement aménagé. Sauf stipulation plus favorable, l'auteur ne peut "
                    "pas s'opposer à certaines modifications non préjudiciables à son honneur "
                    "ou à sa réputation, ni exercer le droit de repentir ou de retrait."
                )
                afficher_article(
                    "Art. L113-9 CPI",
                    "Sauf dispositions statutaires ou stipulations contraires, les droits "
                    "patrimoniaux sur les logiciels créés par un ou plusieurs employés dans "
                    "l'exercice de leurs fonctions ou d'après les instructions de leur employeur "
                    "sont dévolus à l'employeur qui est seul habilité à les exercer."
                )
            elif origine in [3, 4] and temps == 3 and materiel == 3:
                afficher_resultat(
                    "🟢", "LOGICIEL  —  INITIATIVE PERSONNELLE HORS MISSION",
                    "Le fait d'avoir développé le logiciel sur ton temps personnel et avec "
                    "tes propres moyens est un élément favorable, mais ce n'est pas décisif "
                    "à lui seul. Le point central est de savoir si le logiciel a été créé "
                    "dans l'exercice de tes fonctions ou d'après les instructions de "
                    "l'employeur au sens de l'article L113-9 CPI. Si la création est "
                    "réellement étrangère à tes missions et à toute instruction reçue, "
                    "tu restes en principe titulaire des droits patrimoniaux. Vérifie aussi "
                    "les clauses de confidentialité, de non-concurrence et l'éventuel lien "
                    "fonctionnel entre le logiciel et ton poste."
                )
            else:
                afficher_resultat(
                    "🟡", "LOGICIEL SALARIÉ  —  SITUATION MIXTE",
                    "Certains éléments rattachent le logiciel à tes fonctions, d'autres "
                    "suggèrent une initiative plus personnelle. L'enjeu central est donc de "
                    "savoir si le logiciel a été créé dans l'exercice de tes fonctions ou "
                    "d'après les instructions de l'employeur au sens de l'article L113-9 CPI. "
                    "Le temps de création et le matériel utilisé sont des indices utiles, "
                    "mais non décisifs à eux seuls. Une analyse concrète des missions confiées, "
                    "des instructions reçues et de l'objet du logiciel est nécessaire."
                )

        elif statut == 2:  # Alternant
            if cadre_alt == 1:
                afficher_resultat(
                    "🔴", "LOGICIEL ALTERNANT  —  DROITS PROCHES DU SALARIÉ",
                    "L'alternant est soumis au même régime que le salarié pour les créations "
                    "réalisées dans le cadre de sa mission. Les droits patrimoniaux sur le logiciel "
                    "appartiennent probablement à l'entreprise si la création a été faite dans "
                    "l'exercice des fonctions ou sur instruction de l'employeur (art. L113-9 CPI)."
                )
            elif cadre_alt in [2, 3]:
                afficher_resultat(
                    "🟡", "LOGICIEL ALTERNANT  —  PROJET ACADÉMIQUE OU MIXTE",
                    "Le logiciel a été créé dans un cadre lié à l'école ou mixte école-entreprise. "
                    "Ni l'entreprise ni l'école n'ont automatiquement tous les droits. "
                    "Examine les clauses du contrat d'alternance, de la convention de formation "
                    "et le règlement de l'établissement sur la PI des travaux étudiants."
                )
            else:
                afficher_resultat(
                    "🟢", "LOGICIEL ALTERNANT  —  INITIATIVE PERSONNELLE",
                    "Créé sur ta seule initiative, hors mission et hors projet académique. "
                    "En l'absence de clause explicitement applicable à cette situation, "
                    "tu restes probablement titulaire de tes droits. "
                    "Vérifie néanmoins ton contrat d'alternance."
                )

        elif statut == 3:  # Stagiaire
            if clause_stage == 1:
                afficher_resultat(
                    "🟡", "LOGICIEL STAGIAIRE  —  CLAUSE DE CESSION À ANALYSER",
                    "La convention contient une clause précise. Vérifie qu'elle couvre bien "
                    "le type de logiciel créé, les usages prévus, la durée et le territoire. "
                    "En principe, il n'existe pas pour le stagiaire de dévolution automatique "
                    "comparable à celle du salarié. Attention toutefois : l'article L113-9-1 CPI "
                    "prévoit un régime spécial pour certaines personnes non salariées accueillies "
                    "par convention dans une structure, publique ou privée, réalisant de la "
                    "recherche. Si ton stage se déroule dans un laboratoire, un établissement de "
                    "recherche ou une structure R&D, ce point doit être vérifié."
                )
            elif clause_stage == 2:
                afficher_resultat(
                    "🟡", "LOGICIEL STAGIAIRE  —  CLAUSE FLOUE",
                    "La convention contient une clause, mais sa rédaction est vague. En droit "
                    "d'auteur, une transmission de droits doit être constatée par écrit et "
                    "précisément délimitée. Une clause trop générale risque de ne pas couvrir "
                    "l'exploitation souhaitée. Tu conserves potentiellement des droits sur ce "
                    "qui n'est pas clairement cédé. Attention toutefois : si le stage se déroule "
                    "dans une structure, publique ou privée, réalisant de la recherche, l'article "
                    "L113-9-1 CPI peut, sous conditions, dévoluer les droits patrimoniaux sur le "
                    "logiciel à la structure d'accueil."
                )
            else:
                afficher_resultat(
                    "🟢", "LOGICIEL STAGIAIRE  —  TITULAIRE EN PRINCIPE",
                    "Aucune clause identifiable. En principe, il n'existe pas de transfert "
                    "automatique des droits patrimoniaux sur un logiciel créé par un stagiaire "
                    "du seul fait du stage, et tu restes donc en principe titulaire de tes droits. "
                    "Important : depuis l'article L113-9-1 CPI, certaines personnes non salariées "
                    "accueillies par convention dans une structure, publique ou privée, réalisant "
                    "de la recherche peuvent voir leurs droits patrimoniaux dévolus à la structure "
                    "d'accueil si les conditions légales sont réunies. Si ton stage se déroule "
                    "dans un laboratoire, un établissement de recherche ou une structure R&D, "
                    "ce point doit être vérifié avant de conclure."
                )

        elif statut == 4:  # Agent public
            afficher_resultat(
                "🟡", "LOGICIEL AGENT PUBLIC  —  RÉGIME SPÉCIFIQUE",
                "Pour un agent public, il faut éviter de raisonner comme s'il existait une "
                "cession générale et illimitée au profit de la personne publique. Lorsque "
                "l'œuvre est créée dans l'exercice des fonctions ou d'après les instructions "
                "reçues, la personne publique bénéficie d'un droit d'exploitation de plein droit "
                "seulement dans la mesure strictement nécessaire à l'accomplissement de la mission "
                "de service public. Pour l'exploitation commerciale, elle ne dispose en principe "
                "que d'un droit de préférence. En outre, ce régime spécial ne s'applique pas aux "
                "agents dont la divulgation n'est soumise à aucun contrôle hiérarchique préalable. "
                "Pour les logiciels, il faut aussi garder à l'esprit que le droit moral de l'auteur "
                "est légalement aménagé. Le détail dépend donc fortement du statut exact, de "
                "l'organisme et des conditions de création."
            )
            afficher_article(
                "Art. L111-1, L121-7, L131-3-1 et L131-3-2 CPI",
                "Le principe reste que l'auteur conserve son droit, sous réserve des exceptions "
                "prévues par le code. Pour certains agents publics, la personne publique ne reçoit "
                "de plein droit qu'un droit d'exploitation limité à ce qui est strictement "
                "nécessaire à la mission de service public, et ne dispose en principe, pour "
                "l'exploitation commerciale, que d'un droit de préférence."
            )

        elif statut == 5:  # Freelance
            if clause in [3, 4]:
                afficher_resultat(
                    "🟢", "LOGICIEL FREELANCE  —  TITULAIRE  —  PAS DE CESSION",
                    "Aucune clause de cession identifiable. "
                    "En droit d'auteur, une transmission de droits doit être constatée par écrit "
                    "(art. L131-2 CPI) et précisément délimitée quant aux droits cédés et au domaine "
                    "d'exploitation (art. L131-3 CPI). Sans clause précise, "
                    "tu restes titulaire de tous tes droits. "
                    "En l'absence de cession claire, le client ne peut pas se prévaloir d'un "
                    "transfert général des droits. Il peut au mieux soutenir l'existence de droits "
                    "d'usage limités à la finalité convenue, dont l'étendue exacte dépendra du "
                    "contrat, des échanges et des circonstances."
                )
            elif clause == 1 and details == 1:
                afficher_resultat(
                    "🔴", "LOGICIEL FREELANCE  —  DROITS CÉDÉS  —  CONTRAT PRÉCIS",
                    "Le contrat prévoit une cession clairement rédigée. "
                    "Le client peut exploiter le logiciel dans les limites définies. "
                    "Tu conserves tes droits moraux et tout ce qui n'a pas été expressément cédé."
                )
            else:
                afficher_resultat(
                    "🟡", "LOGICIEL FREELANCE  —  CLAUSE À PRÉCISER",
                    "Une clause existe mais est incomplète ou floue. "
                    "Les contrats transmettant des droits d'auteur doivent être constatés par écrit "
                    "(art. L131-2 CPI). En outre, chaque droit cédé doit faire l'objet d'une mention "
                    "distincte et le domaine d'exploitation doit être délimité quant à son étendue, "
                    "sa destination, le lieu et la durée (art. L131-3 CPI). "
                    "Tout ce qui n'est pas clairement cédé reste à toi — "
                    "c'est un levier pour clarifier ou renégocier."
                )
            afficher_article(
                "Art. L131-3 CPI",
                "La transmission des droits de l'auteur est subordonnée à la condition que "
                "chacun des droits cédés fasse l'objet d'une mention distincte dans l'acte "
                "de cession et que le domaine d'exploitation soit délimité quant à son étendue "
                "et à sa destination, quant au lieu et quant à la durée."
            )


    # ------ CAS AUTRE ŒUVRE (texte, visuel, design, musique, etc.) ------
    elif creation in [2, 5, 6]:

        if statut == 1:  # Salarié
            if clause in [3, 4]:
                afficher_resultat(
                    "🟢", "SALARIÉ  —  TITULAIRE  —  HORS RÉGIME LOGICIEL",
                    "Contrairement aux logiciels, il n'existe pas de cession automatique "
                    "au profit de l'employeur pour les œuvres littéraires, graphiques, "
                    "audiovisuelles ou de design. "
                    "Sans clause de cession précise et écrite, tu restes titulaire "
                    "de tes droits d'auteur, même si la création a été réalisée "
                    "pendant tes heures de travail. "
                    "L'employeur peut disposer d'un droit d'usage limité lié au contrat "
                    "de travail, mais pas d'un monopole d'exploitation général."
                )
                afficher_article(
                    "Principe général  —  CPI",
                    "L'employeur ne bénéficie pas automatiquement des droits patrimoniaux "
                    "sur les œuvres créées par son salarié — sauf pour les logiciels (art. L113-9) "
                    "et certains cas particuliers comme les journalistes de presse (art. L132-36 s. CPI)."
                )
            elif clause == 1 and details == 1:
                afficher_resultat(
                    "🔴", "SALARIÉ  —  DROITS CÉDÉS  —  CLAUSE PRÉCISE",
                    "Le contrat prévoit une cession claire et bien détaillée. "
                    "L'employeur peut exploiter l'œuvre dans les limites définies. "
                    "Tu conserves tes droits moraux, inaliénables, et tout ce qui "
                    "n'a pas été expressément cédé."
                )
            else:
                afficher_resultat(
                    "🟡", "SALARIÉ  —  CLAUSE À ANALYSER",
                    "Une clause existe mais est incomplète ou floue. "
                    "En droit d'auteur, une transmission de droits doit être constatée par écrit "
                    "et précisément délimitée quant aux droits cédés et au domaine d'exploitation (art. L131-2 et L131-3 CPI)."
                    "Une clause générale 'tous droits cédés' sans détail des usages, "
                    "durée et territoire peut être insuffisante ou contestée. "
                    "Tu restes potentiellement titulaire des droits non clairement cédés."
                )

        elif statut == 2:  # Alternant
            if cadre_alt in [2, 3]:
                afficher_resultat(
                    "🟡", "ALTERNANT  —  ŒUVRE ACADÉMIQUE OU MIXTE",
                    "La création est liée à un projet académique ou mixte. "
                    "L'école et l'entreprise peuvent avoir des prétentions sur l'œuvre. "
                    "Examine les conditions générales de l'établissement de formation "
                    "et les clauses du contrat d'alternance. "
                    "Une partie des droits peut te rester acquise, notamment sur la "
                    "dimension académique."
                )
            elif cadre_alt == 4:
                afficher_resultat(
                    "🟢", "ALTERNANT  —  INITIATIVE PERSONNELLE",
                    "Créé sur ta seule initiative, sans lien avec ta mission ni projet académique. "
                    "En l'absence de clause explicite applicable, tu restes titulaire de tes droits."
                )
            else:
                afficher_resultat(
                    "🟡", "ALTERNANT  —  ŒUVRE DEMANDÉE PAR L'ENTREPRISE",
                    "Contrairement au logiciel, il n'y a pas de cession automatique au profit "
                    "de l'employeur pour les autres types d'œuvres. "
                    "Une clause de cession écrite et précise est nécessaire pour que "
                    "l'entreprise dispose de droits d'exploitation larges."
                )

        elif statut == 3:  # Stagiaire
            if clause_stage == 1:
                afficher_resultat(
                    "🟡", "STAGIAIRE  —  CLAUSE À ANALYSER",
                    "La convention contient une clause précise. "
                    "Vérifie qu'elle couvre bien l'œuvre créée, les usages prévus et la durée. "
                    "Tes droits moraux restent inaliénables quoi qu'il arrive."
                )
            elif clause_stage == 2:
                afficher_resultat(
                    "🟡", "STAGIAIRE  —  CLAUSE FLOUE",
                    "La clause est vague. En droit d'auteur, une transmission de droits doit être constatée par écrit "
                    "et précisément délimitée quant aux droits cédés et au domaine d'exploitation "
                    "pour être valable. (art. L131-2 et L131-3 CPI)."
                    "Tu conserves probablement des droits sur ce qui n'est pas clairement cédé."
                )
            else:
                afficher_resultat(
                    "🟢", "STAGIAIRE  —  TITULAIRE EN PRINCIPE",
                    "Sans clause, pas de cession. Tu es titulaire de tes droits. "
                    "L'exploitation par l'organisme sans accord écrit constitue "
                    "un usage potentiellement non autorisé."
                )

        elif statut == 4:  # Agent public
            if type_admin == 2:
                afficher_resultat(
                    "🟡", "AGENT PUBLIC  —  RECHERCHE OU ENSEIGNEMENT  —  RÉGIME À VÉRIFIER",
                    "Le principe reste que l'auteur conserve son droit, sous réserve des exceptions "
                    "prévues par le code. Pour les agents auteurs dont la divulgation n'est soumise "
                    "à aucun contrôle hiérarchique préalable, les règles spéciales applicables à "
                    "certains agents publics ne s'appliquent pas. Cette situation peut se rencontrer "
                    "dans certaines activités d'enseignement et de recherche, mais elle doit être "
                    "vérifiée concrètement au regard du statut, des fonctions exercées et des règles "
                    "de l'établissement."
                )
                afficher_article(
                    "Art. L111-1, L121-7-1 et L131-3-1 à L131-3-3 CPI",
                    "Les règles spéciales applicables à certains agents publics ne s'appliquent pas "
                    "aux agents auteurs d'œuvres dont la divulgation n'est soumise à aucun contrôle "
                    "préalable de l'autorité hiérarchique."
                )
            else:
                afficher_resultat(
                    "🟡", "AGENT PUBLIC  —  RÉGIME SPÉCIFIQUE",
                    "Pour les œuvres créées dans l'exercice des fonctions ou d'après les "
                    "instructions reçues, la personne publique bénéficie d'un droit "
                    "d'exploitation de plein droit uniquement dans la mesure strictement "
                    "nécessaire à l'accomplissement de sa mission de service public. Pour "
                    "l'exploitation commerciale, elle ne dispose en principe que d'un droit "
                    "de préférence. Ce régime s'applique à l'État et, par renvoi, à diverses "
                    "autres personnes publiques ; il ne s'applique pas aux agents dont la "
                    "divulgation n'est soumise à aucun contrôle hiérarchique préalable. Hors "
                    "de ces hypothèses, les droits restent à l'agent."
                )

        elif statut == 5:  # Freelance
            if clause in [3, 4]:
                afficher_resultat(
                    "🟢", "FREELANCE  —  TITULAIRE  —  PAS DE CESSION",
                    "Aucune clause de cession : tu restes titulaire de tous tes droits. "
                    "Le client ne peut exploiter l'œuvre que dans le cadre implicitement "
                    "prévu pour l'usage commandé — et rien de plus."
                )
            elif clause == 1 and details == 1:
                afficher_resultat(
                    "🔴", "FREELANCE  —  DROITS CÉDÉS  —  CONTRAT PRÉCIS",
                    "Cession claire et détaillée. Le client peut exploiter l'œuvre "
                    "dans les limites définies. "
                    "Tu conserves tes droits moraux et tout ce qui n'a pas été expressément cédé."
                )
            else:
                afficher_resultat(
                    "🟡", "FREELANCE  —  CLAUSE À PRÉCISER",
                    "La clause est incomplète. Tout ce qui n'est pas clairement cédé reste à toi. "
                    "C'est un levier pour clarifier les droits et, si nécessaire, renégocier."
                )
            afficher_article(
                "Art. L131-3 CPI",
                "La transmission des droits de l'auteur est subordonnée à la condition que "
                "chacun des droits cédés fasse l'objet d'une mention distincte dans l'acte "
                "de cession et que le domaine d'exploitation soit délimité quant à son étendue "
                "et à sa destination, quant au lieu et quant à la durée."
            )


    # =============================================================
    # SIGNAUX D'ALERTE  —  basés sur usage, nom, accord, valeur
    # =============================================================
    alertes = []

    if usage in [1, 2] and accord == 3:
        alertes.append(
            "⚠️  UTILISATION SANS ACCORD FORMEL : L'entreprise utilise ta création "
            "sans que tu aies formellement accepté. Si tu restes titulaire de droits "
            "non cédés, il s'agit d'une exploitation potentiellement non autorisée. "
            "Tu peux demander la régularisation par écrit."
        )

    if nom in [2, 3] and usage in [1, 2]:
        alertes.append(
            "⚠️  DROIT MORAL DE PATERNITÉ : Ton nom n'est pas ou peu mentionné alors que "
            "ta création est exploitée. Le droit de paternité est inaliénable (art. L121-1 CPI). "
            "Tu peux exiger que ton nom soit systématiquement cité, même après une cession "
            "des droits patrimoniaux."
        )

    if valeur in [1, 2] and clause in [3, 4] and usage in [1, 2]:
        alertes.append(
            "⚠️  VALEUR ÉCONOMIQUE SANS CADRE JURIDIQUE : La création a une valeur économique "
            "identifiable mais aucune clause ne régit formellement son exploitation. "
            "Cette situation mérite d'être régularisée par un accord écrit précis."
        )

    if ia in [2, 3]:
        alertes.append(
            "ℹ️  CONTRIBUTION D'UNE IA : Une IA a contribué à la création. "
            "Documente précisément ta contribution humaine originale — les choix créatifs "
            "ou techniques que tu as faits, les itérations, la sélection des éléments. "
            "Cela consolide ta position en matière de droit d'auteur."
        )

    if contrat == 3 and usage in [1, 2]:
        alertes.append(
            "⚠️  AUCUN CONTRAT ÉCRIT : L'entreprise exploite ta création sans qu'aucun "
            "accord écrit n'existe. C'est une situation précaire pour les deux parties. "
            "Propose de formaliser un accord, même minimal, sur les droits et usages."
        )

    if alertes:
        separateur("POINTS D'ATTENTION")
        for a in alertes:
            afficher_alerte(a)


    # =============================================================
    # CONSEILS
    # =============================================================
    separateur("CE QUE TU PEUX FAIRE")

    conseils = []

    conseils.append(
        "Garde des preuves horodatées de ta création : commits Git, fichiers avec "
        "dates de modification, mails, dépôts (INPI pour les brevets, IDDN pour les "
        "logiciels, enveloppe Soleau pour tout type d'œuvre)."
    )

    conseils.append(
        "Relis ton contrat, ta convention de stage ou de formation, et toutes les "
        "annexes portant sur la propriété intellectuelle avant toute discussion."
    )

    conseils.append(
        "Demande la mention de ton nom comme auteur ou créateur : "
        "le droit moral de paternité est inaliénable (art. L121-1 CPI), "
        "même en cas de cession complète des droits patrimoniaux."
    )

    if valeur in [1, 2]:
        conseils.append(
            "La création a une valeur économique directe. Pour les œuvres non-logicielles, "
            "une rémunération proportionnelle aux recettes peut être négociée. "
            "Pour les inventions de mission, une rémunération supplémentaire est due "
            "au salarié (art. L611-7 CPI). Ne laisse pas cette dimension de côté."
        )

    if valeur == 3:
        conseils.append(
            "La création a une valeur stratégique. Si elle contribue à l'avantage "
            "concurrentiel de l'entreprise, c'est un argument pour négocier "
            "une reconnaissance formelle ou une compensation."
        )

    if clause in [2, 3, 4] and usage in [1, 2]:
        conseils.append(
            "La situation n'est pas clairement formalisée alors que la création est exploitée. "
            "Propose un accord écrit précisant les droits cédés ou la licence accordée, "
            "la durée, le territoire et les usages autorisés. "
            "C'est protecteur pour les deux parties."
        )

    if statut in [3, 2]:
        conseils.append(
            "En tant que stagiaire ou alternant, tu peux négocier une mention de "
            "ta contribution dans les documents de l'entreprise (rapport, présentation, "
            "documentation). C'est précieux pour ton portfolio professionnel."
        )

    conseils.append(
        "En cas de doute sérieux ou de conflit : contacte un syndicat, "
        "un représentant du personnel, le service juridique de ton établissement "
        "ou un avocat spécialisé en propriété intellectuelle."
    )

    for c in conseils:
        print()
        print(wrap(c))


    # =============================================================
    # POINTS DE VIGILANCE
    # =============================================================
    separateur("POINTS DE VIGILANCE")

    vigilance = [
        "⚠️  En droit commun, les droits moraux (paternité, respect de l'œuvre, "
        "divulgation, repentir/retrait) sont attachés à la personne de l'auteur et sont "
        "en principe perpétuels, inaliénables et imprescriptibles (art. L121-1 CPI). "
        "Mais attention : pour les logiciels (art. L121-7 CPI) et pour les agents publics "
        "dans les cas où le régime spécial s'applique (art. L121-7-1 CPI), le droit moral "
        "est légalement aménagé, notamment pour les modifications et le retrait.",

        "⚠️  Pour toute cession d'œuvre hors logiciel créé dans les fonctions, "
        "la loi exige une mention distincte pour chaque droit cédé, avec la durée, "
        "le territoire et les usages autorisés (art. L131-3 CPI). "
        "Une clause générale 'tous droits cédés' est souvent insuffisante "
        "et peut être contestée devant un tribunal.",

        "⚠️  Une clause de non-concurrence ou de confidentialité peut restreindre "
        "ta liberté d'exploiter certaines créations même hors temps de travail "
        "et après la fin du contrat. Vérifie l'étendue de ces clauses.",

        "⚠️  Pour les brevets, la déclaration d'invention à l'employeur est une "
        "obligation légale dès lors que l'invention présente un lien avec l'activité "
        "de l'entreprise, même indirect. Un défaut de déclaration peut entraîner "
        "des conséquences juridiques."
    ]

    for v in vigilance:
        print()
        print(wrap(v))


    # =============================================================
    # FIN & EXPORT
    # =============================================================
    separateur()
    export = ask(
        "Veux-tu exporter ce diagnostic dans un fichier texte (.txt) ?",
        ["Oui, exporter", "Non merci"]
    )
    if export == 1:
        exporter_resultats()

    print("\n" + "=" * WIDTH)
    print("FIN DU DIAGNOSTIC".center(WIDTH))
    print("=" * WIDTH)
    print()
    print(wrap("Outil d'orientation — pas un avis juridique."))
    print(wrap("Pour une analyse personnalisée, consulte un professionnel du droit."))
    print()

except KeyboardInterrupt:
    print(f"\n\n{COULEUR_CHOISIE}  Programme interrompu. Au revoir !{REINITIALISATION}\n")
