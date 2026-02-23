📘 Documentation : Installation de Gemini CLI sur macOS
Ce guide documente la configuration d'un environnement de développement local pour interagir avec l'API Google Gemini via Python.

1. Prérequis
Homebrew : Gestionnaire de paquets.

uv : Installateur de paquets Python ultra-rapide.

Clé API Gemini : À récupérer sur Google AI Studio.

2. Configuration de l'Espace de Travail
Bash
# Aller sur le Bureau
cd ~/Desktop

# Créer le dossier du projet
mkdir gemini-cli
cd gemini-cli

# Ouvrir le dossier dans VS Code
code .
3. Environnement Virtuel & Dépendances
Il est crucial d'utiliser un environnement virtuel pour ne pas interférer avec le système.

Bash
# Créer l'environnement virtuel avec uv
uv venv

# Activer l'environnement (à refaire à chaque réouverture de terminal)
source .venv/bin/activate

# Installer la bibliothèque officielle de Google
uv pip install -U google-generativeai
4. Création du Script gemini.py
Fichier à créer à la racine du dossier :

Python
import google.generativeai as genai
import sys

# Configuration de l'accès
genai.configure(api_key="VOTRE_CLE_API_ICI")

# Initialisation du modèle (Flash est rapide et léger)
model = genai.GenerativeModel('gemini-2.5-flash')

def main():
    # Récupérer l'argument passé en ligne de commande
    prompt = " ".join(sys.argv[1:])
    
    if not prompt:
        print("Usage: python gemini.py 'Votre question'")
        return

    # Génération de la réponse
    response = model.generate_content(prompt)
    print("\n--- Gemini CLI ---")
    print(response.text)

if __name__ == "__main__":
    main()
5. Utilisation
Pour poser une question à l'IA depuis le terminal :

Bash
python gemini.py "Explique-moi le concept de système multi-agents en deux phrases."
6. Astuces Terminal
Vérifier l'activation : Si tu vois (.venv) au début de ta ligne de commande, l'environnement est actif.

Désactiver : Tape deactivate.

Réactiver : source .venv/bin/activate (toujours depuis le dossier du projet).

# POUR LANCER L'APPLICATION

cd Desktop
cd gemini-cli
source .venv/bin/activate
gemini "et ici poser les questions ou ecrire les prompts..."