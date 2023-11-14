-- Displaying the average temperature (Fahrenheit) by city ordered by descending temperatures.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;