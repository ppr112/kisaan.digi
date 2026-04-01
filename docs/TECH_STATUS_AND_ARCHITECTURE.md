# Kisaan.digi: Technical Status and Architecture

## 1. Original Aim Before We Started

The original aim was to turn the product idea from the two source documents into a real working foundation for a mobile-first machinery-service ledger product.

The intended product outcome was:
- a provider-led system for managing farmer service transactions
- a shared financial record of machinery usage, dues, and payments
- a simple workflow that could later scale into a larger rural operations platform

At the start, the problem was defined clearly but existed only as concept documents.

## 2. What We Have Done So Far

### Product Foundation
- analyzed the original problem and PRD documents
- clarified the real MVP focus: trust, dues tracking, and settlement clarity
- defined the first realistic product flow:
1. create farmer
2. add service entry
3. record payment
4. view farmer ledger and outstanding balance

### Project Foundation
- created a Python project structure for the app
- converted the idea into a running Flask application
- created a browser-based working interface for local testing
- renamed the visible product identity to `Kisaan.digi`

### UI and UX Foundation
- built a clean dashboard-based layout
- added a nature-aligned visual system using:
  - light green as primary identity
  - white as the default page base
  - soft sunrise warmth as accent
- kept the interface simple, provider-first, and low-friction

### Functional Features Built
- dashboard summary for total service value, total paid, and outstanding dues
- farmer ledger cards
- service entry creation
- payment recording
- farmer creation
- farmer editing

### Data and Persistence
- replaced temporary in-memory storage with a local SQLite database
- created a local database file for persistence across restarts
- seeded initial sample data for testing
- verified that service entries, payments, and farmer updates persist locally

### Repo and Project Cleanup
- added `.gitignore`
- cleaned local clutter for GitHub readiness
- updated the README to match the current project state

## 3. Where We Are Now

We are no longer at concept stage.

We currently have:
- a working Python web app
- local persistent storage
- a usable provider-side MVP flow
- a project folder that is much closer to GitHub-ready state

Current status in plain technical terms:
- frontend: working server-rendered UI
- backend: working Flask routes and business logic
- storage: working local SQLite database
- deployment: local development only
- auth: not built yet
- multi-user sync: not built yet
- cloud backend: not connected yet

## 4. Current Architecture

### Current Stack
- Python
- Flask
- Jinja templates
- SQLite
- HTML/CSS

### Current Runtime Flow
1. `app.py` starts the application
2. `kisaan/__init__.py` creates the Flask app and initializes storage
3. `kisaan/routes.py` handles incoming actions from forms
4. `kisaan/store.py` reads and writes farmer, entry, and payment data
5. `templates/dashboard.html` renders the UI
6. `static/styles.css` controls the visual presentation
7. `data/kisaan.db` stores the actual saved records locally

### Current Data Model

#### Farmers
- id
- name
- village

#### Service Entries
- id
- farmer_id
- service_type
- unit_type
- quantity
- rate
- total
- entry_date

#### Payments
- id
- farmer_id
- amount
- method
- payment_date

### Current System Behavior
- service totals are calculated from quantity x rate
- outstanding balance is computed from service totals minus payments
- dashboard aggregates all ledger activity
- farmer cards summarize individual balances and recent transactions
- forms submit directly to Flask routes
- data is stored in SQLite so it remains after restart

## 5. Complete Architecture of What We Are Building

The complete architecture should be understood in two layers:
- the architecture we have now
- the architecture we are moving toward

### A. Current Practical MVP Architecture

#### Presentation Layer
- provider-facing web interface
- dashboards, forms, ledger views

#### Application Layer
- Flask routes
- input parsing
- flow handling for farmer creation, service entry, and payments

#### Domain Logic Layer
- ledger calculations
- payment status calculation
- farmer summary generation
- activity feed generation

#### Persistence Layer
- SQLite database
- local file-based storage

This is enough for local product building and fast iteration.

### B. Target Product Architecture

#### 1. Client Layer
- provider dashboard
- farmer access view
- mobile-friendly interface
- later: dedicated mobile app if needed

#### 2. Application/API Layer
- authentication
- account-based routing
- CRUD operations for farmers, services, payments
- reporting and statements
- notification/reminder workflows later

#### 3. Business Domain Layer
- service ledger engine
- dues tracking
- settlement logic
- farmer-provider shared visibility rules
- future analytics and booking logic

#### 4. Data Layer
- cloud PostgreSQL via Supabase when ready
- user accounts
- provider-level data ownership
- farmer records
- service history
- payment history
- audit trail later if needed

#### 5. Infrastructure Layer
- local development environment
- GitHub source control
- cloud database later
- deployment environment later

## 6. Recommended Next Engineering Steps

### Immediate Next Step
- initialize git locally and create the first clean commit

### Next Product Step
- keep improving provider workflow around farmer/service/payment management

### Next Platform Step
- add authentication and provider accounts

### Next Architecture Upgrade
- move from local SQLite-only storage to shared cloud storage when we want multi-user access
- Supabase is the strongest current candidate for this phase

## 7. Summary

The project started as a product idea captured in documents.

It is now a functioning local application with:
- real screens
- real form flows
- real local persistence
- a clearer path toward a proper multi-user rural-tech platform

The most important shift is this:
we are no longer planning the product from zero; we are now shaping the first working version of it.
