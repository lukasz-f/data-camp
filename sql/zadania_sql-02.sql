use northwind;

-- 1. Ile kosztowało najdroższe zamówienie?
select sum(od.quantity * od.unit_price + o.shipping_fee) as total_price from order_details od inner join orders o on o.id = od.order_id group by o.id order by total_price desc limit 1;

-- 2. Jaka jest średnia wartość zamówienia?
select avg(total_price) from (select ifnull(sum(od.quantity * od.unit_price + o.shipping_fee), 0) as total_price from orders o left join order_details od on o.id = od.order_id group by o.id) t;

-- 3. Jaka jest najmniejsza kwota zamówienia dla zamówień zamkniętych (status: closed)?
select sum(od.quantity * od.unit_price + o.shipping_fee) as total_price from orders o left join order_details od on o.id = od.order_id left join orders_status os on o.status_id = os.id where os.status_name = 'Closed' group by o.id order by total_price limit 1;

-- 4. Który pracownik złożył zamówienie na najwyższą kwotę?
select e.first_name, e.last_name, sum(od.quantity * od.unit_price + o.shipping_fee) from employees e left join orders o on e.id = o.employee_id left join order_details od on o.id = od.order_id group by e.id, e.first_name, e.last_name order by sum(od.quantity * od.unit_price + o.shipping_fee) desc limit 1;

-- 5. Który dostawca obsłużył najwięcej zamówień?
select s.first_name, s.last_name from suppliers s left join purchase_orders po on s.id = po.supplier_id group by s.id, s.first_name, s.last_name order by count(po.id) desc limit 1;

-- 6. Który pracownik złożył najmniej zamówień?
select e.first_name, e.last_name from employees e left join purchase_orders po on e.id = po.created_by group by e.id, e.first_name, e.last_name order by count(po.id) limit 1;

-- 7. Który klient wydał najwięcej pieniędzy?
select c.first_name, c.last_name from customers c left join orders o on c.id = o.customer_id left join order_details od on o.id = od.order_id group by c.id, c.first_name, c.last_name order by sum(od.quantity * od.unit_price + o.shipping_fee) desc limit 1;

-- 8. Jakie są sumaryczne wartości zamówień na każdy z produktów?
select p.product_name, ifnull(sum(od.quantity * od.unit_price + o.shipping_fee), 0) as total_price from products p left join order_details od on p.id = od.product_id left join orders o on o.id = od.order_id group by p.id, p.product_name;

-- 9. Jakie są sumaryczne wartości zamówień na każdy z produktów w bieżącej produkcji?
select p.product_name, ifnull(sum(od.quantity * od.unit_price + o.shipping_fee), 0) as total_price from products p left join order_details od on p.id = od.product_id left join orders o on o.id = od.order_id where p.discontinued = false group by p.id, p.product_name;

-- 10. Ile zamówień obsłużył każdy z dostawców?
select s.first_name, s.last_name, count(po.id) from suppliers s left join purchase_orders po on s.id = po.supplier_id group by s.id, s.first_name, s.last_name ;
