# Darwin , Samir , Mamadou

#  Projet Pierre-Feuille-Ciseaux et Jeu du Morpion – Système de Tournoi

## 📌 Description
Ce projet consiste à développer en **Python** un système complet de gestion de tournois pour les jeu **Pierre-Feuille-Ciseaux** (PFC) et **Morpion**, jouable en **console**.  
Il permet de gérer des joueurs humains et des intelligences artificielles, d’organiser des tournois, de calculer un classement **ELO**, et de sauvegarder les données.

Le projet est réalisé dans un cadre pédagogique et respecte une planification sur plusieurs jours avec une utilisation de **Git/GitHub**.

---

## 🎯 Objectifs pédagogiques
- Structurer un projet Python en plusieurs modules
- Implémenter une logique de jeu complète
- Utiliser des structures de données (listes, dictionnaires)
- Gérer la persistance avec des fichiers JSON
- Travailler en équipe avec Git (commits réguliers et explicites)

---

## 🕹️ Fonctionnalités principales

### Menu principal
- Créer un tournoi (PFC, Morpion)
- Reprendre un tournoi
- Historique des tournois
- Classement ELO
- Statistiques des joueurs
- Règles du tournoi
- Quitter le programme

### Jeu Pierre-Feuille-Ciseaux
- Choix : pierre, feuille ou ciseaux
- Match en plusieurs manches
- Détermination automatique du vainqueur
- Mise à jour des statistiques et de l’ELO

### ✖VS🔘Morpion
- Choix : chaque case est représenté par un nombre de 1 à 9
- Match en une manche
- Détermination du vainqueur
- Mise à jour des statistiques et de l'ELO

### Joueurs
- Joueurs humains
- IA (difficulté aléatoire)
- Statistiques : victoires, défaites, ratio, ELO

### 🦾Tournois
- Création de tournois
- Gestion des participants
- Sauvegarde et reprise d’un tournoi en cours

### ➕➖Système ELO
- Score initial : 1000
- Gain/perte de points (-50) ou (+50) selon victoire ou défaite
- Classement automatique des joueurs


## 🧠 Architecture et choix techniques
- **Langage** : Python 
- **Interface** : Console / terminal
- ---

## 🛠️ Outils et technologies utilisés

- **Python 3.8+** : langage principal du projet
- **JSON** : sauvegarde des joueurs, tournois et historiques
- **Git Bash** : gestion des versions et des commits en local
- **GitHub** : hébergement du dépôt et travail collaboratif
- **VS Code** : environnement de développement

---

## 🔁 Utilisation de Git
- Dépôt GitHub partagé entre les membres de l’équipe
- Travail en local avec VS Code
- Commits réguliers (minimum 10 commits)
- Messages de commit descriptifs
- Synchronisation via `git push` et `git pull`

---

## 🚀 Lancer le projet

Depuis la racine du projet :
```bash
python src/fonctionprincipale.py
