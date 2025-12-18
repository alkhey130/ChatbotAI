ChatbotAI - Assistant Intelligent

ChatbotAI est une architecture modulaire conçue pour déployer un agent conversationnel robuste. Le projet sépare distinctement la logique de l'interface (API), le moteur de traitement (Engine) et la persistance des données (Database).

📂 Structure du Projet
L'organisation du code suit les meilleures pratiques de modularité :

api/ : Gère les points d'entrée externes et les Webhooks.

app/ : Contient le point d'entrée principal de l'application (main.py).

chatbot/ : Le cœur de l'intelligence, incluant le moteur de traitement (engine.py).

database/ : Gestion de la base de données, modèles ORM et connexions (db.py, models.py).
