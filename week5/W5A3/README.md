# Clinic Management System — Class Diagram

A UML class diagram for a clinic system that supports three core patient-facing features:
**booking an appointment**, **paying the booking fee**, and **ordering medication**.

---

## Class Diagram Preview

> Open `clinic-class-diagram.drawio` at [app.diagrams.net](https://app.diagrams.net) to view the interactive diagram.

---

## System Overview

The design is organised into four functional modules:

### 1. Core Actors
| Class | Description |
|---|---|
| `Patient` | The primary user. Can book appointments, make payments, and order medication. |
| `Doctor` | Manages appointment slots and issues prescriptions to patients. |

### 2. Appointment Module
| Class | Description |
|---|---|
| `Appointment` | Records the scheduled date/time, type, and status of a visit between a patient and doctor. |
| `AppointmentType` | Enum — `GENERAL_CONSULTATION`, `SPECIALIST_VISIT`, `FOLLOW_UP`, `EMERGENCY` |
| `AppointmentStatus` | Enum — `PENDING`, `CONFIRMED`, `COMPLETED`, `CANCELLED` |

### 3. Payment Module
| Class | Description |
|---|---|
| `Payment` | Created automatically when an appointment is confirmed; records the booking fee transaction. |
| `PaymentMethod` | Enum — `CREDIT_CARD`, `DEBIT_CARD`, `CASH`, `INSURANCE` |
| `PaymentStatus` | Enum — `PENDING`, `SUCCESSFUL`, `FAILED`, `REFUNDED` |

### 4. Medication Module
| Class | Description |
|---|---|
| `Prescription` | Issued by a doctor; specifies which medications a patient requires. |
| `Medication` | Represents a drug in the system, including price and whether a prescription is required. |
| `MedicationOrder` | Placed by a patient to order medication; may reference a prescription. |
| `OrderStatus` | Enum — `PLACED`, `PROCESSING`, `READY`, `DISPATCHED`, `DELIVERED` |
| `Pharmacy` | Processes medication orders and manages medication stock. |

---

## Key Relationships

```
Patient ──(books 1..*)──────────► Appointment
                                        │
                                 (generates 1)
                                        │
                                        ▼
Patient ──(makes 1..*)──────────► Payment

Doctor  ──(issues 1..*)─────────► Prescription
                                        │
                                 (based on 0..1)
                                        │
Patient ──(places 1..*)─────────► MedicationOrder ──► Pharmacy
                                        │
                                 (includes 1..*)
                                        │
                                        ▼
                                    Medication
```

---

## Design Decisions

- **`Appointment` generates `Payment`** — The booking fee payment is triggered by appointment confirmation, keeping the two concerns linked but separate.
- **`Prescription` is optional on `MedicationOrder`** — Supports both prescription-required and over-the-counter medication orders.
- **Enumerations for all status fields** — Enforces valid state transitions and avoids hardcoded strings.
- **`Pharmacy` is a dedicated class** — Separates inventory management and order fulfilment from the ordering logic.

---

## Files

| File | Description |
|---|---|
| `README.md` | This document |
| `clinic-class-diagram.drawio` | Editable UML class diagram (open with [draw.io](https://app.diagrams.net)) |
