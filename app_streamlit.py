#!/usr/bin/env python3
"""
✨ Astrologie & Pierres de Pouvoir — Version Streamlit
Lancez avec : streamlit run app_streamlit.py
"""

import streamlit as st
from datetime import date, datetime
from enum import Enum
import random

# ─────────────────────────────────────────────────────────────────────────────
# DONNÉES ASTROLOGIQUES (identiques à l'app originale)
# ─────────────────────────────────────────────────────────────────────────────

class Signe(Enum):
    BELIER     = ("Bélier",      (3, 21), (4, 19),  "Feu",   "Mars",    "♈")
    TAUREAU    = ("Taureau",     (4, 20), (5, 20),  "Terre", "Vénus",   "♉")
    GEMEAUX    = ("Gémeaux",     (5, 21), (6, 20),  "Air",   "Mercure", "♊")
    CANCER     = ("Cancer",      (6, 21), (7, 22),  "Eau",   "Lune",    "♋")
    LION       = ("Lion",        (7, 23), (8, 22),  "Feu",   "Soleil",  "♌")
    VIERGE     = ("Vierge",      (8, 23), (9, 22),  "Terre", "Mercure", "♍")
    BALANCE    = ("Balance",     (9, 23), (10, 22), "Air",   "Vénus",   "♎")
    SCORPION   = ("Scorpion",    (10, 23),(11, 21), "Eau",   "Pluton",  "♏")
    SAGITTAIRE = ("Sagittaire",  (11, 22),(12, 21), "Feu",   "Jupiter", "♐")
    CAPRICORNE = ("Capricorne",  (12, 22),(1, 19),  "Terre", "Saturne", "♑")
    VERSEAU    = ("Verseau",     (1, 20), (2, 18),  "Air",   "Uranus",  "♒")
    POISSONS   = ("Poissons",    (2, 19), (3, 20),  "Eau",   "Neptune", "♓")

    def __init__(self, nom, date_debut, date_fin, element, planete, symbole):
        self.nom        = nom
        self.date_debut = date_debut
        self.date_fin   = date_fin
        self.element    = element
        self.planete    = planete
        self.symbole    = symbole


