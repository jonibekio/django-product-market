# Django Product Market — Product Catalog Demo

![Python](https://img.shields.io/badge/Python-Django-3776AB?logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-templates-092E20?logo=django&logoColor=white) ![Database](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite&logoColor=white)

## Overview

A learning-scale Django product catalog with account/profile workflows and seller-owned product CRUD. Products support category browsing and multiple uploaded images. This repository does not implement a cart, checkout, or order-processing system.

## Features

- Custom account/profile model and session authentication.
- Product categories and product list/detail views.
- Create, update, and delete a seller's own products.
- Multiple product image uploads and a client-side image slider.
- User-specific product listing.

## Screenshots

No product screenshots are tracked in the repository.

## Technology stack and architecture

Python, Django templates, SQLite, Pillow/ImageField, CSS, and JavaScript. The Django project separates account/profile workflows (`accounts`) from catalog/product workflows (`watch`).

```text
accounts/     Custom user, authentication, profile forms/views
watch/        Categories, products, image records, CRUD views
config/       Django settings and URL routing
templates/    Server-rendered pages
media/        Uploaded product images
manage.py
```

## Installation

The repository does not include a dependency manifest. Install the dependencies in a fresh environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install Django Pillow
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. SQLite and local media storage are development defaults.

## Environment variables

No environment-variable contract is documented. The project currently uses development settings. Before hosting, configure a unique secret, `DEBUG=False`, exact allowed hosts, and durable/private media storage.

## Routes and API documentation

This application uses Django HTML views and does not expose a REST API. Account and product routes are declared in `accounts/urls.py` and `watch/urls.py`; verify the source URL patterns for the current exact paths.

## Database

Django models store accounts, product categories, products, and product images. Local development uses SQLite and Django migrations.

## Usage

Create an account, sign in, browse products, and create/manage only products associated with your account. Product-image uploads are stored under the configured media directory.

## Tests and deployment

There are no substantive tests, pinned dependency manifest, CI workflow, Docker configuration, or platform deployment files. The existing test modules are placeholders. Local Django development server is the only documented execution path.

## Security notes

- Django production security settings must be added before internet exposure.
- Verify object-level ownership checks for every product/profile mutation.
- Do not use this learning project to process real orders or payments; those flows are not implemented.
- Database, media, and Python cache artifacts are tracked and should be reviewed separately.

## Future improvements

- Add a dependency manifest and meaningful tests for account ownership and uploads.
- Add pagination and accessible upload validation.
- Implement cart/order workflows only as an explicit future feature.
- Add production settings, CI, and real screenshots.
