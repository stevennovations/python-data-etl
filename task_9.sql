WITH CustomerOrders AS (
    SELECT customer_id, COUNT(*) AS total_orders
    FROM Orders
    GROUP BY customer_id
)
SELECT Customers.customer_name, COALESCE(CustomerOrders.total_orders, 0) AS total_orders
FROM Customers
LEFT JOIN CustomerOrders ON Customers.customer_id = CustomerOrders.customer_id;
