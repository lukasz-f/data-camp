use northwind;

-- 1. Napisać zapytanie, które zwróci nazwę produktu oraz kod (product_name, product_code).
select product_name, product_code from products;

-- 2. Napisać zapytanie, które zwróci listę produktów (id oraz nazwę).
select id, product_name from products;

-- 3. Napisać zapytanie, które zwróci listę produktów nieprodukowanych (discontinued).
select * from products where discontinued = true;

-- 4. Napisać zapytanie, które zwróci najdroższy i najtańszy produkt (name, list_price).
select product_name, list_price from products
where list_price = (select max(list_price) from products)
      or list_price = (select min(list_price) from products);

-- 5. Napisać zapytanie, które zwróci listę produktów (id, product_name, list_price), które kosztuję mniej niż $20.
select id, product_name, list_price from products where list_price < 20;

-- 6. Napisać zapytanie, które zwróci listę produktów (id, product_name, list_price), które kosztują pomiędzy $15, a $25.
select id, product_name, list_price from products where list_price between 15 and 25;

-- 7. Napisać zapytanie, które zwróci listę produktów (product_name, list_price), których cena jest wyższa niż cena średnia.
select product_name, list_price from products where list_price > (select avg(list_price) from products);

-- 8. Napisać zapytanie, które zwróci listę produktów (product_name, list_price), która zwróci 10 najdroższych produktów.
select product_name, list_price from products order by list_price desc limit 10;

-- 9. Napisać zapytanie, które zwróci ilość produktów produkowanych i nie produkowanych obecnie (discontinued).
select sum(discontinued = 1) as przerwane, sum(discontinued = 0) as nieprzerwane from products;

-- 10. W tabeli order_details ustwić pole rabat na 0.1 dla produktów, których cena jednostkowa (unit_price) jest większa niż $25.
update order_details set discount = 0.1 where unit_price > 25;

-- 11. Dodać pracownika o własnym imieniu i nazwisku do tabeli employees.
insert into employees(first_name, last_name) values('Łukasz', 'Frankiewicz');
commit;
