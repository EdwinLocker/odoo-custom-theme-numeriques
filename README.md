# Custom Theme Color — Odoo 18

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

Module de personnalisation des couleurs pour Odoo 18, conçu pour remplacer la couleur violette par défaut (`#875A7B`) par les couleurs de votre charte graphique.

---

## Structure du module

```
custom_theme/
├── __manifest__.py
├── data/
│   └── color_config.xml
├── views/
│   └── email_templates.xml
└── static/src/css/
    ├── variables.css   ← 🎨 SEUL FICHIER À MODIFIER
    ├── backend.css     ← Styles interface admin (ne pas toucher)
    └── portal.css      ← Styles interface client (ne pas toucher)
```

### Rôle de chaque fichier

| Fichier | Rôle | À modifier ? |
|---------|------|:---:|
| `variables.css` | Définition de toutes les couleurs via CSS custom properties | ✅ Oui |
| `backend.css` | Application des couleurs sur l'interface d'administration Odoo | ❌ Non |
| `portal.css` | Application des couleurs sur le portail client Odoo | ❌ Non |

`backend.css` et `portal.css` importent `variables.css` automatiquement. Toute modification dans `variables.css` se propage sur l'ensemble de l'interface.

---

## Personnaliser les couleurs

Éditez **uniquement** `static/src/css/variables.css`, section 1 :

```css
:root {
  /* Couleur principale : fonds navbar, headers, titres */
  --color-primary:   #0f343d;

  /* Couleur d'accent : boutons, survols, call-to-action */
  --color-secondary: #ff6100;
}
```

Si vous changez `--color-primary` ou `--color-secondary`, mettez également à jour les couleurs dérivées (section 2) et les composantes RGB (utilisées pour les transparences) :

```css
  --color-primary-dark:    #051114;   /* primary assombri ~10% */
  --color-primary-light:   #1e687a;   /* primary éclairci ~15% */
  --color-secondary-dark:  #b34400;   /* secondary assombri ~15% */
  --color-secondary-light: #ff904d;   /* secondary éclairci ~15% */

  /* Composantes RGB pour rgba() — à synchroniser avec --color-primary */
  --color-primary-rgb:   15, 52, 61;
  --color-secondary-rgb: 255, 97, 0;
```

Outil pour calculer les variantes : [color-hex.com](https://www.color-hex.com/)

### Exemples de palettes

```css
/* Bleu institutionnel */
--color-primary:   #003366;
--color-secondary: #0077cc;

/* Vert naturel */
--color-primary:   #1a4a2e;
--color-secondary: #4caf50;

/* Rouge corporate */
--color-primary:   #8b0000;
--color-secondary: #d32f2f;
```

---

## Zones couvertes

### Backend (interface d'administration)

- Navbar principale et menu des applications
- Menus de navigation secondaires, onglets, dropdowns
- Boutons primaires, boutons liens, états actifs
- Liens (`a`, `a:hover`)
- Champs de formulaire (focus) et checkboxes/radios cochés
- Barre de statut des enregistrements
- Badges et tags (`.badge.bg-primary`, `.o_tag`)
- Alertes (`.alert-primary`)
- Pagination
- Dashboard / menu d'accueil
- Barres de progression
- Sélection de texte (`::selection`)
- Code inline

### Portal (interface client)

- Header et navbar du portail
- Boutons primaires
- Liens
- Footer
- Titres et contenu portail
- En-têtes de tableaux de documents
- Fil d'Ariane
- Champs de formulaire (focus)
- Pagination
- Badges helpdesk/tickets

### Overrides framework

Les variables Bootstrap 5 et Odoo sont écrasées dans `:root` pour une couverture maximale des composants natifs :

```css
--o-brand-primary, --o-brand-secondary, --o-brand-odoo
--bs-primary, --bs-primary-rgb
--bs-link-color, --bs-link-hover-color
```

---

## Procédure de mise à jour

Après avoir modifié `variables.css`, suivre ces étapes **dans l'ordre** pour éviter les problèmes de cache :

```bash
# 1. Incrémenter la version dans __manifest__.py
#    ex. '18.0.1.3.0' → '18.0.1.3.1'

# 2. Arrêter Odoo (évite les deadlocks)
docker compose stop odoo

# 3. Mettre à jour le module
docker compose run --rm odoo odoo -c /etc/odoo/odoo.conf -d postgres -u custom_theme --stop-after-init

# 4. Redémarrer Odoo
docker compose start odoo
```

Ensuite, dans l'interface Odoo :
1. Activer le **Mode développeur** (Paramètres → bas de page)
2. Menu développeur (icône 🐛) → **Régénérer les assets**
3. Vider le cache navigateur : `Ctrl+Shift+R` (Windows/Linux) ou `Cmd+Shift+R` (Mac)

---

## Installation

```bash
# Cloner dans le dossier addons
cd /chemin/vers/odoo/addons
git clone https://github.com/EdwinLocker/odoo-custom-theme-numeriques.git custom_theme

# Mettre à jour la liste des modules et installer
docker compose run --rm odoo odoo -c /etc/odoo/odoo.conf -d postgres -i custom_theme --stop-after-init
docker compose start odoo
```

---

## Ajouter de nouveaux sélecteurs

Si un élément violet n'est pas couvert :

1. Identifier le sélecteur CSS avec l'inspecteur du navigateur (F12)
2. L'ajouter dans `backend.css` (interface admin) ou `portal.css` (portail client)
3. Utiliser les variables existantes — ne jamais écrire de valeurs hex directement :
   ```css
   .mon_selecteur {
     color: var(--color-primary) !important;
   }
   ```

---

## Compatibilité

| Odoo | Statut |
|------|--------|
| 18.0 | ✅ Testé en production |
| 17.0 | ⚠️ Non testé |
| 16.0 | ❌ Non supporté |

---

## Changelog

### 18.0.1.3.0
- Refactoring complet de l'architecture CSS
- `variables.css` : seul fichier à modifier, syntaxe corrigée (CSS Level 5 → valeurs hex fixes), `!important` retirés des variables, ajout `--color-primary-rgb` / `--color-secondary-rgb`, overrides Bootstrap 5 natifs
- `backend.css` : remplacement des valeurs hardcodées par des variables, ajout checkboxes, badges, alertes, progress bar, `::selection`, organisation par sections numérotées
- `portal.css` : remplacement des rgba hardcodés par variables, réorganisation par sections
- Version : `18.0.1.2.9` → `18.0.1.3.0`

### 18.0.1.2.x
- Premières itérations du thème en production
- Couverture navbar, boutons, liens, formulaires, portail

---

## Licence

LGPL-3 — voir fichier `LICENSE`.