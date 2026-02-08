## Logical Schema Diagram

<p align="center">
  <img src="https://github.com/user-attachments/assets/97ee2d75-559f-437d-a065-04df7462c51b" width="800"/>
</p>


# Logical Schema Explanation

## Design Principles
- 3rd Normal Form (3NF)
- Avoid data duplication
- Clear foreign key relationships
- Scalable for multi-country operations

---

## Tables

### Orders
Stores core order-level information.

Primary Key:
- order_id

Foreign Key:
- marketplace_id

---

### Payments
Captures payment details per order.

Relationship:
- One order can have multiple payments

---

### Fulfillment Orders
Stores shipping and fulfillment-related information.

---

### Finance Orders
Contains SKU-level profitability and quantity details.

---

### Marketplace
Dimension table holding country, region, and currency information.

---

## Relationships
Marketplace → Orders → Payments  
Marketplace → Orders → Fulfillment Orders  
Marketplace → Orders → Finance Orders
