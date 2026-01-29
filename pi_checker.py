#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Formulaire Python
Ce projet a été inspiré et assisté avec l’aide d'outils d'intelligence artificielle pour la rédaction du code.
Auteur : sa0
Licence : MIT
"""

import time
import os
import random
import sys
import textwrap


# =========================
# BANNIÈRE
# =========================


PALETTE_COULEURS = [
    (190, 166, 255),
    (100, 204, 142),
    (136, 189, 252),
]


rouge, vert, bleu = random.choice(PALETTE_COULEURS)
COULEUR_CHOISIE = f"\033[38;2;{rouge};{vert};{bleu}m"
REINITIALISATION = "\033[0m"


PHRASE = "per aspera, ad astra ✶"
NOM_SCRIPT = "INTELLECTUAL PROPERTY CHECKER"


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
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
# OUTILS
# =========================


WIDTH = 80


def wrap(txt):
    return textwrap.fill(txt, WIDTH)


def pause():
    time.sleep(0.3)


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
    print(COULEUR_CHOISIE + nom.center(WIDTH) + REINITIALISATION)
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


def ask(question, options):
    print("\n" + wrap(question))
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        r = input("\n>>> ")
        if r.isdigit() and 1 <= int(r) <= len(options):
            return int(r)
        print("Réponse invalide.")


# =========================
# PROGRAMME PRINCIPAL
# =========================


try:
    executer_animation_intro()
    time.sleep(0.8)
    afficher_en_tete(NOM_SCRIPT)


    print(wrap(
        "Ce questionnaire t’aide à comprendre qui détient les droits sur une création "
        "réalisée pendant, autour ou à côté de ton travail.\n"
        " Outil d’orientation — pas un avis juridique."
    ))


    # =========================
    # BLOC 1 — STATUT
    # =========================


    statut = ask(
        "Quel est ton statut principal ?",
        [
            "Salarié (CDI / CDD)",
            "Alternant",
            "Stagiaire",
            "Agent public",
            "Freelance / Indépendant"
        ]
    )


    contrat = ask(
        "As-tu un contrat / une convention écrite ?",
        [
            "Oui, je l’ai sous les yeux",
            "Oui, mais je réponds de mémoire",
            "Non, rien d’écrit"
        ]
    )


    # =========================
    # BLOC 2 — TYPE DE CRÉATION
    # =========================


    creation = ask(
        "Ta création correspond surtout à quoi ?",
        [
            "Du code / logiciel / script / application",
            "Un texte, visuel, vidéo, design, contenu",
            "Une idée technique ou invention",
            "Plusieurs choses",
            "Je ne sais pas"
        ]
    )


    # =========================
    # BLOC 3 — ORIGINE FACTUELLE
    # =========================


    origine = ask(
        "À l’origine, cette création vient :",
        [
            "D’une demande claire de l’entreprise",
            "D’une initiative personnelle encouragée",
            "D’une initiative personnelle tolérée",
            "Totalement de moi, sans lien avec le travail"
        ]
    )


    temps = ask(
        "Quand as-tu travaillé dessus ?",
        [
            "Uniquement pendant le travail",
            "Un mélange travail / perso",
            "Uniquement hors travail"
        ]
    )


    materiel = ask(
        "Avec quel matériel / logiciels ?",
        [
            "Uniquement ceux de l’entreprise",
            "Un mélange pro / perso",
            "Uniquement les miens"
        ]
    )


    # =========================
    # BLOC 4 — QUESTIONS SPÉCIFIQUES STATUT
    # =========================


    if statut == 2:  # Alternant
        cadre_alt = ask(
            "Cette création était demandée par :",
            [
                "L’entreprise",
                "L’école / centre de formation",
                "Les deux",
                "Moi seul(e)"
            ]
        )
    else:
        cadre_alt = None


    if statut == 3:  # Stagiaire
        clause_stage = ask(
            "Ta convention de stage contient-elle une clause sur la propriété intellectuelle ?",
            [
                "Oui, claire et détaillée",
                "Oui, mais floue",
                "Non",
                "Je ne sais pas"
            ]
        )
    else:
        clause_stage = None


    if statut == 4:  # Agent public
        type_admin = ask(
            "Tu travailles plutôt dans :",
            [
                "Administration classique",
                "Recherche / enseignement",
                "Établissement public spécifique",
                "Je ne sais pas"
            ]
        )
    else:
        type_admin = None


    # =========================
    # BLOC 5 — CONTRAT & CLAUSE
    # =========================


    clause = ask(
        "Ton contrat parle-t-il de propriété intellectuelle ?",
        [
            "Oui, clairement",
            "Oui, mais c’est flou",
            "Non",
            "Je ne sais pas"
        ]
    )


    if clause == 1:
        details = ask(
            "La clause précise-t-elle clairement : durée, territoires, droits cédés ?",
            [
                "Oui, tout est détaillé",
                "C’est vague",
                "Il manque des éléments",
                "Je ne sais pas"
            ]
        )
    else:
        details = None


    # =========================
    # BLOC 6 — UTILISATION
    # =========================


    usage = ask(
        "L’entreprise utilise-t-elle ta création ?",
        [
            "Oui, publiquement",
            "Oui, seulement en interne",
            "Pas encore, mais elle veut",
            "Non"
        ]
    )


    nom = ask(
        "Ton nom est-il mentionné comme créateur ?",
        [
            "Oui",
            "Non",
            "Parfois"
        ]
    )


    accord = ask(
        "As-tu donné ton accord pour cette utilisation ?",
        [
            "Oui, écrit",
            "Oui, oral",
            "Non"
        ]
    )


    # =========================
    # BLOC 7 — IA
    # =========================


    ia = ask(
        "Une intelligence artificielle a-t-elle été utilisée ?",
        [
            "Non",
            "Oui, comme outil",
            "Oui, elle a fait l’essentiel"
        ]
    )


    # =========================
    # BLOC 8 — VALEUR
    # =========================


    valeur = ask(
        "Cette création a-t-elle une valeur économique ?",
        [
            "Oui, elle génère ou peut générer de l’argent",
            "Oui, elle sert à vendre / promouvoir",
            "Valeur interne / stratégique",
            "Faible ou aucune"
        ]
    )


    # =========================
    # ANALYSE
    # =========================


    print("\n" + "-"*WIDTH)
    print("ANALYSE DE TA SITUATION".center(WIDTH))
    print("-"*WIDTH)
    pause()


    if ia == 3:
        print("⚠️ DROITS INCERTAINS / LIMITÉS")
        print(wrap(
            "Si une IA a généré l’essentiel de la création, la protection par le droit d’auteur est "
            "aujourd’hui incertaine ou très limitée : il faut en général une contribution humaine originale "
            "clairement identifiable pour qu’un droit d’auteur soit reconnu."
        ))
        print(wrap(
            "Ta situation dépend alors beaucoup du contexte, des conditions d’utilisation de l’IA et de ton "
            "apport personnel. Un avis juridique individualisé peut être nécessaire."
        ))
        sys.exit()


    # ---- STAGIAIRE ----
    if statut == 3:
        if clause_stage in [1, 2]:
            print("🟡 STAGIAIRE — CLAUSE À ANALYSER FINEMENT")
            print(wrap(
                "Ta convention de stage contient une clause sur la propriété intellectuelle. "
                "Elle peut organiser une cession ou une licence au profit de l’entreprise ou de l’organisme, "
                "mais elle doit rester suffisamment précise (œuvres visées, durée, territoire, usages) pour "
                "être valable. "
                "Même si la création a été demandée par l’entreprise, la portée exacte dépend de la rédaction "
                "de la clause et, en pratique, un contrat ou une clause de cession clairement ciblée est souvent "
                "nécessaire pour sécuriser l’exploitation. "
                "Pour une création hors mission ou sur ton initiative personnelle, tu restes en principe "
                "titulaire des droits, sous réserve de ce qui a été signé. "
                "Tes droits moraux restent inaliénables."
            ))
        else:
            print("🟢 STAGIAIRE — TITULAIRE EN PRINCIPE")
            print(wrap(
                "Pas de clause identifiable sur la propriété intellectuelle : en principe, tu es titulaire "
                "des droits sur tes créations. "
                "Même pour un projet demandé par l’entreprise, il n’y a pas de transfert automatique : "
                "une cession de droits doit être prévue par écrit et suffisamment détaillée pour être opposable. "
                "Tes droits moraux demeurent inaliénables."
            ))


    # ---- ALTERNANT ----
    elif statut == 2:
        if cadre_alt == 1:
            print("🔴 ALTERNANT — RÈGLES PROCHES DU SALARIÉ")
            print(wrap(
                "La création a été demandée par l’entreprise dans le cadre de ton contrat d’alternance. "
                "Pour les logiciels créés dans l’exercice de tes fonctions ou sur instruction de l’employeur, "
                "les droits patrimoniaux d’exploitation sont en principe dévolus à l’employeur. "
                "Pour les autres types de créations, tout dépend du contrat et des clauses de cession éventuelles."
            ))
        elif cadre_alt in [2, 3]:
            print("🟡 ALTERNANT — ZONE GRISE (ÉCOLE / ENTREPRISE)")
            print(wrap(
                "La création est liée à l’école ou à un projet mixte école / entreprise. "
                "Ni l’entreprise ni l’école n’ont automatiquement tous les droits : il faut regarder de près "
                "ton contrat de travail, la convention de formation et les éventuelles clauses de propriété "
                "intellectuelle. "
                "Tu peux rester titulaire d’une partie des droits et négocier des licences ou cessions si "
                "la création a une vraie valeur."
            ))
        else:
            print("🟢 ALTERNANT — INITIATIVE PERSONNELLE")
            print(wrap(
                "Tu as créé cette œuvre sur ton initiative personnelle, hors mission définie et hors horaires. "
                "En l’absence de clause spécifique qui viserait clairement ce type de créations, tu restes "
                "généralement titulaire des droits. "
                "L’utilisation par l’entreprise ou l’école suppose en principe une licence ou une cession "
                "négociée."
            ))


    # ---- AGENT PUBLIC ----
    elif statut == 4:
        print("🟡 AGENT PUBLIC — RÈGLES SPÉCIFIQUES")
        print(wrap(
            "Les agents publics sont soumis à des règles particulières : pour certaines créations réalisées "
            "dans le cadre des missions de service (par exemple logiciels ou documents administratifs), "
            "l’administration peut disposer de droits d’exploitation renforcés. "
            "Pour des créations sur initiative personnelle ou hors mission, tu peux rester pleinement titulaire "
            "de tes droits. "
            "Le détail dépend du type d’administration, du texte qui régit ton statut et, le cas échéant, "
            "de clauses spécifiques : une vérification au cas par cas est souvent nécessaire."
        ))


    # ---- FREELANCE ----
    elif statut == 5:
        # Pas de clause de cession, création personnelle sur son propre matos, hors mission
        if clause in [3, 4] and temps == 3 and materiel == 3 and origine in [3, 4]:
            print("🟢 FREELANCE — PROPRIÉTAIRE EN PRINCIPE")
            print(wrap(
                "Tu as créé cette œuvre sur ton initiative personnelle, hors mission définie et sur ton matériel. "
                "En l’absence de clause de cession ou de licence précise, tu restes en principe titulaire "
                "de tous tes droits. "
                "Un client qui souhaiterait exploiter la création doit obtenir une licence ou une cession "
                "clairement définie (durée, territoire, usages)."
            ))
        # Création pour un client mais contrat flou
        elif origine == 1 and clause in [2]:
            print("🟡 FREELANCE — CLAUSE À PRÉCISER")
            print(wrap(
                "Le client a commandé la création, mais la clause de cession est floue. "
                "En droit d’auteur, la cession doit décrire précisément les droits transférés "
                "(usages, durée, territoires, supports). "
                "Tu restes titulaire de tout ce qui n’est pas clairement cédé, ce qui te donne un levier "
                "pour clarifier ou renégocier le contrat."
            ))
        # Création mixte ou plusieurs clients / initiatives
        elif origine in [2, 3, 4]:
            print("🟡 FREELANCE — NÉGOCIATION POSSIBLE")
            print(wrap(
                "Création hors mission strictement définie ou sur ton initiative personnelle. "
                "La cession ou la licence doit être précisée par écrit dans le contrat, faute de quoi "
                "tu demeures titulaire des droits non transférés. "
                "Tu peux négocier l’étendue de la licence et la rémunération en fonction de la valeur de la création."
            ))
        # Cas par défaut : clause claire pour le client
        else:
            print("🔴 FREELANCE — DROITS CÉDÉS (CONTRAT PRÉCIS)")
            print(wrap(
                "Le contrat prévoit une cession ou une licence de droits rédigée de manière claire "
                "(durée, territoire, usages). "
                "Le client peut exploiter la création dans les limites prévues, et tu conserves uniquement "
                "les droits qui n’ont pas été cédés (par exemple certains usages non mentionnés ou des droits "
                "moraux)."
            ))


    # ---- SALARIÉ ----
    else:  # statut == 1
        # Logiciel clairement dans la mission
        if creation == 1 and origine == 1 and temps == 1:
            print("🔴 SALARIÉ — LOGICIEL : DROITS À L’EMPLOYEUR")
            print(wrap(
                "Le logiciel a été créé dans le cadre de tes fonctions, pendant le temps de travail, "
                "en réponse aux instructions de l’employeur. "
                "Pour ce type de création, le Code de la propriété intellectuelle prévoit que les droits "
                "patrimoniaux d’exploitation sont, en principe, dévolus à l’employeur."
            ))
        # Initiative perso claire, hors horaires et matériel perso, non logiciel ou cas limite
        elif origine in [2, 3, 4] and temps == 3 and materiel == 3 and clause == 1 and details == 1:
            print("🟢 SALARIÉ — INITIATIVE PERSONNELLE (APPRÉCIATION AU CAS PAR CAS)")
            print(wrap(
                "Tu as créé cette œuvre sur ton initiative personnelle, hors horaires de travail et sur ton "
                "matériel. "
                "Même si une clause de cession existe, un juge peut considérer que certaines créations "
                "strictement personnelles échappent à la cession automatique, surtout si elles ne relèvent "
                "pas directement de tes fonctions. "
                "L’entreprise aura souvent besoin d’un accord clair (licence ou cession ciblée) pour exploiter "
                "largement cette création."
            ))
        # Absence de clause claire (hors logiciel)
        elif clause in [3, 4] and creation != 1:
            print("🟢 SALARIÉ — PROPRIÉTAIRE (HORS RÉGIME SPÉCIAL)")
            print(wrap(
                "Sans clause claire de cession pour ce type d’œuvre, tu restes en principe titulaire des droits "
                "d’auteur sur tes créations qui ne relèvent pas d’un régime spécial (comme certains logiciels "
                "créés dans l’exercice des fonctions). "
                "L’employeur peut parfois disposer d’un droit d’usage limité lié à l’exécution du contrat, "
                "mais pas d’un monopole d’exploitation générale sans accord écrit plus précis."
            ))
        else:
            print("🟡 SALARIÉ — SITUATION MIXTE / CLAUSE FLOUE")
            print(wrap(
                "Tu es dans une situation mixte (travail / perso, matériel, clauses floues ou générales). "
                "Pour les logiciels créés dans le cadre de tes fonctions ou sur instruction, les droits "
                "patrimoniaux sont en principe dévolus à l’employeur, même si une partie du travail est faite "
                "hors horaires ou sur ton matériel. "
                "Pour les autres œuvres, tout ce qui n’est pas clairement cédé reste en principe à toi : "
                "c’est un levier de discussion ou de régularisation contractuelle."
            ))


    # =========================
    # CONSEILS
    # =========================


    print("\n" + "-"*WIDTH)
    print("CE QUE TU PEUX FAIRE".center(WIDTH))
    print("-"*WIDTH)
    conseils = [
        "Garde des preuves (dates, fichiers, mails, dépôts, versions).",
        "Lis attentivement ton contrat, ta convention de stage ou de formation et les annexes.",
        "Demande la mention de ton nom comme auteur ou créateur (droit moral).",
        "Si la création a de la valeur : discute d’une licence ou d’une cession écrite, avec conditions claires.",
        "En cas de doute sérieux ou de conflit : contacte un syndicat, un juriste ou un avocat spécialisé."
    ]


    for ligne in conseils:
        print(wrap(ligne))


    print("\n" + "-"*WIDTH)
    print("POINTS DE VIGILANCE".center(WIDTH))
    print("-"*WIDTH)


    vigilance = [
        "⚠️ Les droits moraux (paternité, respect de l’œuvre) sont en principe inaliénables : "
        "même si tu cèdes les droits patrimoniaux, ton nom doit être mentionné et "
        "l’intégrité de ta création respectée, sauf exceptions légales limitées.",


        "⚠️ Vérifie toujours :",
        "  • la durée et le territoire de la cession,",
        "  • les usages autorisés par le contrat (supports, types d’exploitation),",
        "  • si tu peux négocier une licence plutôt qu’une cession complète,",
        "  • les mentions obligatoires (nom, crédit, paternité).",


        "⚠️ Ces points sont essentiels pour protéger tes créations et ton droit moral, "
        "et pour encadrer les droits de ton employeur, de ton client ou de ton école."
    ]


    for ligne in vigilance:
        print(wrap(ligne))


    print("\n" + "="*WIDTH)
    print("FIN DU DIAGNOSTIC".center(WIDTH))
    print("="*WIDTH)
    print("Outil d’orientation — pas un avis juridique.")


except KeyboardInterrupt:
    print(f"\n\n{COULEUR_CHOISIE} Programme interrompu. Au revoir ! {REINITIALISATION}")