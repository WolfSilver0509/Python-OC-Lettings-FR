# Utilisez une image Python comme image de base
FROM python:3.11.3

# Définissez les variables d'environnement pour éviter les erreurs de déploiement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Créez et définissez le répertoire de travail dans l'image
WORKDIR /app

# Copiez le fichier requirements.txt et installez les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiez tout le contenu du projet dans le répertoire de travail de l'image
COPY . /app/

# Exposez le port sur lequel fonctionne votre application Django
EXPOSE 8000

# Commande pour exécuter votre application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
