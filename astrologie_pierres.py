#!/usr/bin/env python3
"""
Application Astrologie & Pierres - Découvrez votre thème astral et vos pierres de pouvoir
Design moderne avec fonctionnalités enrichies
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
from enum import Enum
import random


# ────────────────────────────────────────────────────────────────────────────
# DONNÉES ASTROLOGIQUES
# ────────────────────────────────────────────────────────────────────────────

class Signe(Enum):
    """Énumération des signes astrologiques avec leurs dates"""
    BELIER = ("Bélier", (3, 21), (4, 19), "Feu", "Mars")
    TAUREAU = ("Taureau", (4, 20), (5, 20), "Terre", "Vénus")
    GEMEAUX = ("Gémeaux", (5, 21), (6, 20), "Air", "Mercure")
    CANCER = ("Cancer", (6, 21), (7, 22), "Eau", "Lune")
    LION = ("Lion", (7, 23), (8, 22), "Feu", "Soleil")
    VIERGE = ("Vierge", (8, 23), (9, 22), "Terre", "Mercure")
    BALANCE = ("Balance", (9, 23), (10, 22), "Air", "Vénus")
    SCORPION = ("Scorpion", (10, 23), (11, 21), "Eau", "Pluton")
    SAGITTAIRE = ("Sagittaire", (11, 22), (12, 21), "Feu", "Jupiter")
    CAPRICORNE = ("Capricorne", (12, 22), (1, 19), "Terre", "Saturne")
    VERSEAU = ("Verseau", (1, 20), (2, 18), "Air", "Uranus")
    POISSONS = ("Poissons", (2, 19), (3, 20), "Eau", "Neptune")

    def __init__(self, nom, date_debut, date_fin, element, planete):
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.element = element
        self.planete = planete


# Base de données des pierres par signe
PIERRES_PAR_SIGNE = {
    Signe.BELIER: [
        {"nom": "Cornaline", "proprietes": "Courage, énergie, confiance", "couleur": "Rouge-orange"},
        {"nom": "Calcite rouge", "proprietes": "Vitalité, passion, dynamisme", "couleur": "Rouge"},
        {"nom": "Jaspe rouge", "proprietes": "Force, protection, ancrage", "couleur": "Rouge"},
        {"nom": "Diamant", "proprietes": "Puissance, clarté mentale, invincibilité", "couleur": "Incolore"}
    ],
    Signe.TAUREAU: [
        {"nom": "Émeraude", "proprietes": "Stabilité, prospérité, amour", "couleur": "Vert"},
        {"nom": "Lapis-lazuli", "proprietes": "Sagesse, communication, sérénité", "couleur": "Bleu"},
        {"nom": "Turquoise", "proprietes": "Protection, équilibre, guérison", "couleur": "Bleu-vert"},
        {"nom": "Péridot", "proprietes": "Abondance, protection, clarté", "couleur": "Vert clair"}
    ],
    Signe.GEMEAUX: [
        {"nom": "Citrine", "proprietes": "Intelligence, communication, joie", "couleur": "Jaune"},
        {"nom": "Agathe", "proprietes": "Harmonie, équilibre, clarté", "couleur": "Multicolore"},
        {"nom": "Tourmaline noire", "proprietes": "Protection, ancrage", "couleur": "Noir"},
        {"nom": "Béryl", "proprietes": "Clarté mentale, éloquence", "couleur": "Incolore"}
    ],
    Signe.CANCER: [
        {"nom": "Opale", "proprietes": "Émotions, intuition, imagination", "couleur": "Arc-en-ciel"},
        {"nom": "Pierre de lune", "proprietes": "Douceur, intuition, féminité", "couleur": "Blanc laiteux"},
        {"nom": "Calcite blanche", "proprietes": "Pureté, clarté énergétique", "couleur": "Blanc"},
        {"nom": "Perle", "proprietes": "Sagesse, douceur, guérison émotionnelle", "couleur": "Blanc"},
    ],
    Signe.LION: [
        {"nom": "Or", "proprietes": "Rayonnement, confiance, majesté", "couleur": "Or"},
        {"nom": "Cristal de roche", "proprietes": "Clarté, puissance, amplification", "couleur": "Incolore"},
        {"nom": "Rubis", "proprietes": "Passion, leadership, vitalité", "couleur": "Rouge"},
        {"nom": "Ambre", "proprietes": "Chaleur, soleil, transformation", "couleur": "Ambre"}
    ],
    Signe.VIERGE: [
        {"nom": "Saphir bleu", "proprietes": "Sagesse, sincérité, clarté", "couleur": "Bleu"},
        {"nom": "Jade vert", "proprietes": "Purification, guérison, équilibre", "couleur": "Vert"},
        {"nom": "Sodalite", "proprietes": "Logique, harmonie intérieure", "couleur": "Bleu"},
        {"nom": "Améthyste", "proprietes": "Sérénité, sagesse, équilibre", "couleur": "Violet"}
    ],
    Signe.BALANCE: [
        {"nom": "Opale", "proprietes": "Équilibre, beauté, harmonie", "couleur": "Arc-en-ciel"},
        {"nom": "Lépidolite", "proprietes": "Sérénité, équilibre émotionnel", "couleur": "Violet"},
        {"nom": "Rose quartz", "proprietes": "Amour, douceur, harmonie", "couleur": "Rose"},
        {"nom": "Aventurine verte", "proprietes": "Prospérité, sérénité", "couleur": "Vert"}
    ],
    Signe.SCORPION: [
        {"nom": "Obsidienne noire", "proprietes": "Protection, transformation, profondeur", "couleur": "Noir"},
        {"nom": "Hémorite", "proprietes": "Vitalité, ancrage, purification", "couleur": "Rouge-noir"},
        {"nom": "Malachite", "proprietes": "Transformation, protection psychique", "couleur": "Vert"},
        {"nom": "Turmaline noire", "proprietes": "Purification psychique, protection", "couleur": "Noir"}
    ],
    Signe.SAGITTAIRE: [
        {"nom": "Topaze bleue", "proprietes": "Sagesse, communication, guérison", "couleur": "Bleu"},
        {"nom": "Lapis-lazuli", "proprietes": "Voyage, sagesse, protection", "couleur": "Bleu"},
        {"nom": "Citrine", "proprietes": "Abondance, optimisme, chance", "couleur": "Jaune"},
        {"nom": "Turquoise", "proprietes": "Protection du voyageur, sagesse", "couleur": "Bleu-vert"}
    ],
    Signe.CAPRICORNE: [
        {"nom": "Grenat", "proprietes": "Discipline, persévérance, ancrage", "couleur": "Rouge-noir"},
        {"nom": "Onyx noir", "proprietes": "Ancrage, protection, force intérieure", "couleur": "Noir"},
        {"nom": "Tourmaline noire", "proprietes": "Résilience, grounding", "couleur": "Noir"},
        {"nom": "Fluorite noire", "proprietes": "Ordre, clarté, structure", "couleur": "Noir-violet"}
    ],
    Signe.VERSEAU: [
        {"nom": "Améthyste", "proprietes": "Intuition, spiritualité, innovation", "couleur": "Violet"},
        {"nom": "Fluorite violette", "proprietes": "Conscience, spiritualité, clarté", "couleur": "Violet"},
        {"nom": "Labradorite", "proprietes": "Intuition, protection, transformation", "couleur": "Gris-bleu"},
        {"nom": "Tourmaline électrique", "proprietes": "Innovation, énergie future", "couleur": "Noir"},
    ],
    Signe.POISSONS: [
        {"nom": "Améthyste", "proprietes": "Intuition, spiritualité, sensibilité", "couleur": "Violet"},
        {"nom": "Calcédoine rose", "proprietes": "Douceur, compassion, guérison", "couleur": "Rose"},
        {"nom": "Fluorite verte", "proprietes": "Équilibre émotionnel, guérison", "couleur": "Vert"},
        {"nom": "Aigue-marine", "proprietes": "Fluidité, clarté, paix intérieure", "couleur": "Bleu clair"}
    ]
}


# Descriptions des éléments
DESCRIPTIONS_ELEMENTS = {
    "Feu": "Passion, dynamisme, créativité",
    "Terre": "Stabilité, pragmatisme, ancrage",
    "Air": "Communication, intellect, liberté",
    "Eau": "Émotions, intuition, compassion"
}

# Chakras associés à chaque signe
CHAKRAS_PAR_SIGNE = {
    Signe.BELIER: {"nom": "Chakra Racine", "couleur": "Rouge", "localisation": "Base de la colonne vertébrale", "element": "Terre"},
    Signe.TAUREAU: {"nom": "Chakra Racine", "couleur": "Rouge", "localisation": "Base de la colonne vertébrale", "element": "Terre"},
    Signe.GEMEAUX: {"nom": "Chakra Laryngé", "couleur": "Bleu ciel", "localisation": "Gorge", "element": "Air"},
    Signe.CANCER: {"nom": "Chakra du Cœur", "couleur": "Rose/Vert", "localisation": "Cœur", "element": "Eau"},
    Signe.LION: {"nom": "Chakra du Plexus Solaire", "couleur": "Jaune doré", "localisation": "Fosse à l'estomac", "element": "Feu"},
    Signe.VIERGE: {"nom": "Chakra du Plexus Solaire", "couleur": "Jaune doré", "localisation": "Fosse à l'estomac", "element": "Terre"},
    Signe.BALANCE: {"nom": "Chakra du Cœur", "couleur": "Rose/Vert", "localisation": "Cœur", "element": "Air"},
    Signe.SCORPION: {"nom": "Chakra Sacré", "couleur": "Orange", "localisation": "Bas-ventre", "element": "Eau"},
    Signe.SAGITTAIRE: {"nom": "Chakra du Troisième Œil", "couleur": "Indigo", "localisation": "Front", "element": "Feu"},
    Signe.CAPRICORNE: {"nom": "Chakra Racine", "couleur": "Rouge", "localisation": "Base de la colonne vertébrale", "element": "Terre"},
    Signe.VERSEAU: {"nom": "Chakra Laryngé", "couleur": "Bleu ciel", "localisation": "Gorge", "element": "Air"},
    Signe.POISSONS: {"nom": "Chakra de la Couronne", "couleur": "Violet", "localisation": "Sommet du crâne", "element": "Eau"}
}

# Couleurs porte-bonheur
COULEURS_SIGNE = {
    Signe.BELIER: ["Rouge", "Blanc", "Or"],
    Signe.TAUREAU: ["Vert", "Rose", "Bleu"],
    Signe.GEMEAUX: ["Jaune", "Gris", "Blanc"],
    Signe.CANCER: ["Blanc", "Argent", "Crème"],
    Signe.LION: ["Or", "Rouge", "Jaune"],
    Signe.VIERGE: ["Vert", "Beige", "Marron"],
    Signe.BALANCE: ["Rose", "Bleu ciel", "Blanc"],
    Signe.SCORPION: ["Rouge", "Noir", "Marron"],
    Signe.SAGITTAIRE: ["Violet", "Bleu", "Vert"],
    Signe.CAPRICORNE: ["Noir", "Gris", "Marron"],
    Signe.VERSEAU: ["Turquoise", "Bleu électrique", "Argent"],
    Signe.POISSONS: ["Turquoise", "Violet", "Vert clair"]
}

# Mantras personnalisés
MANTRAS_PAR_SIGNE = {
    Signe.BELIER: "Je suis courageux et je fonce avec confiance vers mes objectifs.",
    Signe.TAUREAU: "Je suis stable, grounded et j'attire l'abondance dans ma vie.",
    Signe.GEMEAUX: "Je communique avec clarté et je suis curieux du monde.",
    Signe.CANCER: "Je suis protégé par mon intuition et ma sensibilité est ma force.",
    Signe.LION: "Je rayonne avec confiance et j'inspire ceux qui m'entourent.",
    Signe.VIERGE: "Je suis conscient et je cultive l'harmonie en moi ET autour de moi.",
    Signe.BALANCE: "Je cherche l'équilibre et je crée plus de beauté dans le monde.",
    Signe.SCORPION: "Je me transforme constamment et je maîtrise ma destinée.",
    Signe.SAGITTAIRE: "Je suis libre et je explore les frontières infinies de la vie.",
    Signe.CAPRICORNE: "Je suis persévérant et j'édifie un futur solide et prospère.",
    Signe.VERSEAU: "Je suis unique et je révolutionne le monde avec mes idées.",
    Signe.POISSONS: "Je flotte avec grâce et ma compassion guérit le monde."
}

# Compatibilité amoureuse entre signes (1-5 cœurs)
COMPATIBILITE_AMOUREUSE = {
    Signe.BELIER: {
        Signe.BELIER: 4, Signe.TAUREAU: 2, Signe.GEMEAUX: 4, Signe.CANCER: 2,
        Signe.LION: 5, Signe.VIERGE: 2, Signe.BALANCE: 3, Signe.SCORPION: 3,
        Signe.SAGITTAIRE: 5, Signe.CAPRICORNE: 2, Signe.VERSEAU: 4, Signe.POISSONS: 2
    },
    Signe.TAUREAU: {
        Signe.BELIER: 2, Signe.TAUREAU: 4, Signe.GEMEAUX: 2, Signe.CANCER: 5,
        Signe.LION: 2, Signe.VIERGE: 5, Signe.BALANCE: 3, Signe.SCORPION: 4,
        Signe.SAGITTAIRE: 2, Signe.CAPRICORNE: 5, Signe.VERSEAU: 2, Signe.POISSONS: 4
    },
    Signe.GEMEAUX: {
        Signe.BELIER: 4, Signe.TAUREAU: 2, Signe.GEMEAUX: 4, Signe.CANCER: 2,
        Signe.LION: 3, Signe.VIERGE: 4, Signe.BALANCE: 5, Signe.SCORPION: 2,
        Signe.SAGITTAIRE: 5, Signe.CAPRICORNE: 2, Signe.VERSEAU: 5, Signe.POISSONS: 2
    },
    Signe.CANCER: {
        Signe.BELIER: 2, Signe.TAUREAU: 5, Signe.GEMEAUX: 2, Signe.CANCER: 4,
        Signe.LION: 2, Signe.VIERGE: 4, Signe.BALANCE: 3, Signe.SCORPION: 5,
        Signe.SAGITTAIRE: 2, Signe.CAPRICORNE: 4, Signe.VERSEAU: 2, Signe.POISSONS: 5
    },
    Signe.LION: {
        Signe.BELIER: 5, Signe.TAUREAU: 2, Signe.GEMEAUX: 3, Signe.CANCER: 2,
        Signe.LION: 4, Signe.VIERGE: 2, Signe.BALANCE: 5, Signe.SCORPION: 2,
        Signe.SAGITTAIRE: 5, Signe.CAPRICORNE: 2, Signe.VERSEAU: 3, Signe.POISSONS: 2
    },
    Signe.VIERGE: {
        Signe.BELIER: 2, Signe.TAUREAU: 5, Signe.GEMEAUX: 4, Signe.CANCER: 4,
        Signe.LION: 2, Signe.VIERGE: 4, Signe.BALANCE: 3, Signe.SCORPION: 4,
        Signe.SAGITTAIRE: 2, Signe.CAPRICORNE: 5, Signe.VERSEAU: 2, Signe.POISSONS: 4
    },
    Signe.BALANCE: {
        Signe.BELIER: 3, Signe.TAUREAU: 3, Signe.GEMEAUX: 5, Signe.CANCER: 3,
        Signe.LION: 5, Signe.VIERGE: 3, Signe.BALANCE: 4, Signe.SCORPION: 2,
        Signe.SAGITTAIRE: 4, Signe.CAPRICORNE: 2, Signe.VERSEAU: 5, Signe.POISSONS: 3
    },
    Signe.SCORPION: {
        Signe.BELIER: 3, Signe.TAUREAU: 4, Signe.GEMEAUX: 2, Signe.CANCER: 5,
        Signe.LION: 2, Signe.VIERGE: 4, Signe.BALANCE: 2, Signe.SCORPION: 4,
        Signe.SAGITTAIRE: 2, Signe.CAPRICORNE: 4, Signe.VERSEAU: 2, Signe.POISSONS: 5
    },
    Signe.SAGITTAIRE: {
        Signe.BELIER: 5, Signe.TAUREAU: 2, Signe.GEMEAUX: 5, Signe.CANCER: 2,
        Signe.LION: 5, Signe.VIERGE: 2, Signe.BALANCE: 4, Signe.SCORPION: 2,
        Signe.SAGITTAIRE: 4, Signe.CAPRICORNE: 2, Signe.VERSEAU: 5, Signe.POISSONS: 2
    },
    Signe.CAPRICORNE: {
        Signe.BELIER: 2, Signe.TAUREAU: 5, Signe.GEMEAUX: 2, Signe.CANCER: 4,
        Signe.LION: 2, Signe.VIERGE: 5, Signe.BALANCE: 2, Signe.SCORPION: 4,
        Signe.SAGITTAIRE: 2, Signe.CAPRICORNE: 4, Signe.VERSEAU: 2, Signe.POISSONS: 3
    },
    Signe.VERSEAU: {
        Signe.BELIER: 4, Signe.TAUREAU: 2, Signe.GEMEAUX: 5, Signe.CANCER: 2,
        Signe.LION: 3, Signe.VIERGE: 2, Signe.BALANCE: 5, Signe.SCORPION: 2,
        Signe.SAGITTAIRE: 5, Signe.CAPRICORNE: 2, Signe.VERSEAU: 4, Signe.POISSONS: 3
    },
    Signe.POISSONS: {
        Signe.BELIER: 2, Signe.TAUREAU: 4, Signe.GEMEAUX: 2, Signe.CANCER: 5,
        Signe.LION: 2, Signe.VIERGE: 4, Signe.BALANCE: 3, Signe.SCORPION: 5,
        Signe.SAGITTAIRE: 2, Signe.CAPRICORNE: 3, Signe.VERSEAU: 3, Signe.POISSONS: 4
    }
}

# Influence lunaire sur chaque signe
INFLUENCES_LUNAIRES = {
    "Lune Nouvelle": "Idéal pour débuter de nouveaux projets et prendre des décisions",
    "Lune Croissante": "Amplifiez vos efforts et manifester vos intentions",
    "Pleine Lune": "État d'énergie maximal, perfectionnez ce que vous avez commencé",
    "Lune Décroissante": "Moment de lâcher-prise et d'introspection"
}

# Conseils quotidiens par élément
CONSEILS_BIEN_ETRE = {
    "Feu": "🔥 Canalisez votre énergie avec de l'exercice intensif. Portez des pierres rouges pour intensifier votre feu intérieur.",
    "Terre": "🌍 Connectez-vous à la Nature. Marchez pieds nus, méditez dehors. Portez du vert pour rester ancré.",
    "Air": "💨 Respirez profondément et pratiquez le yoga. Portez du bleu pour favoriser la clarté mentale.",
    "Eau": "💧 Pratiquez l'auto-compassion et la méditation. Prenez un bain apaisant. Portez du rose/blanc pour la sérénité."
}

# Pierres de destinée (cristal de naissance)
CRISTAL_DE_NAISSANCE_MOIS = {
    1: "Grenat", 2: "Améthyste", 3: "Aigue-marine", 4: "Diamant",
    5: "Émeraude", 6: "Perle", 7: "Rubis", 8: "Péridot",
    9: "Saphir", 10: "Opale", 11: "Topaze", 12: "Turquoise"
}

PROPRIETES_CRISTAL_MOIS = {
    1: "Protection et Force", 2: "Sérénité et Spiritualité", 3: "Guérison et Sérénité",
    4: "Pureté et Incorruptibilité", 5: "Amour et Succès", 6: "Pureté et Protection",
    7: "Passion et Prospérité", 8: "Vitalité et Chance", 9: "Sagesse et Sincérité",
    10: "Espoir et Imagination", 11: "Prospérité et Guérison", 12: "Voyage et Paix"
}


# ────────────────────────────────────────────────────────────────────────────
# LOGIQUE MÉTIER
# ────────────────────────────────────────────────────────────────────────────

def determiner_signe(jour: int, mois: int) -> Signe:
    """Détermine le signe astrologique en fonction de la date de naissance"""
    date_check = (mois, jour)
    
    for signe in Signe:
        debut = signe.date_debut
        fin = signe.date_fin
        
        # Gestion spéciale pour les signes qui changent d'année (Capricorne)
        if debut[0] > fin[0]:  # Ex: (12, 22) à (1, 19)
            if date_check >= debut or date_check <= fin:
                return signe
        else:
            if debut <= date_check <= fin:
                return signe
    
    return Signe.BELIER  # Par défaut


def calculer_age(date_naissance: date) -> int:
    """Calcule l'âge en fonction de la date de naissance"""
    aujourd_hui = date.today()
    age = aujourd_hui.year - date_naissance.year
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1
    return age


