SELECT Orders.order_id, Orders.customer_id, Orders.order_date
FROM Orders
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
WHERE Order_Items.product_id IN (SELECT product_id FROM products WHERE product_name = 'iPhone');
