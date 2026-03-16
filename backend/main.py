"""
JANUS-X API - Point d'entrée principal avec routeur intelligent
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# Import du routeur
from realtime_router import RealtimeRouter

# Initialisation de l'application
app = FastAPI(
    title="JANUS-X API",
    description="Routeur intelligent pour LLM avec audit trail",
    version="1.0.0"
)

# Configuration CORS pour permettre les requêtes depuis l'interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialisation du routeur
json_path = os.path.join(os.path.dirname(__file__), "..", "data", "llm_models.json")
router = RealtimeRouter(json_path=json_path)

@app.get("/")
async def root():
    """Route de test pour vérifier que l'API fonctionne"""
    return {
        "message": "JANUS-X API",
        "status": "online",
        "modeles_disponibles": len(router.modeles)
    }

@app.post("/api/chat")
async def chat(requete: dict):
    """
    Endpoint principal pour le chat
    Reçoit une requête et retourne la réponse du meilleur modèle
    """
    # Extraire les données de la requête
    texte = requete.get("texte", "")
    user_id = requete.get("user_id", "anonymous")
    
    if not texte:
        return {"erreur": "Texte manquant"}
    
    # Traiter la requête avec le routeur
    resultat = await router.traiter_requete(texte, user_id)
    
    return resultat

@app.get("/api/modeles")
async def lister_modeles():
    """Retourne la liste de tous les modèles disponibles"""
    modeles = []
    for modele_id, modele in router.modeles.items():
        modeles.append({
            "id": modele_id,
            "nom": modele.nom,
            "pays": modele.pays,
            "taille_gb": modele.taille_gb,
            "langues": modele.langues,
            "specialites": modele.specialites,
            "vitesse": modele.vitesse
        })
    return {
        "total": len(modeles),
        "modeles": modeles
    }

@app.get("/api/stats")
async def get_stats():
    """Retourne les statistiques d'utilisation"""
    return router.get_stats()

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 JANUS-X API - Démarrage")
    print("="*50)
    print(f"📊 {len(router.modeles)} modèles chargés")
    print("🌐 Serveur sur http://0.0.0.0:8000")
    print("="*50 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
