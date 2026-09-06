CREATE DATABASE manufacturing_analytics;

USE manufacturing_analytics;

CREATE TABLE production_data (
    Date DATE,
    Production_Line VARCHAR(50),
    Machine_ID VARCHAR(20),
    Product VARCHAR(50),
    Target_Production INT,
    Actual_Production INT,
    Defective_Units INT,
    Downtime_Minutes INT,
    Operating_Hours DECIMAL(5,2)
);