/*
1.
Есть бд “КОФЕЙНЯ”
необходимо спроектировать таблицы “КОФЕ” , “БАРИСТА”, “СМЕНА” 
ЗАПРОСЫ:
Какой бариста на смене
Какие кофе продали на смене
Какой бариста продал кофе (пример “капучино 200 мл”) на смене (пример 10.09.2022)
*/

/*
РЕШЕНИЕ:
В одном дне 4 смены,
баристы меняются каждую смену,
любой бариста может продать любое кофе:
- смена содержит инфу о баристах и проданных ими кофе.
*/

-- /* CREATE */
-- CREATE TABLE IF NOT EXISTS coffee (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- ncoffee NVARCHAR
-- );
-- 
-- CREATE TABLE IF NOT EXISTS barista (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- name NVARCHAR
-- );
-- 
-- CREATE TABLE IF NOT EXISTS shift (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- nshift NVARCHAR,
-- date_time datetime,
-- id_barista INTEGER,
-- id_coffee INTEGER,
-- FOREIGN KEY (id_barista) REFERENCES barista(id),
-- FOREIGN KEY (id_coffee) REFERENCES coffee(id)
-- );

/* INSERT */
/*
INSERT INTO coffee (ncoffee) VALUES
("капучино"),	-- 1
("эспрессо"),	-- 2
("латте"),		-- 3
("американо")	-- 4
;

INSERT INTO barista (name) VALUES
("Бориска"),	-- 1
("Ивасик"),		-- 2
("Ванёк")		-- 3
;

INSERT INTO shift (nshift, date_time, id_barista, id_coffee) VALUES
("смена-1", "2023-09-18 06:00:00", 1, 2),		-- 1
("смена-2", "2023-09-18 12:00:00", 2, 3),		-- 2
("смена-2", "2023-09-18 15:59:00", 2, 4),		-- 3
("смена-3", "2023-09-18 18:00:00", 3, 1),		-- 4
("смена-3", "2023-09-18 18:02:00", 3, 2),		-- 5
("смена-3", "2023-09-18 23:59:00", 3, 1),		-- 6
("смена-4", "2023-09-19 00:01:00", 1, 1),		-- 7
("смена-4", "2023-09-19 01:59:00", 1, 2),		-- 8
("смена-4", "2023-09-19 02:59:00", 1, 3),		-- 9
("смена-4", "2023-09-19 03:59:00", 1, 4),		-- 10
("смена-1", "2023-09-19 06:00:00", 2, 2),		-- 11
("смена-1", "2023-09-19 10:30:00", 2, 3),		-- 12
("смена-2", "2023-09-19 12:59:00", 3, 4),		-- 13
("смена-2", "2023-09-19 14:00:00", 3, 1),		-- 14
("смена-3", "2023-09-19 18:03:00", 1, 2),		-- 15
("смена-3", "2023-09-19 23:58:00", 1, 1),		-- 16
("смена-4", "2023-09-20 01:02:00", 2, 1),		-- 17
("смена-4", "2023-09-20 05:59:00", 2, 2)		-- 18
;
*/
/* SELECT */
/* Какой бариста на смене */
-- SELECT name, nshift, date_time FROM barista, shift 
-- WHERE barista.id = id_barista AND nshift = "смена-1";

/* Какие кофе продали на смене */
-- SELECT ncoffee, nshift, date_time FROM coffee, shift 
-- WHERE coffee.id = id_coffee AND nshift = "смена-1";

/* Какой бариста продал кофе (пример “капучино 200 мл”) на смене (пример 10.09.2022) */
-- SELECT name, ncoffee, nshift, date_time FROM barista, coffee, shift 
-- WHERE coffee.id = id_coffee AND barista.id = id_barista 
-- AND ncoffee = "капучино" AND date_time LIKE "2023-09-19%";