# 🏆 JANUS-X - Routeur intelligent pour LLM

**JANUS-X** est un routeur intelligent pour modèles de langage (LLM) qui choisit automatiquement le meilleur modèle pour chaque question posée.

🔗 **Interface en ligne** : [https://expertIA35.github.io/JANUS-X/](https://expertIA35.github.io/JANUS-X/)

---

##  Fonctionnalités

-  Routage intelligent (62 modèles, analyse en temps réel)
-  Vrais modèles en local (Mistral, Llama, Phi, Gemma)
-  Interface moderne avec chat et statistiques
-  Open source, transparent, sans lock-in

---

##  Installation en 1 commande

```bash
git clone https://github.com/expertIA35/JANUS-X.git
cd JANUS-X
./install.sh


##  Routage intelligent (PPCA)

**JANUS-X** utilise un algorithme unique appelé **PPCA** (Proportional Cognitive Routing) pour choisir le meilleur modèle à chaque question.

###  Comment ça marche ?

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

###  Pourquoi PPCA est unique

- ✅ **Temps réel** : analyse en moins de 0.1 seconde
- ✅ **Multi-dimensionnel** : prend en compte plusieurs critères
- ✅ **Adaptatif** : peut intégrer de nouveaux modèles facilement
- ✅ **Transparent** : chaque décision est justifiée

 UTILITÉ DE JANUS-X
Pour qui ?
 Entreprises : sécuriser et optimiser l'usage des LLM

 Développeurs : tester et comparer des modèles

 Chercheurs : analyser les performances des LLM

 Particuliers : utiliser l'IA en local, gratuitement

Cas d'usage concrets
Domaine	Exemple	Modèle utilisé
Droit	"Rédiger un contrat de vente"	SaulLM
Code	"Fonction Python pour trier une liste"	DeepSeek Coder
Médecine	"Symptômes de la grippe"	BioMistral
Finance	"Analyser un bilan comptable"	FinGPT
Général	"Expliquer la relativité"	Mistral
Avantages
✅ Économies : jusqu'à 50% sur les coûts d'API

✅ Confidentialité : tout tourne en local

✅ Performance : modèle adapté à chaque tâche

✅ Traçabilité : audit trail immuable (en développement)

⚠️ LIMITES ACTUELLES
Techniques
Limite	Explication	Solution future
RAM nécessaire	Les gros modèles (70B+) nécessitent 80 Go RAM	Version cloud
Temps de réponse	Premier chargement lent (modèle à charger)	Pré-chargement intelligent
Modèles par défaut	Seulement 4 modèles pré-téléchargés	Script d'installation automatique
Fonctionnelles
Limite	Explication	Solution future
Détection de langue	Basique (français/anglais)	Modèle de détection dédié
Analyse thématique	Mots-clés simples	Classification par IA
Audit trail	Pas encore implémenté	À venir dans version 2.0
Déploiement
Limite	Explication	Solution future
Installation	Nécessite des compétences techniques	Version SaaS
Espace disque	15-20 Go pour les modèles de base	Streaming de modèles
Mise à jour	Manuelle pour l'instant	Auto-update
📜 LICENCE
Projet principal : MIT 
text
MIT License

Copyright (c) 2026 Chawki TARIFS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Ce que ça permet :

✅ Utilisation commerciale

✅ Modification

✅ Distribution

✅ Utilisation privée

Ce que ça ne permet pas :

❌ Retirer la licence originale

❌ Tenir l'auteur responsable

Modèles LLM : licences variées
Modèle	Licence	Restrictions
Mistral	Apache 2.0	✅ Utilisation libre
Llama	Licence Meta	⚠️ Acceptation requise
Phi	MIT	✅ Utilisation libre
Gemma	Licence Google	⚠️ Acceptation requise
DeepSeek	MIT	✅ Utilisation libre
SaulLM	MIT	✅ Utilisation libre
BioMistral	Apache 2.0	✅ Utilisation libre
Tous les modèles sont open source et gratuits !

 TABLEAU RÉCAPITULATIF
Aspect	Détail
Utilité	Routage intelligent entre 62 LLM
Public	Entreprises, devs, chercheurs, particuliers
Limites	RAM, temps de chargement, modèles par défaut
Licence projet	MIT (ultra permissive)
Licences modèles	Apache 2.0, MIT, licences Meta/Google
Coût	100% gratuit (open source)
