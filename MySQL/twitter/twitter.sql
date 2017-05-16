-- Joining TABLES
-- Join
-- Find All the clients (first and last name) billing amounts and charged date
SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id
-- list all the domain names and leads (first and last name) for each site
SELECT sites.domain_name, leads.first_name, leads.last_name
FROM sites
JOIN leads ON sites.id = leads.id;
-- JOIN ON MULTIPLE TABLES
-- Get the names of the clients, their domain names and the first names of all the leads generated from those sites.
SELECT CONCAT_WS(' ',clients.first_name, clients.last_name) AS full_name, sites.domain_name, leads.first_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id;
-- LEFT & RIGHT JOIN
-- List all the clients and the sites each client has, even if the client hasn't landed a site yet.
SELECT CONCAT_WS(' ',clients.first_name, clients.last_name) AS full_name, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.id = sites.clients_id;
-- GROUPING ROWS
SELECT clients.first_name, clients.last_name, SUM(billing.amount), billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id;
-- GROUP CONCAT
SELECT GROUP_CONCAT(sites.domain_name) AS domains, clients.first_name, clients.last_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP by clients.id;





-- COUNT
-- find the total number of leads for each site

SELECT COUNT(leads.id), sites.domain_name
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;















