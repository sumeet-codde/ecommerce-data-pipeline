-- ============================================
-- E-COMMERCE DATA ANALYSIS
-- ============================================


-- 1. View all orders
SELECT *
FROM orders_processed;


-- 2. Total number of orders
SELECT COUNT(*) AS total_orders
FROM orders_processed;


-- 3. Total revenue from delivered orders
SELECT SUM(revenue) AS total_revenue
FROM orders_processed
WHERE status = 'Delivered';


-- 4. Average order value
SELECT AVG(revenue) AS average_order_value
FROM orders_processed
WHERE status = 'Delivered';


-- 5. Revenue by product
SELECT
    product_id,
    SUM(revenue) AS total_revenue
FROM orders_processed
WHERE status = 'Delivered'
GROUP BY product_id
ORDER BY total_revenue DESC;


-- 6. Revenue by customer
SELECT
    customer_id,
    SUM(revenue) AS total_revenue
FROM orders_processed
WHERE status = 'Delivered'
GROUP BY customer_id
ORDER BY total_revenue DESC;


-- 7. Order count by status
SELECT
    status,
    COUNT(*) AS order_count
FROM orders_processed
GROUP BY status
ORDER BY order_count DESC;