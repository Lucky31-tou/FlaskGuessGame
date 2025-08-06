# Flask Guess Game - Jeu du Nombre Mystère

Une application web simple développée avec le micro-framework Python Flask. Elle met en œuvre un jeu classique du "Nombre Mystère", un système d'authentification utilisateur basique et un compteur de visites par session.

## Fonctionnalités

-   **Jeu du Nombre Mystère** : Devinez un nombre généré aléatoirement entre 0 et 100. Vous avez 10 tentatives pour trouver la bonne réponse.
-   **Système d'authentification** : Une page de connexion permet aux utilisateurs de s'identifier. L'accès à certaines parties du site est restreint aux utilisateurs connectés.
-   **Gestion de session** : Utilisation des sessions Flask pour suivre l'état de connexion de l'utilisateur, sa progression dans le jeu et le nombre de visites sur une page spécifique.
-   **Compteur de visites** : Une page dédiée qui compte combien de fois elle a été visitée au cours de la session de l'utilisateur.

## Installation et Lancement

Pour faire fonctionner ce projet sur votre machine locale, suivez ces étapes :

1.  **Clonez le dépôt**
    Clonez ce dépôt GitHub sur votre ordinateur.
    ```bash
    git clone https://github.com/Lucky31-tou/FlaskGuessGame.git
    ```

2.  **Accédez au dossier du projet**
    ```bash
    cd FlaskGuessGame
    ```

3.  **Créez un environnement virtuel (recommandé)**
    Cela permet d'isoler les dépendances du projet.
    ```bash
    # Pour Windows
    python -m venv venv
    venv\Scripts\activate

    # Pour macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Installez les dépendances**
    Le projet ne dépend que de Flask.
    ```bash
    pip install Flask
    ```

5.  **Lancez l'application**
    ```bash
    python app.py
    ```
    L'application sera alors accessible dans votre navigateur.

## Comment utiliser l'application

Une fois l'application lancée, ouvrez votre navigateur web et accédez à l'adresse suivante :

➡️ **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### Pages disponibles

-   **/login** : Page de connexion. Vous pouvez utiliser l'un des comptes suivants :
    -   `nom`: `admin`, `mdp`: `1234`
    -   `nom`: `marie`, `mdp`: `nsi`
    -   `nom`: `paul`, `mdp`: `azerty`
-   **/jeu** : La page principale du jeu du Nombre Mystère.
-   **/compteur** : Une page qui affiche le nombre de fois que vous l'avez visitée pendant votre session.
-   **/logout** : Pour vous déconnecter.

Auteur : Louis Dubois