PIERRES_PAR_SIGNE = {
    Signe.BELIER:     [{"nom": "Cornaline",       "proprietes": "Courage, énergie, confiance",           "couleur": "Rouge-orange"},
                       {"nom": "Calcite rouge",    "proprietes": "Vitalité, passion, dynamisme",          "couleur": "Rouge"},
                       {"nom": "Jaspe rouge",      "proprietes": "Force, protection, ancrage",            "couleur": "Rouge"},
                       {"nom": "Diamant",          "proprietes": "Puissance, clarté mentale, invincibilité","couleur": "Incolore"}],
    Signe.TAUREAU:    [{"nom": "Émeraude",         "proprietes": "Stabilité, prospérité, amour",          "couleur": "Vert"},
                       {"nom": "Lapis-lazuli",     "proprietes": "Sagesse, communication, sérénité",      "couleur": "Bleu"},
                       {"nom": "Turquoise",        "proprietes": "Protection, équilibre, guérison",       "couleur": "Bleu-vert"},
                       {"nom": "Péridot",          "proprietes": "Abondance, protection, clarté",         "couleur": "Vert clair"}],
    Signe.GEMEAUX:    [{"nom": "Citrine",          "proprietes": "Intelligence, communication, joie",     "couleur": "Jaune"},
                       {"nom": "Agathe",           "proprietes": "Harmonie, équilibre, clarté",           "couleur": "Multicolore"},
                       {"nom": "Tourmaline noire", "proprietes": "Protection, ancrage",                   "couleur": "Noir"},
                       {"nom": "Béryl",            "proprietes": "Clarté mentale, éloquence",             "couleur": "Incolore"}],
    Signe.CANCER:     [{"nom": "Opale",            "proprietes": "Émotions, intuition, imagination",      "couleur": "Arc-en-ciel"},
                       {"nom": "Pierre de lune",   "proprietes": "Douceur, intuition, féminité",          "couleur": "Blanc laiteux"},
                       {"nom": "Calcite blanche",  "proprietes": "Pureté, clarté énergétique",            "couleur": "Blanc"},
                       {"nom": "Perle",            "proprietes": "Sagesse, douceur, guérison émotionnelle","couleur": "Blanc"}],
    Signe.LION:       [{"nom": "Or",               "proprietes": "Rayonnement, confiance, majesté",       "couleur": "Or"},
                       {"nom": "Cristal de roche", "proprietes": "Clarté, puissance, amplification",      "couleur": "Incolore"},
                       {"nom": "Rubis",            "proprietes": "Passion, leadership, vitalité",         "couleur": "Rouge"},
                       {"nom": "Ambre",            "proprietes": "Chaleur, soleil, transformation",       "couleur": "Ambre"}],
    Signe.VIERGE:     [{"nom": "Saphir bleu",      "proprietes": "Sagesse, sincérité, clarté",            "couleur": "Bleu"},
                       {"nom": "Jade vert",        "proprietes": "Purification, guérison, équilibre",     "couleur": "Vert"},
                       {"nom": "Sodalite",         "proprietes": "Logique, harmonie intérieure",          "couleur": "Bleu"},
                       {"nom": "Améthyste",        "proprietes": "Sérénité, sagesse, équilibre",          "couleur": "Violet"}],
    Signe.BALANCE:    [{"nom": "Opale",            "proprietes": "Équilibre, beauté, harmonie",           "couleur": "Arc-en-ciel"},
                       {"nom": "Lépidolite",       "proprietes": "Sérénité, équilibre émotionnel",        "couleur": "Violet"},
                       {"nom": "Rose quartz",      "proprietes": "Amour, douceur, harmonie",              "couleur": "Rose"},
                       {"nom": "Aventurine verte", "proprietes": "Prospérité, sérénité",                  "couleur": "Vert"}],
    Signe.SCORPION:   [{"nom": "Obsidienne noire", "proprietes": "Protection, transformation, profondeur","couleur": "Noir"},
                       {"nom": "Hématite",         "proprietes": "Vitalité, ancrage, purification",       "couleur": "Rouge-noir"},
                       {"nom": "Malachite",        "proprietes": "Transformation, protection psychique",  "couleur": "Vert"},
                       {"nom": "Tourmaline noire", "proprietes": "Purification psychique, protection",    "couleur": "Noir"}],
    Signe.SAGITTAIRE: [{"nom": "Topaze bleue",     "proprietes": "Sagesse, communication, guérison",      "couleur": "Bleu"},
                       {"nom": "Lapis-lazuli",     "proprietes": "Voyage, sagesse, protection",           "couleur": "Bleu"},
                       {"nom": "Citrine",          "proprietes": "Abondance, optimisme, chance",          "couleur": "Jaune"},
                       {"nom": "Turquoise",        "proprietes": "Protection du voyageur, sagesse",       "couleur": "Bleu-vert"}],
    Signe.CAPRICORNE: [{"nom": "Grenat",           "proprietes": "Discipline, persévérance, ancrage",     "couleur": "Rouge-noir"},
                       {"nom": "Onyx noir",        "proprietes": "Ancrage, protection, force intérieure", "couleur": "Noir"},
                       {"nom": "Tourmaline noire", "proprietes": "Résilience, grounding",                 "couleur": "Noir"},
                       {"nom": "Fluorite noire",   "proprietes": "Ordre, clarté, structure",              "couleur": "Noir-violet"}],
    Signe.VERSEAU:    [{"nom": "Améthyste",        "proprietes": "Intuition, spiritualité, innovation",   "couleur": "Violet"},
                       {"nom": "Fluorite violette","proprietes": "Conscience, spiritualité, clarté",      "couleur": "Violet"},
                       {"nom": "Labradorite",      "proprietes": "Intuition, protection, transformation", "couleur": "Gris-bleu"},
                       {"nom": "Tourmaline élect.","proprietes": "Innovation, énergie future",            "couleur": "Noir"}],
    Signe.POISSONS:   [{"nom": "Améthyste",        "proprietes": "Intuition, spiritualité, sensibilité",  "couleur": "Violet"},
                       {"nom": "Calcédoine rose",  "proprietes": "Douceur, compassion, guérison",         "couleur": "Rose"},
                       {"nom": "Fluorite verte",   "proprietes": "Équilibre émotionnel, guérison",        "couleur": "Vert"},
                       {"nom": "Aigue-marine",     "proprietes": "Fluidité, clarté, paix intérieure",     "couleur": "Bleu clair"}],
}

