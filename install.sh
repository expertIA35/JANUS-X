#!/bin/bash

echo "========================================="
echo "🚀 JANUS-X - Installation automatique"
echo "========================================="
echo ""

# 1. Installer Ollama
echo "📦 Installation de Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# 2. Démarrer le serveur Ollama en arrière-plan
echo ""
echo "🔄 Démarrage du serveur Ollama..."
ollama serve &
sleep 5

# 3. Télécharger les modèles
echo ""
echo "📥 Téléchargement des modèles (cela peut prendre quelques minutes)..."
echo "   • Mistral 7B (4.1 Go)"
ollama pull mistral
echo "   • Llama 3.2 3B (3.2 Go)"
ollama pull llama3.2
echo "   • Phi-3 Mini (2.2 Go)"
ollama pull phi3
echo "   • Gemma 2B (1.8 Go)"
ollama pull gemma:2b

# 4. Installer les dépendances Python
echo ""
echo "🐍 Installation des dépendances Python..."
cd backend
pip install -r requirements.txt

# 5. Arrêter l'ancien serveur si nécessaire
echo ""
echo "🛑 Arrêt des anciens serveurs..."
pkill -f "python main.py"
sleep 2

# 6. Lancer le serveur
echo ""
echo "✅ Installation terminée !"
echo "🚀 Démarrage du serveur JANUS-X..."
echo ""
echo "📡 Interface disponible sur : http://localhost:8000"
echo ""
python main.py
