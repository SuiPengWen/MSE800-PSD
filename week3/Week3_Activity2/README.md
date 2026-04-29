# Week 3 Activity 2: Money Exchange Software Database Design

## 1. Project Overview
This project presents the database design for a **finance money exchange software application**. The system enables users to manage multi-currency wallets, perform exchange transactions, set rate alerts, and manage secure account credentials.

---

## 2. ER Diagram Entities & Attributes
All entities include primary keys (PK), foreign keys (FK), and a minimum of 5 attributes as required:

### Customer
Represents a registered user of the platform.
- `customer_id(PK)`
- `full_name`
- `email_address`
- `residential_address`
- `phone_number`

### Wallet
Represents a user's balance in a specific currency.
- `wallet_id(PK)`
- `customer_id(FK)`
- `currency_code`
- `available_balance`
- `created_at`

### ExchangeTransaction
Records every currency exchange operation.
- `transaction_id(PK)`
- `customer_id(FK)`
- `source_wallet_id(FK)`
- `destination_wallet_id(FK)`
- `transaction_datetime`
- `source_amount`
- `destination_amount`

### RateAlert
Stores user-defined alerts for target exchange rates.
- `alert_id(PK)`
- `customer_id(FK)`
- `base_currency_code`
- `target_currency_code`
- `target_rate_threshold`

### UserCredential
Stores secure authentication details for users.
- `credential_id(PK)`
- `customer_id(FK)`
- `credential_type`
- `password_hash`
- `is_active`

---

## 3. Entity Relationships
| Relationship | Cardinality | Description |
| :--- | :--- | :--- |
| `Customer` ↔ `RateAlert` | 1:N | One customer can set multiple rate alerts; each alert belongs to one customer. |
| `Customer` ↔ `Wallet` | 1:N | One customer can own multiple currency wallets; each wallet belongs to one customer. |
| `Customer` ↔ `ExchangeTransaction` | 1:N | One customer can perform multiple transactions; each transaction belongs to one customer. |
| `Customer` ↔ `UserCredential` | 1:N | One customer can have multiple security credentials; each credential belongs to one customer. |
| `Wallet` ↔ `ExchangeTransaction` | N:M | A wallet can be the source or destination in multiple transactions; each transaction requires one source and one destination wallet. |

---

## 4. Design Compliance
- ✅ 5+ entities defined
- ✅ Each entity has ≥5 attributes (including PK/FK)
- ✅ All relationships are labeled with cardinality (1:N, N:M)
- ✅ Schema aligns with real-world money exchange business logic

---

## 5. Submission Files
- `week3_act2_money_exchange_er.drawio`: Editable ER diagram source file
- `week3_act2_money_exchange_er.png`: Exported ER diagram image