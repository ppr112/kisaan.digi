# Kisaan PRD

## 1. Product Summary

Kisaan is a mobile-first digital ledger for farm machinery service tracking between service providers and farmers. The system records each service transaction, maintains a running ledger, and helps both sides see dues and payment status clearly.

## 2. Problem

Machinery services in rural areas are often tracked manually using notebooks or memory. This creates:
- weak transparency
- delayed payment reconciliation
- missing or inaccurate records
- disputes around total dues

## 3. Primary Users

- Primary user: machinery service provider
- Secondary user: farmer

## 4. MVP Goal

Replace notebook tracking with a simple shared digital record that helps users:
- log services quickly
- know how much is due
- track what has been paid
- reduce confusion and trust issues

## 5. Core User Jobs

### Service Provider
- add a farmer
- select service type
- enter quantity and rate
- see running balance
- record payment when money is received

### Farmer
- view service history
- see pending amount
- verify settlement status

## 6. MVP Features

- phone-based access
- farmer profile creation
- service entry creation
- transaction history
- ledger summary
- payment recording
- farmer-side visibility

## 7. Recommended Additions

- preset service categories
- saved rate templates
- partial payment support
- outstanding dues dashboard
- local language support
- low-network friendly design
- shareable statement view

## 8. Data Model

### Users
- id
- role
- name
- phone
- preferred_language

### Farmers
- id
- provider_id
- name
- village
- phone

### Service Entries
- id
- farmer_id
- provider_id
- service_type
- unit_type
- quantity
- rate
- total
- date
- notes

### Payments
- id
- farmer_id
- provider_id
- amount
- date
- method
- notes

## 9. Business Logic

- total per service entry = quantity x rate
- outstanding balance = total services - total payments
- ledger is farmer-specific and provider-owned
- each payment reduces the outstanding balance

## 10. UX Principles

- simple mobile-first flow
- large tap areas
- minimum typing
- familiar wording
- clear dues visibility
- designed for low tech confidence

## 11. Risks

- provider resistance to switching from notebooks
- low digital confidence among some users
- unclear ownership of dispute resolution
- weak connectivity in field environments

## 12. Success Metrics

- number of providers using daily
- number of entries created per week
- repeat usage after first week
- payment records tracked digitally
- provider willingness to stop using notebooks

## 13. Long-Term Vision

After proving the core ledger workflow, Kisaan can expand into:
- service booking
- payment reminders
- digital settlements
- seasonal analytics
- operational planning for rural service businesses
