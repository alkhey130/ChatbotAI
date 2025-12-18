# chatbot/engine.py

import re

def chatbot_reply(message: str) -> str:
    """
    Retourne une réponse basée sur des mots-clés et leurs synonymes.
    Plus flexible que la simple correspondance exacte.
    """
    message = message.lower().strip()

    # Dictionnaire des réponses avec une liste de synonymes pour chaque intention
    responses = {
        "salutation": {
            "keywords": ["bonjour", "salut", "coucou", "hello", "hey"],
            "reply": "Bot: Salut ! Ravi de te voir ici 😃"
        },
        "blague": {
            "keywords": ["blague", "humour", "rigole"],
            "reply": "Bot: Pourquoi les développeurs aiment le café ? Parce qu'ils supportent le Java 😅"
        },
        "météo": {
            "keywords": ["météo", "temps", "climat", "soleil", "pluie"],
            "reply": "Bot: Je ne peux pas vérifier la météo, mais il fait toujours beau dans le monde du code 😎"
        },
        "travail": {
            "keywords": ["travail", "emploi", "job", "carrière"],
            "reply": "Bot: Le marché du travail est très favorable aux développeurs en ce moment !"
        },
        "projet": {
            "keywords": ["projet", "portfolio", "application", "site"],
            "reply": "Bot: Pour tes projets, je peux te donner des conseils ou des ressources utiles."
        },
        "aide": {
            "keywords": ["aide", "support", "assistance", "question"],
            "reply": "Bot: Bien sûr, je suis là pour aider. Que veux-tu savoir ?"
        }
    }

    # Parcourir toutes les intentions et vérifier si un mot-clé est présent
    for intent, data in responses.items():
        for keyword in data["keywords"]:
            if re.search(rf"\b{re.escape(keyword)}\b", message):
                return data["reply"]

    # Réponse par défaut
    return "Bot: Je n'ai pas compris… Peux-tu reformuler ?"
