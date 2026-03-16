"""
Routeur temps réel avec base de données JSON des LLM
"""

import json
import re
import time
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict
import os

@dataclass
class Modele:
    """Représente un modèle LLM"""
    id: str
    nom: str
    pays: str
    taille_gb: float
    ram_requise: float
    langues: List[str]
    specialites: List[str]
    scores: Dict[str, float]
    vitesse: float
    description: str = ""

class RealtimeRouter:
    """
    Routeur qui analyse CHAQUE requête individuellement
    et sélectionne le meilleur modèle pour CETTE requête précise
    """
    
    def __init__(self, json_path=None):
        if json_path is None:
            # Chemin par défaut
            json_path = os.path.join(os.path.dirname(__file__), "..", "data", "llm_models.json")
        self.modeles = self._charger_modeles_json(json_path)
        self.stats_utilisation = defaultdict(lambda: {
            "requetes": 0,
            "temps_moyen": 0,
            "satisfaction": 0
        })
        print(f"✅ Routeur initialisé avec {len(self.modeles)} modèles")
    
    def _charger_modeles_json(self, json_path: str) -> Dict[str, Modele]:
        """Charge les modèles depuis le fichier JSON"""
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            modeles = {}
            for modele_id, props in data.items():
                modeles[modele_id] = Modele(
                    id=modele_id,
                    nom=props.get('nom', modele_id),
                    pays=props.get('pays', 'Inconnu'),
                    taille_gb=props.get('taille_gb', 0),
                    ram_requise=props.get('ram_requise', props.get('taille_gb', 4) * 2),
                    langues=props.get('langues', ['en']),
                    specialites=props.get('specialites', ['general']),
                    scores=props.get('scores', {'general': 0.5}),
                    vitesse=props.get('vitesse', 30),
                    description=props.get('description', '')
                )
            
            print(f"📦 {len(modeles)} modèles chargés depuis {json_path}")
            return modeles
            
        except FileNotFoundError:
            print(f"❌ Fichier {json_path} non trouvé - utilisation de modèles par défaut")
            return self._charger_modeles_defaut()
        except json.JSONDecodeError as e:
            print(f"❌ Erreur de lecture JSON: {e}")
            return self._charger_modeles_defaut()
    
    def _charger_modeles_defaut(self) -> Dict[str, Modele]:
        """Modèles par défaut si le fichier JSON n'est pas trouvé"""
        return {
            "mistral-7b": Modele(
                id="mistral-7b",
                nom="Mistral 7B",
                pays="France",
                taille_gb=4.1,
                ram_requise=8,
                langues=["fr", "en", "es", "de", "it"],
                specialites=["general", "conversation"],
                scores={"fr": 0.98, "general": 0.95},
                vitesse=45,
                description="Modèle français généraliste"
            ),
            "llama-3.1-8b": Modele(
                id="llama-3.1-8b",
                nom="Llama 3.1 8B",
                pays="USA",
                taille_gb=4.5,
                ram_requise=10,
                langues=["en", "fr", "es"],
                specialites=["general", "multilingue"],
                scores={"fr": 0.82, "general": 0.94},
                vitesse=35,
                description="Modèle Meta multilingue"
            )
        }
    
    def analyser_requete(self, requete: str) -> Dict:
        """
        Analyse approfondie d'une requête
        """
        texte = requete.lower()
        
        # Déterminer la langue principale (simplifié)
        langue = self._analyser_langue(texte)
        
        # Déterminer les thèmes
        themes = self._analyser_themes(texte)
        theme_principal = themes[0] if themes else "general"
        
        # Analyser la complexité
        complexite = self._analyser_complexite(texte)
        
        return {
            "langue_principale": langue,
            "themes": themes,
            "theme_principal": theme_principal,
            "complexite": complexite,
            "mots_cles": self._extraire_mots_cles(texte)
        }
    
    def _analyser_langue(self, texte: str) -> str:
        """Détecte la langue principale"""
        mots_fr = ["le", "la", "les", "un", "une", "je", "tu", "il", "elle", "nous", "vous", "ils", "elles", "et", "ou", "mais", "donc", "car", "bonjour", "merci"]
        mots_en = ["the", "a", "an", "i", "you", "he", "she", "we", "they", "and", "or", "but", "so", "because", "hello", "thank"]
        
        score_fr = sum(1 for m in mots_fr if m in texte)
        score_en = sum(1 for m in mots_en if m in texte)
        
        if score_fr > score_en:
            return "fr"
        else:
            return "en"
    
    def _analyser_themes(self, texte: str) -> List[str]:
        """Détecte les thèmes de la requête"""
        themes = []
        if any(m in texte for m in ["code", "python", "programmation", "java", "javascript", "function"]):
            themes.append("code")
        if any(m in texte for m in ["droit", "loi", "juridique", "contrat", "legal", "tribunal"]):
            themes.append("droit")
        if any(m in texte for m in ["math", "équation", "calcul", "algèbre", "géométrie"]):
            themes.append("math")
        if any(m in texte for m in ["medical", "santé", "maladie", "hopital", "docteur", "symptôme"]):
            themes.append("medical")
        if any(m in texte for m in ["finance", "banque", "argent", "investissement", "bourse"]):
            themes.append("finance")
        if any(m in texte for m in ["science", "physique", "chimie", "biologie", "recherche"]):
            themes.append("science")
        if not themes:
            themes.append("general")
        return themes
    
    def _analyser_complexite(self, texte: str) -> Dict:
        """Analyse la complexité de la requête"""
        mots = texte.split()
        longueur = len(mots)
        
        # Termes techniques
        termes_techniques = ["algorithme", "implémentation", "architecture", "optimisation", 
                           "paradigme", "ontologie", "épistémologie", "phénoménologie",
                           "dérivée", "intégrale", "théorème", "lemme"]
        
        nb_technique = sum(1 for terme in termes_techniques if terme in texte)
        
        # Score de complexité (0-1)
        score = min(1.0, (
            (longueur / 50) * 0.5 +
            (nb_technique / 5) * 0.5
        ))
        
        if score < 0.3:
            niveau = "simple"
        elif score < 0.6:
            niveau = "intermediaire"
        else:
            niveau = "expert"
        
        return {
            "score": score,
            "niveau": niveau,
            "longueur": longueur,
            "termes_techniques": nb_technique
        }
    
    def _extraire_mots_cles(self, texte: str) -> List[str]:
        """Extrait les mots-clés importants"""
        stop_words = ["le", "la", "les", "un", "une", "des", "je", "tu", "il", "elle",
                     "nous", "vous", "ils", "elles", "et", "ou", "mais", "donc",
                     "car", "ni", "or", "si", "de", "du", "au", "aux", "en", "y"]
        
        mots = texte.split()
        mots_importants = []
        
        for mot in mots:
            if len(mot) > 3 and mot not in stop_words and mot not in mots_importants:
                mots_importants.append(mot)
        
        return mots_importants[:5]
    
    def selectionner_modele(self, profil: Dict, ram_disponible: float = 16) -> Tuple[Optional[Modele], Dict]:
        """
        Sélectionne le meilleur modèle pour la requête
        """
        scores_modeles = []
        
        for modele_id, modele in self.modeles.items():
            # Vérifier RAM disponible
            if modele.ram_requise > ram_disponible:
                continue
            
            # Calculer le score
            score, raisons = self._calculer_score_modele(modele, profil)
            
            scores_modeles.append({
                "modele": modele,
                "score": score,
                "raisons": raisons
            })
        
        # Trier par score
        scores_modeles.sort(key=lambda x: x["score"], reverse=True)
        
        if not scores_modeles:
            return None, {"erreur": "Aucun modèle compatible"}
        
        meilleur = scores_modeles[0]
        
        decision = {
            "modele_selectionne": meilleur["modele"].id,
            "score": meilleur["score"],
            "raisons": meilleur["raisons"],
            "alternatives": [
                {
                    "modele": m["modele"].id,
                    "score": m["score"],
                    "raisons": m["raisons"][:2]
                }
                for m in scores_modeles[1:4]
            ]
        }
        
        return meilleur["modele"], decision
    
    def _calculer_score_modele(self, modele: Modele, profil: Dict) -> Tuple[float, List[str]]:
        """
        Calcule un score pour un modèle spécifique
        """
        poids = {
            "langue": 0.30,
            "theme": 0.40,
            "complexite": 0.30
        }
        
        score_total = 0
        raisons = []
        
        # 1. Score de langue
        langue = profil.get("langue_principale", "en")
        if langue in modele.langues:
            score_langue = modele.scores.get(langue, 0.8)
            score_total += score_langue * poids["langue"]
            raisons.append(f"Langue {langue}: {score_langue:.2f}")
        else:
            score_total += 0.3 * poids["langue"]
            raisons.append(f"Langue {langue} non supportée")
        
        # 2. Score des thèmes
        theme = profil.get("theme_principal", "general")
        if theme in modele.specialites:
            score_theme = modele.scores.get(theme, 0.9)
            score_total += score_theme * poids["theme"]
            raisons.append(f"Thème {theme}: {score_theme:.2f}")
        else:
            score_general = modele.scores.get("general", 0.7)
            score_total += score_general * poids["theme"]
            raisons.append(f"Thème général: {score_general:.2f}")
        
        # 3. Complexité
        complexite = profil.get("complexite", {}).get("score", 0.5)
        if complexite > 0.7 and modele.taille_gb > 4:
            raisons.append("Bon pour requêtes complexes")
            score_total += 0.9 * poids["complexite"]
        elif complexite < 0.3 and modele.taille_gb < 3:
            raisons.append("Léger et rapide pour requête simple")
            score_total += 0.9 * poids["complexite"]
        else:
            score_total += 0.7 * poids["complexite"]
        
        return min(1.0, score_total), raisons[:3]
    
    async def traiter_requete(self, requete: str, user_id: str = "anonymous") -> Dict:
        """
        Traite une requête complète
        """
        debut = time.time()
        
        # Analyser la requête
        profil = self.analyser_requete(requete)
        
        # RAM disponible (simulée)
        ram_disponible = 16  # 16 Go par défaut
        
        # Sélectionner le modèle
        modele, decision = self.selectionner_modele(profil, ram_disponible)
        
        if not modele:
            return {
                "erreur": "Aucun modèle disponible",
                "requete": requete,
                "temps": time.time() - debut
            }
        
        # Mettre à jour les stats
        self.stats_utilisation[modele.id]["requetes"] += 1
        
        # Simuler une réponse (dans la vraie vie, appellerait le modèle)
        reponse = f"Réponse générée par {modele.nom} ({modele.pays})"
        
        return {
            "requete": requete,
            "reponse": reponse,
            "modele_utilise": {
                "id": modele.id,
                "nom": modele.nom,
                "pays": modele.pays,
                "taille_gb": modele.taille_gb
            },
            "analyse": profil,
            "decision_routage": decision,
            "performance": {
                "temps_total": time.time() - debut
            }
        }
    
    def get_stats(self) -> Dict:
        """Retourne les statistiques d'utilisation"""
        return {
            "modeles_disponibles": len(self.modeles),
            "requetes_traitees": sum(s["requetes"] for s in self.stats_utilisation.values()),
            "stats_par_modele": dict(self.stats_utilisation)
        }
