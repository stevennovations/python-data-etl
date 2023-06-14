SELECT DISTINCT Orders.order_id, Orders.order_date
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
WHERE Customers.customer_name = 'John O''Brien';
