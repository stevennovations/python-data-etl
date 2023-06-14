SELECT Orders.order_id, Products.product_name, Order_Items.quantity
FROM Orders
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
RIGHT JOIN Products ON Order_Items.product_id = Products.product_id;