CHAKRAS_PAR_SIGNE = {
    Signe.BELIER:     {"nom": "Chakra Racine",           "couleur": "🔴 Rouge",       "localisation": "Base de la colonne vertébrale"},
    Signe.TAUREAU:    {"nom": "Chakra Racine",           "couleur": "🔴 Rouge",       "localisation": "Base de la colonne vertébrale"},
    Signe.GEMEAUX:    {"nom": "Chakra Laryngé",          "couleur": "🔵 Bleu ciel",   "localisation": "Gorge"},
    Signe.CANCER:     {"nom": "Chakra du Cœur",          "couleur": "💚 Rose/Vert",   "localisation": "Cœur"},
    Signe.LION:       {"nom": "Chakra du Plexus Solaire","couleur": "🟡 Jaune doré",  "localisation": "Fosse à l'estomac"},
    Signe.VIERGE:     {"nom": "Chakra du Plexus Solaire","couleur": "🟡 Jaune doré",  "localisation": "Fosse à l'estomac"},
    Signe.BALANCE:    {"nom": "Chakra du Cœur",          "couleur": "💚 Rose/Vert",   "localisation": "Cœur"},
    Signe.SCORPION:   {"nom": "Chakra Sacré",            "couleur": "🟠 Orange",      "localisation": "Bas-ventre"},
    Signe.SAGITTAIRE: {"nom": "Chakra du Troisième Œil", "couleur": "🟣 Indigo",      "localisation": "Front"},
    Signe.CAPRICORNE: {"nom": "Chakra Racine",           "couleur": "🔴 Rouge",       "localisation": "Base de la colonne vertébrale"},
    Signe.VERSEAU:    {"nom": "Chakra Laryngé",          "couleur": "🔵 Bleu ciel",   "localisation": "Gorge"},
    Signe.POISSONS:   {"nom": "Chakra de la Couronne",   "couleur": "🟣 Violet",      "localisation": "Sommet du crâne"},
}

COULEURS_SIGNE = {
    Signe.BELIER:     ["Rouge", "Blanc", "Or"],
    Signe.TAUREAU:    ["Vert", "Rose", "Bleu"],
    Signe.GEMEAUX:    ["Jaune", "Gris", "Blanc"],
    Signe.CANCER:     ["Blanc", "Argent", "Crème"],
    Signe.LION:       ["Or", "Rouge", "Jaune"],
    Signe.VIERGE:     ["Vert", "Beige", "Marron"],
    Signe.BALANCE:    ["Rose", "Bleu ciel", "Blanc"],
    Signe.SCORPION:   ["Rouge", "Noir", "Marron"],
    Signe.SAGITTAIRE: ["Violet", "Bleu", "Vert"],
    Signe.CAPRICORNE: ["Noir", "Gris", "Marron"],
    Signe.VERSEAU:    ["Turquoise", "Bleu électrique", "Argent"],
    Signe.POISSONS:   ["Turquoise", "Violet", "Vert clair"],
}

