#!/usr/bin/env python3
"""
Générateur de voix du Père Noël avec OpenAI TTS
Génère un fichier MP3 avec un message de Noël du Père Noël
"""

import sys
import os

try:
    from openai import OpenAI
except ImportError:
    print("❌ Erreur: Le module 'openai' n'est pas installé.")
    print("Installez-le avec: pip install openai")
    sys.exit(1)

# Vérifier que la clé API est définie
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ Erreur: La variable d'environnement OPENAI_API_KEY n'est pas définie.")
    print("Définissez-la avec: export OPENAI_API_KEY='votre-clé-api'")
    sys.exit(1)

try:
    client = OpenAI(api_key=api_key)
    
    # Message du Père Noël en français
    text = """
    Ho ho ho ! 
    Bonjour à tous les petits et les grands enfants.
    C'est moi, le Père Noël.
    Je vous souhaite un merveilleux Noël, rempli de joie, de surprises et de moments magiques.
    Prenez soin de vous et de vos proches… et n'oubliez pas les biscuits pour moi.
    Ho ho ho ! Joyeux Noël !
    """
    
    print("🎄 Génération de la voix du Père Noël...")
    
    # Appel à l'API OpenAI Text-to-Speech
    # Voix disponibles: alloy, echo, fable, onyx, nova, shimmer, coral, verse, ballad, ash, sage, marin, cedar
    response = client.audio.speech.create(
        model="tts-1-hd",      # Modèle de haute qualité
        voice="onyx",           # Voix grave et joviale (père noël)
        input=text,
        speed=0.9              # Légèrement plus lent pour un effet jovial
    )
    
    # Écrire le fichier audio
    output_file = "pere-noel.mp3"
    with open(output_file, "wb") as f:
        f.write(response.content)
    
    print(f"✅ Succès! Audio généré: {output_file}")
    
except FileNotFoundError:
    print("❌ Erreur: Impossible de créer le fichier de sortie")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erreur lors de la génération: {str(e)}")
    sys.exit(1)
