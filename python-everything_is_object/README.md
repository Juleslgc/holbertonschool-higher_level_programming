#  Python – Objets, Références et Mutabilité

Ce projet présente de manière simple et structurée les **concepts fondamentaux** de Python autour de la gestion de la mémoire, des objets, des références et de la mutabilité. Ces notions sont essentielles pour bien comprendre le comportement des variables, des fonctions et éviter les pièges courants liés aux objets partagés.

---

##  Concepts abordés

###  Qu'est-ce qu’un objet ?
En Python, **tout est objet** : entiers, chaînes, listes, fonctions, etc.  
Un objet possède :
- un **type** (`int`, `str`, etc.)
- une **valeur**
- un **identifiant** (son emplacement mémoire)

---

###  Différence entre une classe et un objet
- Une **classe** est un **modèle** définissant un type d’objet.
- Un **objet** (ou **instance**) est une réalisation concrète de cette classe.

---

###  Objets mutables vs immutables
- Un objet **mutable** peut être modifié (ex : `list`, `dict`).
- Un objet **immutable** ne peut pas être modifié (ex : `int`, `str`, `tuple`).

---

###  Références et affectation
Les variables en Python ne contiennent **pas directement les objets**, mais des **références** vers eux.  
L’opération `=` crée une liaison entre une variable et une référence d’objet, **sans copier** l’objet.

---

###  Alias
Quand deux variables font référence au **même objet**, on parle d’**alias**.  
Modifier cet objet via l'une des variables affectera l'autre.

---

###  Identité et égalité
- `==` compare le **contenu** des objets.
- `is` compare leur **identité** (même objet ou non).

---

###  Identifier un objet
La fonction `id(obj)` renvoie l'**identifiant unique** d’un objet, qui correspond à son **adresse mémoire** dans l’implémentation CPython.

---

###  Types mutables intégrés
- `list`
- `dict`
- `set`
- `bytearray`

---

###  Types immutables intégrés
- `int`
- `float`
- `str`
- `tuple`
- `frozenset`
- `bytes`

---

###  Passage des variables aux fonctions
Python passe les **références** aux fonctions, pas les objets eux-mêmes :
- Si l’objet est **mutable**, il peut être modifié.
- Si l’objet est **immutable**, toute modification crée un nouvel objet (l’original reste inchangé).

---

##  Objectif du projet

Ce projet a été conçu pour :
- Mieux comprendre comment Python manipule les objets en mémoire
- Clarifier les comportements parfois déroutants liés aux alias et à la mutabilité
- Apprendre à utiliser correctement `is`, `==`, `id()` et à distinguer valeur et identité