MANTRAS_PAR_SIGNE = {
    Signe.BELIER:     "Je suis courageux et je fonce avec confiance vers mes objectifs.",
    Signe.TAUREAU:    "Je suis stable, grounded et j'attire l'abondance dans ma vie.",
    Signe.GEMEAUX:    "Je communique avec clarté et je suis curieux du monde.",
    Signe.CANCER:     "Je suis protégé par mon intuition et ma sensibilité est ma force.",
    Signe.LION:       "Je rayonne avec confiance et j'inspire ceux qui m'entourent.",
    Signe.VIERGE:     "Je suis conscient et je cultive l'harmonie en moi et autour de moi.",
    Signe.BALANCE:    "Je cherche l'équilibre et je crée plus de beauté dans le monde.",
    Signe.SCORPION:   "Je me transforme constamment et je maîtrise ma destinée.",
    Signe.SAGITTAIRE: "Je suis libre et j'explore les frontières infinies de la vie.",
    Signe.CAPRICORNE: "Je suis persévérant et j'édifie un futur solide et prospère.",
    Signe.VERSEAU:    "Je suis unique et je révolutionne le monde avec mes idées.",
    Signe.POISSONS:   "Je flotte avec grâce et ma compassion guérit le monde.",
}

COMPATIBILITE_AMOUREUSE = {
    Signe.BELIER:     {Signe.BELIER:4, Signe.TAUREAU:2, Signe.GEMEAUX:4, Signe.CANCER:2,  Signe.LION:5,    Signe.VIERGE:2,    Signe.BALANCE:3,    Signe.SCORPION:3,  Signe.SAGITTAIRE:5, Signe.CAPRICORNE:2, Signe.VERSEAU:4,  Signe.POISSONS:2},
    Signe.TAUREAU:    {Signe.BELIER:2, Signe.TAUREAU:4, Signe.GEMEAUX:2, Signe.CANCER:5,  Signe.LION:2,    Signe.VIERGE:5,    Signe.BALANCE:3,    Signe.SCORPION:4,  Signe.SAGITTAIRE:2, Signe.CAPRICORNE:5, Signe.VERSEAU:2,  Signe.POISSONS:4},
    Signe.GEMEAUX:    {Signe.BELIER:4, Signe.TAUREAU:2, Signe.GEMEAUX:4, Signe.CANCER:2,  Signe.LION:3,    Signe.VIERGE:4,    Signe.BALANCE:5,    Signe.SCORPION:2,  Signe.SAGITTAIRE:5, Signe.CAPRICORNE:2, Signe.VERSEAU:5,  Signe.POISSONS:2},
    Signe.CANCER:     {Signe.BELIER:2, Signe.TAUREAU:5, Signe.GEMEAUX:2, Signe.CANCER:4,  Signe.LION:2,    Signe.VIERGE:4,    Signe.BALANCE:3,    Signe.SCORPION:5,  Signe.SAGITTAIRE:2, Signe.CAPRICORNE:4, Signe.VERSEAU:2,  Signe.POISSONS:5},
    Signe.LION:       {Signe.BELIER:5, Signe.TAUREAU:2, Signe.GEMEAUX:3, Signe.CANCER:2,  Signe.LION:4,    Signe.VIERGE:2,    Signe.BALANCE:5,    Signe.SCORPION:2,  Signe.SAGITTAIRE:5, Signe.CAPRICORNE:2, Signe.VERSEAU:3,  Signe.POISSONS:2},
    Signe.VIERGE:     {Signe.BELIER:2, Signe.TAUREAU:5, Signe.GEMEAUX:4, Signe.CANCER:4,  Signe.LION:2,    Signe.VIERGE:4,    Signe.BALANCE:3,    Signe.SCORPION:4,  Signe.SAGITTAIRE:2, Signe.CAPRICORNE:5, Signe.VERSEAU:2,  Signe.POISSONS:4},
    Signe.BALANCE:    {Signe.BELIER:3, Signe.TAUREAU:3, Signe.GEMEAUX:5, Signe.CANCER:3,  Signe.LION:5,    Signe.VIERGE:3,    Signe.BALANCE:4,    Signe.SCORPION:2,  Signe.SAGITTAIRE:4, Signe.CAPRICORNE:2, Signe.VERSEAU:5,  Signe.POISSONS:3},
    Signe.SCORPION:   {Signe.BELIER:3, Signe.TAUREAU:4, Signe.GEMEAUX:2, Signe.CANCER:5,  Signe.LION:2,    Signe.VIERGE:4,    Signe.BALANCE:2,    Signe.SCORPION:4,  Signe.SAGITTAIRE:2, Signe.CAPRICORNE:4, Signe.VERSEAU:2,  Signe.POISSONS:5},
    Signe.SAGITTAIRE: {Signe.BELIER:5, Signe.TAUREAU:2, Signe.GEMEAUX:5, Signe.CANCER:2,  Signe.LION:5,    Signe.VIERGE:2,    Signe.BALANCE:4,    Signe.SCORPION:2,  Signe.SAGITTAIRE:4, Signe.CAPRICORNE:2, Signe.VERSEAU:5,  Signe.POISSONS:2},
    Signe.CAPRICORNE: {Signe.BELIER:2, Signe.TAUREAU:5, Signe.GEMEAUX:2, Signe.CANCER:4,  Signe.LION:2,    Signe.VIERGE:5,    Signe.BALANCE:2,    Signe.SCORPION:4,  Signe.SAGITTAIRE:2, Signe.CAPRICORNE:4, Signe.VERSEAU:2,  Signe.POISSONS:3},
    Signe.VERSEAU:    {Signe.BELIER:4, Signe.TAUREAU:2, Signe.GEMEAUX:5, Signe.CANCER:2,  Signe.LION:3,    Signe.VIERGE:2,    Signe.BALANCE:5,    Signe.SCORPION:2,  Signe.SAGITTAIRE:5, Signe.CAPRICORNE:2, Signe.VERSEAU:4,  Signe.POISSONS:3},
    Signe.POISSONS:   {Signe.BELIER:2, Signe.TAUREAU:4, Signe.GEMEAUX:2, Signe.CANCER:5,  Signe.LION:2,    Signe.VIERGE:4,    Signe.BALANCE:3,    Signe.SCORPION:5,  Signe.SAGITTAIRE:2, Signe.CAPRICORNE:3, Signe.VERSEAU:3,  Signe.POISSONS:4},
}

