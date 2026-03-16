# 🏆 JANUS-X - Routeur intelligent pour LLM

**JANUS-X** est un routeur intelligent pour modèles de langage (LLM) qui choisit automatiquement le meilleur modèle pour chaque question posée.

🔗 **Interface en ligne** : [https://expertIA35.github.io/JANUS-X/](https://expertIA35.github.io/JANUS-X/)

---

## ✨ Fonctionnalités

- 🧠 Routage intelligent (62 modèles, analyse en temps réel)
- ⚡ Vrais modèles en local (Mistral, Llama, Phi, Gemma)
- 📊 Interface moderne avec chat et statistiques
- 🔒 Open source, transparent, sans lock-in

---

## 🚀 Installation en 1 commande

```bash
git clone https://github.com/expertIA35/JANUS-X.git
cd JANUS-X
./install.sh


## 🧠 Routage intelligent (PPCA)

**JANUS-X** utilise un algorithme unique appelé **PPCA** (Proportional Cognitive Routing) pour choisir le meilleur modèle à chaque question.

### 🔍 Comment ça marche ?

1. **Analyse de la requête**  
   Pour chaque question, le système analyse :
   - **Langue** (français, anglais, etc.)
   - **Thème** (droit, code, médecine, général, etc.)
   - **Complexité** (simple, intermédiaire, expert)
   - **Mots-clés** spécifiques

2. **Calcul du SCC (Score de Complexité Cognitive)**  
   Chaque modèle reçoit un score basé sur :
   - Compatibilité linguistique (30%)
   - Adéquation thématique (40%)
   - Capacité à gérer la complexité (30%)

3. **Sélection du meilleur modèle**  
   Le modèle avec le score le plus élevé est choisi automatiquement.

### 📊 Exemples concrets

| Question | Analyse | Modèle choisi | Score |
|----------|---------|---------------|-------|
| "Comment créer une SAS ?" | 🇫🇷 droit | **SaulLM** (France) | 98% |
| "Écris une fonction Python" | code | **DeepSeek Coder** (Chine) | 95% |
| "Explique la relativité" | science | **Mistral** (France) | 92% |
| "Bonjour" | conversation | **Mistral** (France) | 98% |

### 🏆 Pourquoi PPCA est unique

- ✅ **Temps réel** : analyse en moins de 0.1 seconde
- ✅ **Multi-dimensionnel** : prend en compte plusieurs critères
- ✅ **Adaptatif** : peut intégrer de nouveaux modèles facilement
- ✅ **Transparent** : chaque décision est justifiée
