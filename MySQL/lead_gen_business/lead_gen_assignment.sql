-- 1. What query would you run to get 
-- the total revenue for March of 2012?
SELECT billing.charged_datetime AS month, SUM(amount) as total_revenue
FROM billing
WHERE MONTH(billing.charged_datetime) = 3 AND YEAR(billing.charged_datetime) = 2012;
-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT billing.client_id, SUM(billing.amount)
FROM billing
WHERE billing.client_id = 2;
-- 3. What query would you run to get all the sites that client=10 owns?
SELECT sites.client_id, sites.domain_name
FROM sites
WHERE sites.client_id = 10;
-- 4. What query would you run to get total # of sites created
-- per month per year for the client with an id of 1? What about for client=20?
-- total sites per month per year, for client
SELECT sites.client_id, COUNT(sites.domain_name), date_format(sites.created_datetime, '%M') AS month,
date_format(sites.created_datetime, '%Y') AS year
FROM sites
WHERE sites.client_id = 1
GROUP BY month, year;

-- 5. What query would you run to get the total # of leads
-- generated for each of the sites between January 1, 2011 to February 15, 2011?

SELECT sites.domain_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_registered
FROM sites
	LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY sites.site_id;

-- 6. What query would you run to get a list of client names and the total # of leads we've
-- generated for each of our clients between January 1, 2011 to December 31, 2011?

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_generated
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id;

-- 7. What query would you run to get a list of client names and the total # of leads
-- we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT concat(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads_id), DATE_FORMAT(leads.registered_datetime, '%M') AS 'month'
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY clients.client_id, MONTH(leads.registered_datetime)
ORDER BY MONTH(leads.registered_datetime);
