# Kisaan.digi

Kisaan.digi is a Python-based, mobile-first digital ledger for farm machinery services. It helps machinery service providers log work done for farmers, track running dues, record payments, and create a transparent shared history.

This project starts with a focused MVP:
- service entry tracking
- farmer ledger visibility
- payment recording
- simple, low-friction mobile workflow

The long-term vision is bigger: a trusted rural operations platform that can later grow into booking, settlements, analytics, and broader farmer support services.

## Why This Matters

In many rural workflows, machinery services are still tracked in notebooks or memory. Payments are often delayed for months, which creates confusion, disputes, and weak record keeping.

Kisaan.digi replaces that with a shared digital record so both the service provider and farmer can see the same truth.

## Core MVP

- provider-led dashboard
- add and manage farmers
- log services by acre, hour, or trip
- auto-calculate charges
- view transaction history
- track outstanding dues
- record partial and full payments
- enable shared farmer visibility

## Current Build Status

The current version now includes:
- working local UI
- service entry form
- payment recording form
- farmer ledger view
- permanent local data saving on your machine

## Tech Foundation

- Python
- Flask
- HTML templates
- local SQLite database for saving data between restarts

## Repo Structure

- [`app.py`](/Users/prashanthreddy/Documents/Kisaan.digi/app.py): starts the local app
- [`kisaan/__init__.py`](/Users/prashanthreddy/Documents/Kisaan.digi/kisaan/__init__.py): connects the app setup
- [`kisaan/routes.py`](/Users/prashanthreddy/Documents/Kisaan.digi/kisaan/routes.py): controls page actions
- [`kisaan/store.py`](/Users/prashanthreddy/Documents/Kisaan.digi/kisaan/store.py): handles saved data and calculations
- [`templates/dashboard.html`](/Users/prashanthreddy/Documents/Kisaan.digi/templates/dashboard.html): main UI page
- [`static/styles.css`](/Users/prashanthreddy/Documents/Kisaan.digi/static/styles.css): colors and visual design
- [`docs/PRD.md`](/Users/prashanthreddy/Documents/Kisaan.digi/docs/PRD.md): product requirement document
- [`docs/ROADMAP.md`](/Users/prashanthreddy/Documents/Kisaan.digi/docs/ROADMAP.md): phased execution plan
- [`docs/PORTFOLIO.md`](/Users/prashanthreddy/Documents/Kisaan.digi/docs/PORTFOLIO.md): GitHub and portfolio positioning

## Run Locally

1. Create a virtual environment:
   `python3 -m venv .venv`
2. Activate it:
   `source .venv/bin/activate`
3. Install dependencies:
   `python3 -m pip install -r requirements.txt`
4. Start the app:
   `python3 app.py`
5. Open:
   `http://127.0.0.1:5000`

## Product Direction

The first product is not a broad farming app. It is a trust and settlement tool for machinery service transactions.

That focus is important:
- narrow enough to adopt
- practical enough to use daily
- valuable enough to replace notebook tracking

## Recommended Next Steps

1. Add farmer creation and editing
2. Add login and provider accounts
3. Move from local-only saving to shared online data when ready
4. Connect Supabase when we want multi-user access
5. Push a clean first version to GitHub