INFLUENCES_LUNAIRES = {
    "🌑 Lune Nouvelle":    "Idéal pour débuter de nouveaux projets et prendre des décisions.",
    "🌒 Lune Croissante":  "Amplifiez vos efforts et manifestez vos intentions.",
    "🌕 Pleine Lune":      "État d'énergie maximal, perfectionnez ce que vous avez commencé.",
    "🌘 Lune Décroissante":"Moment de lâcher-prise et d'introspection.",
}

CONSEILS_BIEN_ETRE = {
    "Feu":   "🔥 Canalisez votre énergie avec de l'exercice intensif. Portez des pierres rouges pour intensifier votre feu intérieur.",
    "Terre": "🌍 Connectez-vous à la Nature. Marchez pieds nus, méditez dehors. Portez du vert pour rester ancré.",
    "Air":   "💨 Respirez profondément et pratiquez le yoga. Portez du bleu pour favoriser la clarté mentale.",
    "Eau":   "💧 Pratiquez l'auto-compassion et la méditation. Prenez un bain apaisant. Portez du rose/blanc pour la sérénité.",
}

CRISTAL_DE_NAISSANCE_MOIS = {
    1:"Grenat", 2:"Améthyste", 3:"Aigue-marine", 4:"Diamant",
    5:"Émeraude", 6:"Perle", 7:"Rubis", 8:"Péridot",
    9:"Saphir", 10:"Opale", 11:"Topaze", 12:"Turquoise",
}

PROPRIETES_CRISTAL_MOIS = {
    1:"Protection et Force", 2:"Sérénité et Spiritualité", 3:"Guérison et Sérénité",
    4:"Pureté et Incorruptibilité", 5:"Amour et Succès", 6:"Pureté et Protection",
    7:"Passion et Prospérité", 8:"Vitalité et Chance", 9:"Sagesse et Sincérité",
    10:"Espoir et Imagination", 11:"Prospérité et Guérison", 12:"Voyage et Paix",
}

DESCRIPTIONS_ELEMENTS = {
    "Feu":   "Passion, dynamisme, créativité",
    "Terre": "Stabilité, pragmatisme, ancrage",
    "Air":   "Communication, intellect, liberté",
    "Eau":   "Émotions, intuition, compassion",
}