def generer_profil(nom: str, prenoms: str, date_naissance: date) -> dict:
    """Génère un profil astrologique complet"""
    signe = determiner_signe(date_naissance.day, date_naissance.month)
    age = calculer_age(date_naissance)
    
    return {
        "nom_complet": f"{prenoms} {nom}",
        "signe": signe,
        "age": age,
        "date_naissance": date_naissance,
        "element": signe.element,
        "planete": signe.planete,
        "pierres": PIERRES_PAR_SIGNE[signe]
    }


# ────────────────────────────────────────────────────────────────────────────
# INTERFACE GRAPHIQUE
# ────────────────────────────────────────────────────────────────────────────

class AstrologyApp(tk.Tk):
    """Application Astrologie & Pierres - Design Moderne"""
    
    # Palette de couleurs moderne
    BG_PRIMARY = "#0a0e27"      # Fond principal très sombre
    BG_SECONDARY = "#1a1f3a"    # Fond secondaire
    BG_TERTIARY = "#2d3561"     # Fond tertiaire
    COLOR_ACCENT = "#c77dff"    # Rose/Violet
    COLOR_ACCENT_LIGHT = "#d8b3ff"
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#b4b9d1"
    SUCCESS = "#00d9ff"
    WARNING = "#ffa500"
    
    def __init__(self):
        super().__init__()
        self.title("✨ Astrologie & Pierres de Pouvoir ✨")
        self.geometry("1100x800")
        self.minsize(1000, 700)
        self.configure(bg=self.BG_PRIMARY)
        
        # Configuration du style
        self.setup_styles()
        
        self.profil = None
        self.create_widgets()
        
    def setup_styles(self):
        """Configure le style moderne"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Couleurs de base
        self.style.configure('TFrame', background=self.BG_PRIMARY)
        self.style.configure('TLabel', background=self.BG_PRIMARY, foreground=self.TEXT_PRIMARY)
        self.style.configure('TButton', font=('Helvetica', 10), background=self.BG_SECONDARY)
        
        # Styles personnalisés
        self.style.configure('Title.TLabel', font=('Helvetica', 22, 'bold'), 
                            foreground=self.COLOR_ACCENT, background=self.BG_PRIMARY)
        self.style.configure('Heading.TLabel', font=('Helvetica', 14, 'bold'), 
                            foreground=self.COLOR_ACCENT_LIGHT, background=self.BG_PRIMARY)
        self.style.configure('SubHeading.TLabel', font=('Helvetica', 11, 'bold'), 
                            foreground=self.SUCCESS, background=self.BG_SECONDARY)
        self.style.configure('Info.TLabel', font=('Helvetica', 10), 
                            foreground=self.TEXT_SECONDARY, background=self.BG_SECONDARY)
        self.style.configure('TLabelframe', background=self.BG_SECONDARY, foreground=self.COLOR_ACCENT,
                            relief='flat', borderwidth=0)
        self.style.configure('TLabelframe.Label', background=self.BG_SECONDARY, 
                            foreground=self.COLOR_ACCENT, font=('Helvetica', 11, 'bold'))
        
    def create_widgets(self):
        """Crée les widgets de l'interface modernisée"""
        # Frame principal avec gradient
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header avec titre et logo
        self.create_header(main_frame)
        
        # Créer les onglets
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Configuration du style des onglets
        self.style.configure('TNotebook', background=self.BG_PRIMARY, borderwidth=0)
        self.style.configure('TNotebook.Tab', padding=[20, 10], font=('Helvetica', 10))
        
        # Onglet 1: Formulaire
        form_frame = ttk.Frame(self.notebook)
        self.notebook.add(form_frame, text="📝 Formulaire")
        self.create_form(form_frame)
        
        # Onglet 2: Profil Astrologique
        self.result_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.result_frame, text="🌟 Votre Profil")
        
        # Onglet 3: Pierres & Chakras
        self.result_frame2 = ttk.Frame(self.notebook)
        self.notebook.add(self.result_frame2, text="💎 Pierres & Chakras")
        
        # Onglet 4: Astrologie Amoureuse
        self.result_frame3 = ttk.Frame(self.notebook)
        self.notebook.add(self.result_frame3, text="💕 Compatibilité")
        
        # Onglet 5: Bien-être
        self.result_frame4 = ttk.Frame(self.notebook)
        self.notebook.add(self.result_frame4, text="🧘 Bien-être & Conseils")
    
    def create_header(self, parent):
        """Crée l'en-tête avec titre"""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, padx=15, pady=15)
        
        title = ttk.Label(header_frame, text="✨ Astrologie & Pierres de Pouvoir ✨", style='Title.TLabel')
        title.pack(side=tk.LEFT, expand=True)
        
        subtitle = ttk.Label(header_frame, text="Découvrez votre destinée astrale", style='Info.TLabel')
        subtitle.pack(side=tk.LEFT, padx=20)
        
    def create_form(self, parent):
        """Crée le formulaire d'entrée modernisé"""
        canvas = tk.Canvas(parent, bg=self.BG_PRIMARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Section informations personnelles
        info_labelframe = ttk.LabelFrame(scrollable_frame, text="👤 Informations Personnelles", padding="20")
        info_labelframe.pack(fill=tk.X, padx=20, pady=10)
        
        # Nom
        ttk.Label(info_labelframe, text="Nom :", style='Heading.TLabel').grid(row=0, column=0, sticky='e', padx=10, pady=8)
        self.entry_nom = ttk.Entry(info_labelframe, width=35, font=('Helvetica', 11))
        self.entry_nom.grid(row=0, column=1, sticky='ew', padx=10, pady=8)
        
        # Prénoms
        ttk.Label(info_labelframe, text="Prénoms :", style='Heading.TLabel').grid(row=1, column=0, sticky='e', padx=10, pady=8)
        self.entry_prenoms = ttk.Entry(info_labelframe, width=35, font=('Helvetica', 11))
        self.entry_prenoms.grid(row=1, column=1, sticky='ew', padx=10, pady=8)
        
        # Date de naissance
        ttk.Label(info_labelframe, text="Date de naissance :", style='Heading.TLabel').grid(row=2, column=0, sticky='nw', padx=10, pady=8)
        
        date_frame = ttk.Frame(info_labelframe)
        date_frame.grid(row=2, column=1, sticky='ew', padx=10, pady=8)
        
        ttk.Label(date_frame, text="Jour:", style='Info.TLabel').pack(side=tk.LEFT, padx=5)
        self.spin_jour = ttk.Spinbox(date_frame, from_=1, to=31, width=4, font=('Helvetica', 10))
        self.spin_jour.set(15)
        self.spin_jour.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(date_frame, text="Mois:", style='Info.TLabel').pack(side=tk.LEFT, padx=5)
        self.spin_mois = ttk.Spinbox(date_frame, from_=1, to=12, width=4, font=('Helvetica', 10))
        self.spin_mois.set(6)
        self.spin_mois.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(date_frame, text="Année:", style='Info.TLabel').pack(side=tk.LEFT, padx=5)
        self.spin_annee = ttk.Spinbox(date_frame, from_=1900, to=2025, width=6, font=('Helvetica', 10))
        self.spin_annee.set(1995)
        self.spin_annee.pack(side=tk.LEFT, padx=5)
        
        info_labelframe.columnconfigure(1, weight=1)
        
        # Section horoscope
        horoscope_labelframe = ttk.LabelFrame(scrollable_frame, text="🔮 Horoscope Rapide", padding="20")
        horoscope_labelframe.pack(fill=tk.X, padx=20, pady=10)
        
        ttk.Label(horoscope_labelframe, text="Cherchez-vous la compatibilité amoureuse ?", style='Heading.TLabel').pack(anchor=tk.W, pady=5)
        
        self.combo_signe_amoure = ttk.Combobox(horoscope_labelframe, 
            values=[s.nom for s in Signe], width=30, font=('Helvetica', 10), state='readonly')
        self.combo_signe_amoure.set("-- Choisissez un signe --")
        self.combo_signe_amoure.pack(fill=tk.X, pady=10)
        
        # Bouton de validation
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(pady=30)
        
        btn_valider = ttk.Button(button_frame, text="🚀 Découvrir mon Thème Astral", 
                                command=self.valider_formulaire)
        btn_valider.pack(ipadx=20, ipady=10)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def valider_formulaire(self):
        """Valide et traite le formulaire"""
        try:
            nom = self.entry_nom.get().strip()
            prenoms = self.entry_prenoms.get().strip()
            jour = int(self.spin_jour.get())
            mois = int(self.spin_mois.get())
            annee = int(self.spin_annee.get())
            
            if not nom or not prenoms:
                messagebox.showerror("Erreur", "Veuillez entrer votre nom et vos prénoms")
                return
            
            if not (1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee <= 2025):
                messagebox.showerror("Erreur", "Date invalide")
                return
            
            date_naissance = date(annee, mois, jour)
            
            if date_naissance > date.today():
                messagebox.showerror("Erreur", "La date de naissance ne peut pas être dans le futur")
                return
            
            # Générer le profil
            self.profil = generer_profil(nom, prenoms, date_naissance)
            self.afficher_resultats()
            self.notebook.select(1)
            
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides")
    
    def afficher_resultats(self):
        """Affiche tous les onglets de résultats"""
        if not self.profil:
            return
        
        # Effacer les anciens widgets
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        for widget in self.result_frame2.winfo_children():
            widget.destroy()
        for widget in self.result_frame3.winfo_children():
            widget.destroy()
        for widget in self.result_frame4.winfo_children():
            widget.destroy()
        
        # Remplir onglet 1: Profil
        self.remplir_profil(self.result_frame)
        
        # Remplir onglet 2: Pierres & Chakras
        self.remplir_pierres_chakras(self.result_frame2)
        
        # Remplir onglet 3: Compatibilité
        self.remplir_compatibilite(self.result_frame3)
        
        # Remplir onglet 4: Bien-être
        self.remplir_bien_etre(self.result_frame4)
    
    def remplir_profil(self, parent):
        """Remplir l'onglet profil astrologique"""
        canvas = tk.Canvas(parent, bg=self.BG_PRIMARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Titre du profil
        titre = ttk.Label(scrollable_frame, text=f"🌟 Bienvenue {self.profil['nom_complet']} ! 🌟", style='Title.TLabel')
        titre.pack(pady=20)
        
        # Info de base
        signe = self.profil['signe']
        
        info_frame = ttk.LabelFrame(scrollable_frame, text="📊 Votre Profil Astral", padding="20")
        info_frame.pack(fill=tk.X, padx=20, pady=10)
        
        info_text = f"""
Âge : {self.profil['age']} ans
Date de naissance : {self.profil['date_naissance'].strftime('%d/%m/%Y')}
Cristal de naissance : {CRISTAL_DE_NAISSANCE_MOIS[self.profil['date_naissance'].month]} ({PROPRIETES_CRISTAL_MOIS[self.profil['date_naissance'].month]})
        """
        ttk.Label(info_frame, text=info_text, style='Info.TLabel', justify=tk.LEFT).pack(anchor=tk.W)
        
        # Signe astrologique
        signe_frame = ttk.LabelFrame(scrollable_frame, text="♈ Votre Signe Astrologique", padding="20")
        signe_frame.pack(fill=tk.X, padx=20, pady=10)
        
        signe_text = f"""
Signe : ⭐ {signe.nom.upper()}
Élément : {signe.element}
Description : {DESCRIPTIONS_ELEMENTS[signe.element]}
Planète Maîtresse : {signe.planete}
Couleurs porte-bonheur : {', '.join(COULEURS_SIGNE[signe])}
        """
        ttk.Label(signe_frame, text=signe_text, style='Info.TLabel', justify=tk.LEFT).pack(anchor=tk.W)
        
        # Mantra
        mantra_frame = ttk.LabelFrame(scrollable_frame, text="🙏 Votre Mantra Personnel", padding="20")
        mantra_frame.pack(fill=tk.X, padx=20, pady=10)
        
        mantra_text = MANTRAS_PAR_SIGNE[signe]
        ttk.Label(mantra_frame, text=f'"{mantra_text}"', style='SubHeading.TLabel', 
                 justify=tk.LEFT, wraplength=600).pack(anchor=tk.W)
        
        # Conseil astral
        conseil_frame = ttk.LabelFrame(scrollable_frame, text="🔮 Conseil Astral", padding="20")
        conseil_frame.pack(fill=tk.X, padx=20, pady=10)
        
        conseil = f"""
En tant que {signe.nom}, vous êtes naturellement {DESCRIPTIONS_ELEMENTS[signe.element].lower()}.
La {signe.planete} veille sur vous et guide votre destinée.
Vos forces : Énergie, dynamisme et capacité à transformer les défis en opportunités.
Vos défis : Apprendre l'équilibre et l'introspection pour une vie harmonieuse.
        """
        ttk.Label(conseil_frame, text=conseil, style='Info.TLabel', 
                 justify=tk.LEFT, wraplength=600).pack(anchor=tk.W)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def remplir_pierres_chakras(self, parent):
        """Remplir l'onglet pierres et chakras"""
        canvas = tk.Canvas(parent, bg=self.BG_PRIMARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        signe = self.profil['signe']
        
        # Pierres de pouvoir
        pierres_frame = ttk.LabelFrame(scrollable_frame, text="💎 Vos Pierres de Pouvoir", padding="20")
        pierres_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        for i, pierre in enumerate(self.profil['pierres'], 1):
            pierre_text = f"""
🔷 {pierre['nom'].upper()}
   Propriétés : {pierre['proprietes']}
   Couleur : {pierre['couleur']}
            """
            ttk.Label(pierres_frame, text=pierre_text, style='SubHeading.TLabel', 
                     justify=tk.LEFT).pack(anchor=tk.W, pady=5)
        
        # Chakra associé
        chakra = CHAKRAS_PAR_SIGNE[signe]
        
        chakra_frame = ttk.LabelFrame(scrollable_frame, text="🌀 Votre Chakra Dominant", padding="20")
        chakra_frame.pack(fill=tk.X, padx=20, pady=10)
        
        chakra_text = f"""
Chakra : {chakra['nom']}
Couleur : {chakra['couleur']}
Localisation : {chakra['localisation']}
Élément : {chakra['element']}

💡 Conseil : Portez vos pierres sur ce chakra pour harmoniser votre énergie vitale.
        """
        ttk.Label(chakra_frame, text=chakra_text, style='Info.TLabel', 
                 justify=tk.LEFT, wraplength=600).pack(anchor=tk.W)
        
        # Cristal de naissance
        cristal_frame = ttk.LabelFrame(scrollable_frame, text="💫 Votre Cristal de Destinée", padding="20")
        cristal_frame.pack(fill=tk.X, padx=20, pady=10)
        
        mois = self.profil['date_naissance'].month
        cristal_text = f"""
Cristal : {CRISTAL_DE_NAISSANCE_MOIS[mois]}
Pouvoir : {PROPRIETES_CRISTAL_MOIS[mois]}

💫 Portez ce cristal pour activer votre destinée et votre chemin de vie.
        """
        ttk.Label(cristal_frame, text=cristal_text, style='Info.TLabel', 
                 justify=tk.LEFT, wraplength=600).pack(anchor=tk.W)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def remplir_compatibilite(self, parent):
        """Remplir l'onglet compatibilité amoureuse"""
        canvas = tk.Canvas(parent, bg=self.BG_PRIMARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        titre = ttk.Label(scrollable_frame, text="💕 Votre Compatibilité Amoureuse 💕", style='Title.TLabel')
        titre.pack(pady=20)
        
        signe_perso = self.profil['signe']
        
        # Afficher la compatibilité avec tous les signes (sauf le sien)
        compat_frame = ttk.LabelFrame(scrollable_frame, text="⭐ Compatibilité par Signe", padding="20")
        compat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        for autre_signe in Signe:
            if autre_signe == signe_perso:
                continue
            
            score = COMPATIBILITE_AMOUREUSE[signe_perso][autre_signe]
            coeurs = "❤️" * score + "🤍" * (5 - score)
            
            compat_text = f"{autre_signe.nom.ljust(12)} : {coeurs}  ({score}/5)"
            ttk.Label(compat_frame, text=compat_text, style='Info.TLabel').pack(anchor=tk.W, pady=2)
        
        # Recommandations
        conseil_frame = ttk.LabelFrame(scrollable_frame, text="💑 Conseil Amoureux", padding="20")
        conseil_frame.pack(fill=tk.X, padx=20, pady=10)
        
        conseil_text = f"""
Votre signe {signe_perso.nom} s'accorde particulièrement bien avec :
• Les {signe_perso.element}s de même élément
• Les signes complémentaires de votre polarité

🔮 Astuce : Portez votre cristal de destinée pour amplifier votre magnétisme amoureux !
        """
        ttk.Label(conseil_frame, text=conseil_text, style='SubHeading.TLabel', 
                 justify=tk.LEFT, wraplength=600).pack(anchor=tk.W)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def remplir_bien_etre(self, parent):
        """Remplir l'onglet bien-être et conseils"""
        canvas = tk.Canvas(parent, bg=self.BG_PRIMARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        titre = ttk.Label(scrollable_frame, text="🧘 Bien-être & Mode de Vie 🧘", style='Title.TLabel')
        titre.pack(pady=20)
        
        signe = self.profil['signe']
        
        # Conseil d'aujourd'hui
        conseil_frame = ttk.LabelFrame(scrollable_frame, text="✨ Conseil Bien-être d'Aujourd'hui", padding="20")
        conseil_frame.pack(fill=tk.X, padx=20, pady=10)
        
        conseil = CONSEILS_BIEN_ETRE[signe.element]
        ttk.Label(conseil_frame, text=conseil, style='SubHeading.TLabel', 
                 justify=tk.LEFT, wraplength=600).pack(anchor=tk.W)
        
        # Influence lunaire
        lune_frame = ttk.LabelFrame(scrollable_frame, text="🌙 Influence de la Lune", padding="20")
        lune_frame.pack(fill=tk.X, padx=20, pady=10)
        
        phases = list(INFLUENCES_LUNAIRES.items())
        phase_alea = random.choice(phases)
        
        lune_text = f"""
Phase Lunaire Actuelle Recommandée : {phase_alea[0]}
{phase_alea[1]}

💡 Astuce : Synchronisez votre vie avec les cycles lunaires pour une meilleure harmonie.
        """
        ttk.Label(lune_frame, text=lune_text, style='Info.TLabel', 
                 justify=tk.LEFT, wraplength=600).pack(anchor=tk.W)
        
        # Guide de bien-être
        guide_frame = ttk.LabelFrame(scrollable_frame, text="🌿 Guide Pratique par Élément", padding="20")
        guide_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        element_guides = {
            "Feu": """
🔥 POUR LES SIGNES DE FEU (Bélier, Lion, Sagittaire) :
• Activité physique intense (sport, danse)
• Méditation en plein soleil
• Pierres rouges/oranges (Cornaline, Rubis)
• Éviter l'épuisement - intégrez du repos régulier
            """,
            "Terre": """
🌍 POUR LES SIGNES DE TERRE (Taureau, Vierge, Capricorne) :
• Marche en nature, jardinage
• Yoga lent et restaurateur
• Pierres vertes (Émeraude, Jade)
• Ancrez-vous avec des rituels quotidiens
            """,
            "Air": """
💨 POUR LES SIGNES D'AIR (Gémeaux, Balance, Verseau) :
• Yoga dynamique, danse
• Respiration consciente
• Pierres bleues (Saphir, Turquoise)
• Écoutez votre intuition mentale
            """,
            "Eau": """
💧 POUR LES SIGNES D'EAU (Cancer, Scorpion, Poissons) :
• Yoga yin, méditation profonde
• Bains relaxants
• Pierres roses/mauves (Améthyste, Quartz rose)
• Honorer votre sensibilité émotionnelle
            """
        }
        
        guide_text = element_guides.get(signe.element, "")
        ttk.Label(guide_frame, text=guide_text, style='Info.TLabel', 
                 justify=tk.LEFT, wraplength=600).pack(anchor=tk.W)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


# ────────────────────────────────────────────────────────────────────────────
# POINT D'ENTRÉE
# ────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = AstrologyApp()
    app.mainloop()
