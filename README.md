# Custom Theme Color Odoo

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

## 🎨 Description

**Custom Theme Color Odoo** est un module qui permet de personnaliser facilement les couleurs de l'interface Odoo en remplaçant la couleur violette par défaut (`#875A7B`) par vos couleurs d'entreprise.

### ✨ Fonctionnalités

- ✅ Remplacement de la couleur principale d'Odoo
- ✅ Personnalisation des boutons, liens et éléments interactifs
- ✅ Modification des couleurs dans les emails automatiques
- ✅ Support des badges, tags et étiquettes
- ✅ Compatible interface backend et frontend
- ✅ Architecture SCSS modulaire et maintenable
- ✅ Compatible mode sombre/clair

### 🎯 Zones couvertes

- Navbar et menus de navigation
- Boutons principaux et secondaires
- Liens et éléments interactifs
- Pagination et contrôles
- Formulaires et champs de saisie
- Badges et indicateurs de statut
- Tags et étiquettes
- Header et footer du portail client
- Templates d'emails

## 📁 Structure du module

```
custom_theme/
├── __init__.py
├── __manifest__.py
├── data/
│   └── color_config.xml
├── views/
│   └── email_templates.xml
└── static/
    └── src/
        └── scss/
            ├── _variables.scss   ← 🎨 MODIFIER ICI pour changer les couleurs
            ├── _common.scss      ← Styles partagés (boutons, liens, forms)
            ├── backend.scss      ← Interface admin Odoo
            └── portal.scss       ← Interface client/portail
```

### Architecture des fichiers SCSS

| Fichier | Rôle | Quand modifier |
|---------|------|----------------|
| `_variables.scss` | Définitions des couleurs | Pour changer la charte graphique |
| `_common.scss` | Boutons, liens, formulaires | Pour ajuster les styles communs |
| `backend.scss` | Navbar, dashboard, admin | Pour personnaliser l'interface admin |
| `portal.scss` | Header, footer, portail | Pour personnaliser l'interface client |

> **Note** : Les fichiers préfixés par `_` sont des *partials* SCSS. Ils ne sont pas compilés seuls mais importés par les autres fichiers.

## 🚀 Installation

### Méthode 1 : Installation depuis GitHub

1. **Clonez le repository dans votre dossier addons :**
   ```bash
   cd /chemin/vers/odoo/addons
   git clone https://github.com/VOTRE_USERNAME/custom-theme-color-odoo.git custom_theme
   ```

2. **Redémarrez votre serveur Odoo :**
   ```bash
   docker compose restart odoo
   # ou
   ./odoo-bin -u all -d votre_base_de_donnees
   ```

3. **Installez le module :**
   - Allez dans `Apps` > `Mettre à jour la liste des Apps`
   - Recherchez "Custom Theme Colors"
   - Cliquez sur `Installer`

### Méthode 2 : Installation manuelle

1. **Téléchargez le module et placez-le dans votre dossier addons**
2. **Redémarrez Odoo et installez le module via l'interface**

## ⚙️ Configuration

### 🎨 Personnaliser les couleurs

Éditez **uniquement** le fichier `static/src/scss/_variables.scss` :

```scss
// Couleurs principales - MODIFIER CES VALEURS
$color-primary:    #0F343D;   // Votre couleur principale
$color-secondary:  #FF6100;   // Votre couleur secondaire

// Couleurs complémentaires (optionnel)
$color-beige:   #F6F5F1;
$color-cafe:    #E1D8B8;
$color-jaune:   #FDD860;
$color-vert:    #C5FAD6;
$color-violet:  #D9CDFF;
$color-noir:    #262625;
```

Les couleurs dérivées (hover, focus) sont calculées automatiquement.

### 🎨 Exemples de palettes

```scss
/* Bleu professionnel */
$color-primary: #0066CC;
$color-secondary: #FF6B35;

/* Vert moderne */
$color-primary: #2ECC40;
$color-secondary: #1F8B2C;

/* Rouge corporate */
$color-primary: #DC3545;
$color-secondary: #FFC107;
```

## 🛠️ Personnalisation avancée

### Modifier les styles backend

Éditez `backend.scss` pour personnaliser l'interface admin :

```scss
// Exemple : changer la couleur du dashboard
.o_home_menu {
    background-color: $color-primary !important;
}
```

### Modifier les styles portail

Éditez `portal.scss` pour personnaliser l'interface client :

```scss
// Exemple : personnaliser les titres
.o_portal h1 {
    color: $color-secondary;
}
```

### Ajouter de nouveaux sélecteurs

Si certains éléments violets ne sont pas couverts :

1. **Identifiez l'élément avec l'inspecteur (F12)**
2. **Ajoutez le sélecteur dans le fichier approprié** (`backend.scss` ou `portal.scss`)

## 🔍 Débogage

### Identifier les éléments violets restants

Ajoutez temporairement ce code dans `_common.scss` :

```scss
// Fait clignoter les éléments avec couleur violette hardcodée
*[style*="#875A7B"] {
    outline: 3px solid red !important;
    animation: highlight-purple 1s infinite;
}

@keyframes highlight-purple {
    0%, 100% { outline-color: red; }
    50% { outline-color: yellow; }
}
```

### Vider le cache

Après modification des fichiers SCSS :
1. Videz le cache navigateur : `Cmd+Shift+R` (Mac) ou `Ctrl+Shift+R` (Windows)
2. Redémarrez Odoo si nécessaire

## 📋 Compatibilité

- **Odoo 18.0** ⚠️ En cours de test
- **Odoo 17.0** ⚠️ Devrait fonctionner (non testé)
- **Odoo 16.0** ⚠️ Adaptations possibles requises

## 📝 Changelog

### Version 2.0.0
- 🔄 Refactoring complet avec architecture SCSS modulaire
- ✅ Fichier de variables centralisé
- ✅ Séparation backend / portal
- ✅ Styles communs factorisés
- ✅ Documentation améliorée

### Version 1.0.0
- ✅ Remplacement couleur principale Odoo
- ✅ Support des emails automatiques
- ✅ Badges et tags personnalisés
- ✅ Interface backend/frontend

## ⚖️ Licence

Ce projet est sous licence LGPL-3. Voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! 

1. Fork le projet
2. Créez une branche : `git checkout -b feature/ma-fonctionnalite`
3. Committez : `git commit -m "Ajout de ma fonctionnalité"`
4. Push : `git push origin feature/ma-fonctionnalite`
5. Ouvrez une Pull Request

## 🐛 Signaler un problème

1. Vérifiez les [issues existantes](https://github.com/VOTRE_USERNAME/custom-theme-color-odoo/issues)
2. Créez une nouvelle issue avec :
   - Description du problème
   - Capture d'écran si applicable
   - Version d'Odoo utilisée
   - Navigateur et version

---

⭐ **Si ce module vous aide, n'hésitez pas à lui donner une étoile !**
