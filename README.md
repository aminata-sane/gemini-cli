# 🤖 Gemini CLI

Un outil de ligne de commande élégant et interactif pour interagir avec l'IA Google Gemini, inspiré de l'interface Copilot.

![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Gemini](https://img.shields.io/badge/Gemini-2.5--Flash-orange.svg)

## 📋 Description

Gemini CLI est une interface en ligne de commande qui vous permet de poser des questions à l'IA Google Gemini directement depuis votre terminal. Avec un design élégant utilisant Rich pour l'affichage, et un streaming en temps réel des réponses, c'est l'outil parfait pour vos interactions avec l'IA.

## ✨ Fonctionnalités

- 🚀 **Streaming en temps réel** : Réponses affichées au fur et à mesure
- 🎨 **Interface élégante** : Panneaux colorés pour différencier les entrées et réponses
- 🔄 **Historique de conversation** : Maintien du contexte entre les questions
- ⚡ **Rapide et léger** : Utilise le modèle Gemini 2.5 Flash
- 🐍 **Python moderne** : Construit avec Python 3.14 et les dernières bibliothèques

## 🛠️ Installation

### Prérequis

- macOS (ou Linux/Windows avec adaptations)
- [Homebrew](https://brew.sh/) installé
- Clé API Google Gemini (obtenue sur [Google AI Studio](https://aistudio.google.com/))

### Étapes d'installation

1. **Clonez le repository**
   ```bash
   git clone https://github.com/votre-username/gemini-cli.git
   cd gemini-cli
   ```

2. **Installez Python 3.14**
   ```bash
   brew install python
   ```

3. **Créez l'environnement virtuel**
   ```bash
   /opt/homebrew/bin/python3 -m venv .venv
   ```

4. **Activez l'environnement et installez les dépendances**
   ```bash
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Configurez votre clé API**
   Créez un fichier `.env` à la racine du projet :
   ```env
   GEMINI_API_KEY=votre_clé_api_ici
   ```

6. **Ajoutez l'alias global (optionnel mais recommandé)**
   ```bash
   echo 'alias gemini="cd /chemin/vers/gemini-cli && PYTHONNOUSERSITE=1 source .venv/bin/activate && python3 gemini.py"' >> ~/.zshrc
   source ~/.zshrc
   ```

## 🚀 Utilisation

### Mode commande
```bash
gemini "Explique-moi le concept d'intelligence artificielle"
```

### Mode interactif (si vous modifiez le script)
```bash
python3 gemini.py
# Puis tapez vos questions dans l'interface
```

### Exemples de sortie
```
── User Input ──
╭────────────────────────────────────╮
│ Explique-moi Python en 2 phrases   │
╰────────────────────────────────────╯

── Gemini Copilot ──
╭──────────────────────────────────────────────────────────────────────────────╮
│ Python est un langage de programmation interprété, orienté objet et de haut │
│ niveau, connu pour sa syntaxe claire et lisible. Il est largement utilisé    │
│ pour le développement web, l'analyse de données, l'IA et bien plus encore.   │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## ⚙️ Configuration

### Variables d'environnement
- `GEMINI_API_KEY` : Votre clé API Google Gemini (obligatoire)

### Personnalisation
Vous pouvez modifier le script `gemini.py` pour :
- Changer le modèle Gemini utilisé
- Ajuster les couleurs et styles d'affichage
- Ajouter des fonctionnalités supplémentaires

## 📁 Structure du projet

```
gemini-cli/
├── gemini.py          # Script principal
├── requirements.txt   # Dépendances Python
├── .env               # Configuration (non versionné)
├── .gitignore         # Fichiers à ignorer
├── Documentation.md   # Documentation détaillée
└── README.md          # Ce fichier
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- [Google Gemini](https://ai.google.dev/) pour l'API IA
- [Rich](https://github.com/Textualize/rich) pour l'affichage terminal
- [Prompt Toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) pour l'interface interactive

## 📞 Support

Si vous avez des questions ou rencontrez des problèmes :
- Ouvrez une issue sur GitHub
- Consultez la [Documentation.md](Documentation.md) pour plus de détails

---

⭐ Si ce projet vous plaît, n'hésitez pas à lui donner une étoile !</content>
<parameter name="filePath">/Users/mameaminataconstancesane/Desktop/gemini-cli/README.md