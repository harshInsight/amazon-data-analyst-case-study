# Logical Schema Explanation

## Orders Table
- order_id (Primary Key)
- marketplace_id
- order_status
- purchase_date

## Payments Table
- payment_id (Primary Key)
- order_id (Foreign Key)
- payment_method
- payment_amount

Relationship:
One order can have multiple payments.
