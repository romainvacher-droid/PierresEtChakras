#!/usr/bin/env python3
"""Créer une icône personnalisée pour l'application"""

from PIL import Image, ImageDraw, ImageFont

# Créer une image 256x256 avec dégradé de violet
img = Image.new('RGB', (256, 256), color='#0f1419')
draw = ImageDraw.Draw(img, 'RGBA')

# Ajouter un cercle violet clair en arrière-plan
draw.ellipse([20, 20, 236, 236], fill='#7c3aed', outline='#c77dff', width=3)

# Ajouter un dégradé plus clair au centre
draw.ellipse([40, 40, 216, 216], fill='#a78bfa', outline='#c77dff', width=2)

# Ajouter le texte en plein centre (star emoji ✨)
try:
    # Essayer avec une police système
    font = ImageFont.load_default()
    draw.text((85, 85), "✨", fill='#ffffff', font=font)
except:
    pass

# Sauvegarder en ICO
img.save('icon.ico')
print("✅ Icône créée : icon.ico")
