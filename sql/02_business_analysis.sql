USE manufacturing_analytics;

SELECT
    SUM(Target_Production) AS Total_Target,
    SUM(Actual_Production) AS Total_Actual,
    SUM(Defective_Units) AS Total_Defects,
    ROUND(
        SUM(Actual_Production) / SUM(Target_Production) * 100,
        2
    ) AS Production_Achievement_Percent
FROM production_data;

SELECT
    Production_Line,
    SUM(Target_Production) AS Target_Production,
    SUM(Actual_Production) AS Actual_Production,
    SUM(Defective_Units) AS Defective_Units,
    SUM(Downtime_Minutes) AS Downtime_Minutes,
    ROUND(
        SUM(Actual_Production) / SUM(Target_Production) * 100,
        2
    ) AS Achievement_Percent
FROM production_data
GROUP BY Production_Line
ORDER BY Achievement_Percent DESC;
SELECT
    Machine_ID,
    SUM(Downtime_Minutes) AS Total_Downtime_Minutes,
    ROUND(
        SUM(Downtime_Minutes) / 60,
        2
    ) AS Total_Downtime_Hours
FROM production_data
GROUP BY Machine_ID
ORDER BY Total_Downtime_Minutes DESC;
SELECT
    Product,
    SUM(Actual_Production) AS Actual_Production,
    SUM(Defective_Units) AS Defective_Units,
    ROUND(
        SUM(Defective_Units) / SUM(Actual_Production) * 100,
        2
    ) AS Defect_Rate_Percent
FROM production_data
GROUP BY Product
ORDER BY Defect_Rate_Percent DESC;
SELECT
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(Target_Production) AS Target_Production,
    SUM(Actual_Production) AS Actual_Production,
    ROUND(
        SUM(Actual_Production) / SUM(Target_Production) * 100,
        2
    ) AS Achievement_Percent
FROM production_data
GROUP BY DATE_FORMAT(Date, '%Y-%m')
ORDER BY Month;
SELECT
    Machine_ID,
    ROUND(
        SUM(Actual_Production) / SUM(Target_Production) * 100,
        2
    ) AS Achievement_Percent,
    SUM(Downtime_Minutes) AS Downtime_Minutes
FROM production_data
GROUP BY Machine_ID
ORDER BY Achievement_Percent ASC
LIMIT 1;
SELECT
    Machine_ID,
    ROUND(
        SUM(Actual_Production) / SUM(Target_Production) * 100,
        2
    ) AS Achievement_Percent,
    SUM(Downtime_Minutes) AS Downtime_Minutes
FROM production_data
GROUP BY Machine_ID
ORDER BY Achievement_Percent DESC
LIMIT 1;