EMOJI_ELEMENT = {"Feu": "🔥", "Terre": "🌍", "Air": "💨", "Eau": "💧"}


# ─────────────────────────────────────────────────────────────────────────────
# LOGIQUE MÉTIER
# ─────────────────────────────────────────────────────────────────────────────

def determiner_signe(jour: int, mois: int) -> Signe:
    date_check = (mois, jour)
    for signe in Signe:
        debut, fin = signe.date_debut, signe.date_fin
        if debut[0] > fin[0]:
            if date_check >= debut or date_check <= fin:
                return signe
        else:
            if debut <= date_check <= fin:
                return signe
    return Signe.BELIER


def calculer_age(date_naissance: date) -> int:
    aujourd_hui = date.today()
    age = aujourd_hui.year - date_naissance.year
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1
    return age


def phase_lunaire_actuelle() -> str:
    phases = list(INFLUENCES_LUNAIRES.keys())
    idx = (date.today().day // 7) % 4
    return phases[idx]


# ─────────────────────────────────────────────────────────────────────────────
# INTERFACE STREAMLIT
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="✨ Astrologie & Pierres",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS personnalisé ──────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Fond général */
    .stApp { background-color: #0a0e27; color: #ffffff; }

    /* Titre principal */
    h1 { color: #c77dff !important; text-align: center; }
    h2 { color: #d8b3ff !important; }
    h3 { color: #00d9ff !important; }

    /* Cartes */
    .card {
        background: #1a1f3a;
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #2d3561;
    }
    .card-pierre {
        background: #2d3561;
        border-radius: 12px;
        padding: 14px;
        margin: 6px 0;
        border-left: 4px solid #c77dff;
    }
    .mantra {
        background: linear-gradient(135deg, #1a1f3a, #2d3561);
        border-radius: 12px;
        padding: 18px;
        border-left: 4px solid #00d9ff;
        font-style: italic;
        font-size: 1.05rem;
    }
    .coeur { color: #ff6b9d; font-size: 1.3rem; }
    .label { color: #b4b9d1; font-size: 0.9rem; }

    /* Bouton */
    .stButton>button {
        background: linear-gradient(135deg, #5a4fcf, #c77dff);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 32px;
        font-size: 1.1rem;
        font-weight: bold;
        width: 100%;
        cursor: pointer;
    }
    .stButton>button:hover { opacity: 0.9; }

    /* Inputs */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>select,
    .stDateInput>div>div>input {
        background-color: #1a1f3a !important;
        color: #ffffff !important;
        border: 1px solid #2d3561 !important;
        border-radius: 8px !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] { color: #b4b9d1; }
    .stTabs [aria-selected="true"] { color: #c77dff !important; border-bottom-color: #c77dff !important; }

    /* Séparateur */
    hr { border-color: #2d3561; }
</style>
""", unsafe_allow_html=True)


# ── En-tête ───────────────────────────────────────────────────────────────────
st.markdown("# ✨ Astrologie & Pierres de Pouvoir")
st.markdown("<p style='text-align:center; color:#b4b9d1;'>Découvrez votre destinée astrale</p>", unsafe_allow_html=True)
st.markdown("---")


# ── Formulaire ────────────────────────────────────────────────────────────────
with st.container():
    st.markdown("## 👤 Informations Personnelles")
    col1, col2 = st.columns(2)
    with col1:
        nom     = st.text_input("Nom", placeholder="Votre nom de famille")
        prenoms = st.text_input("Prénom(s)", placeholder="Votre prénom")
    with col2:
        date_naissance = st.date_input(
            "Date de naissance",
            value=date(1995, 6, 15),
            min_value=date(1900, 1, 1),
            max_value=date.today(),
        )
        noms_signes = [s.nom for s in Signe]
        signe_amour_nom = st.selectbox(
            "💕 Compatibilité avec (optionnel)",
            options=["-- Aucun --"] + noms_signes,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    lancer = st.button("🚀 Découvrir mon Thème Astral")


# ── Résultats ─────────────────────────────────────────────────────────────────
if lancer:
    if not nom or not prenoms:
        st.error("⚠️ Veuillez renseigner votre nom et prénom.")
    else:
        signe      = determiner_signe(date_naissance.day, date_naissance.month)
        age        = calculer_age(date_naissance)
        nom_complet = f"{prenoms} {nom}"
        chakra     = CHAKRAS_PAR_SIGNE[signe]
        pierres    = PIERRES_PAR_SIGNE[signe]
        cristal    = CRISTAL_DE_NAISSANCE_MOIS[date_naissance.month]
        prop_cristal = PROPRIETES_CRISTAL_MOIS[date_naissance.month]
        phase      = phase_lunaire_actuelle()
        emoji_elem = EMOJI_ELEMENT[signe.element]

        st.markdown("---")

        # ── Onglets de résultats ──────────────────────────────────────────────
        tab1, tab2, tab3, tab4 = st.tabs([
            "🌟 Profil Astral",
            "💎 Pierres & Chakras",
            "💕 Compatibilité",
            "🧘 Bien-être",
        ])

        # ────── TAB 1 : Profil ────────────────────────────────────────────────
        with tab1:
            st.markdown(f"## {signe.symbole} Profil de {nom_complet}")

            col_a, col_b, col_c, col_d = st.columns(4)
            col_a.metric("Signe", f"{signe.symbole} {signe.nom}")
            col_b.metric("Élément", f"{emoji_elem} {signe.element}")
            col_c.metric("Planète", f"🪐 {signe.planete}")
            col_d.metric("Âge", f"{age} ans")

            st.markdown("<br>", unsafe_allow_html=True)

            col_l, col_r = st.columns(2)

            with col_l:
                st.markdown(f"""
                <div class='card'>
                    <h3>🔮 Informations Générales</h3>
                    <p><span class='label'>Nom complet :</span> <b>{nom_complet}</b></p>
                    <p><span class='label'>Date de naissance :</span> <b>{date_naissance.strftime('%d %B %Y')}</b></p>
                    <p><span class='label'>Signe astrologique :</span> <b>{signe.symbole} {signe.nom}</b></p>
                    <p><span class='label'>Élément :</span> <b>{emoji_elem} {signe.element}</b> — {DESCRIPTIONS_ELEMENTS[signe.element]}</p>
                    <p><span class='label'>Planète dominante :</span> <b>🪐 {signe.planete}</b></p>
                </div>
                """, unsafe_allow_html=True)

            with col_r:
                couleurs = COULEURS_SIGNE[signe]
                st.markdown(f"""
                <div class='card'>
                    <h3>🌈 Couleurs Porte-Bonheur</h3>
                    <p>{"  •  ".join(f"<b>{c}</b>" for c in couleurs)}</p>
                    <br>
                    <h3>{phase}</h3>
                    <p>{INFLUENCES_LUNAIRES[phase]}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class='mantra'>
                💬 <b>Mantra du jour :</b><br><br>
                « {MANTRAS_PAR_SIGNE[signe]} »
            </div>
            """, unsafe_allow_html=True)

        # ────── TAB 2 : Pierres & Chakras ────────────────────────────────────
        with tab2:
            st.markdown(f"## 💎 Pierres de Pouvoir — {signe.symbole} {signe.nom}")

            cols = st.columns(2)
            for i, pierre in enumerate(pierres):
                with cols[i % 2]:
                    st.markdown(f"""
                    <div class='card-pierre'>
                        <b>💎 {pierre['nom']}</b><br>
                        <span class='label'>Couleur :</span> {pierre['couleur']}<br>
                        <span class='label'>Propriétés :</span> {pierre['proprietes']}
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            col_ch, col_cr = st.columns(2)

            with col_ch:
                st.markdown(f"""
                <div class='card'>
                    <h3>🌀 Chakra Principal</h3>
                    <p><b>{chakra['nom']}</b></p>
                    <p><span class='label'>Couleur :</span> {chakra['couleur']}</p>
                    <p><span class='label'>Localisation :</span> {chakra['localisation']}</p>
                </div>
                """, unsafe_allow_html=True)

            with col_cr:
                st.markdown(f"""
                <div class='card'>
                    <h3>💠 Cristal de Naissance</h3>
                    <p><b>{cristal}</b></p>
                    <p><span class='label'>Mois :</span> {date_naissance.strftime('%B')}</p>
                    <p><span class='label'>Propriétés :</span> {prop_cristal}</p>
                </div>
                """, unsafe_allow_html=True)

        # ────── TAB 3 : Compatibilité ─────────────────────────────────────────
        with tab3:
            st.markdown(f"## 💕 Compatibilité Amoureuse — {signe.symbole} {signe.nom}")

            # Compatibilité avec le signe choisi dans le formulaire
            if signe_amour_nom != "-- Aucun --":
                signe_amour = next(s for s in Signe if s.nom == signe_amour_nom)
                score = COMPATIBILITE_AMOUREUSE[signe][signe_amour]
                coeurs = "❤️" * score + "🤍" * (5 - score)
                st.markdown(f"""
                <div class='card' style='text-align:center;'>
                    <h3>{signe.symbole} {signe.nom} + {signe_amour.symbole} {signe_amour.nom}</h3>
                    <p style='font-size:2rem;'>{coeurs}</p>
                    <p><b>{score}/5</b> — {'Affinité exceptionnelle ✨' if score == 5 else 'Bonne compatibilité 💫' if score >= 3 else 'Compatibilité modérée 🌙'}</p>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)

            # Tableau complet
            st.markdown("### Compatibilité avec tous les signes")
            cols = st.columns(3)
            signes_list = list(Signe)
            for i, autre_signe in enumerate(signes_list):
                score = COMPATIBILITE_AMOUREUSE[signe][autre_signe]
                coeurs = "❤️" * score + "🤍" * (5 - score)
                with cols[i % 3]:
                    st.markdown(f"""
                    <div class='card-pierre'>
                        <b>{autre_signe.symbole} {autre_signe.nom}</b><br>
                        {coeurs}
                    </div>
                    """, unsafe_allow_html=True)

        # ────── TAB 4 : Bien-être ─────────────────────────────────────────────
        with tab4:
            st.markdown(f"## 🧘 Bien-être & Conseils — {emoji_elem} {signe.element}")

            st.markdown(f"""
            <div class='card'>
                <h3>🌿 Conseil du Jour</h3>
                <p style='font-size:1.05rem;'>{CONSEILS_BIEN_ETRE[signe.element]}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            col_lune, col_mantra = st.columns(2)
            with col_lune:
                st.markdown(f"""
                <div class='card'>
                    <h3>🌙 Influence Lunaire</h3>
                    <p><b>{phase}</b></p>
                    <p>{INFLUENCES_LUNAIRES[phase]}</p>
                </div>
                """, unsafe_allow_html=True)

            with col_mantra:
                st.markdown(f"""
                <div class='card'>
                    <h3>💬 Mantra Personnel</h3>
                    <p style='font-style:italic;'>« {MANTRAS_PAR_SIGNE[signe]} »</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 🌈 Résumé de votre Profil")
            st.markdown(f"""
            <div class='card'>
                <p>✦ <b>Signe :</b> {signe.symbole} {signe.nom} &nbsp;|&nbsp;
                   <b>Élément :</b> {emoji_elem} {signe.element} &nbsp;|&nbsp;
                   <b>Planète :</b> 🪐 {signe.planete}</p>
                <p>✦ <b>Chakra :</b> {chakra['nom']} ({chakra['couleur']})</p>
                <p>✦ <b>Pierre principale :</b> 💎 {pierres[0]['nom']} — {pierres[0]['proprietes']}</p>
                <p>✦ <b>Cristal de naissance :</b> 💠 {cristal} — {prop_cristal}</p>
                <p>✦ <b>Couleurs :</b> {', '.join(COULEURS_SIGNE[signe])}</p>
            </div>
            """, unsafe_allow_html=True)
