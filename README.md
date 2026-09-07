# 🏭 Manufacturing Production Efficiency Analytics

An end-to-end **Manufacturing Analytics & Business Intelligence** project built using **Python, SQL, and Microsoft Power BI** to analyze production efficiency, machine performance, quality, defects, downtime, and Overall Equipment Effectiveness (OEE).

The project transforms raw manufacturing data into meaningful business insights through **data generation, data analysis, SQL-based business analysis, KPI development, and interactive Power BI dashboards**.

---

## 📊 Project Overview

Manufacturing organizations need to continuously monitor production efficiency, machine utilization, quality, downtime, and equipment effectiveness to improve operational performance.

This project provides a centralized analytical view of manufacturing operations and helps identify:

* Production performance against targets
* Underperforming production lines and machines
* Downtime patterns
* Defect and quality issues
* Production variances
* Overall Equipment Effectiveness (OEE)
* Production trends over time
* Machine-level performance

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Analyze manufacturing production performance
* Compare target production with actual production
* Measure production achievement
* Analyze machine-level performance
* Monitor OEE and availability
* Identify defect patterns
* Analyze downtime across production lines
* Evaluate production variance
* Develop manufacturing KPIs
* Build an interactive Business Intelligence dashboard
* Demonstrate an end-to-end data analytics workflow

---

## 🔄 Project Workflow

```text
Python
   │
   ▼
Data Generation
   │
   ▼
CSV Dataset
   │
   ▼
Python Data Analysis
   │
   ▼
SQL Business Analysis
   │
   ▼
Power Query
   │
   ▼
DAX Measures & KPIs
   │
   ▼
Power BI Dashboard
   │
   ▼
Business Insights
```

---

## 🛠️ Tools & Technologies

| Tool / Technology     | Purpose                         |
| --------------------- | ------------------------------- |
| 🐍 Python             | Data generation and analysis    |
| 💻 Visual Studio Code | Python development environment  |
| 🗄️ SQL               | Database and business analysis  |
| 📊 Microsoft Power BI | Dashboard development           |
| 🔄 Power Query        | Data transformation             |
| 📐 DAX                | KPI and analytical calculations |
| 📁 CSV                | Dataset storage                 |
| 📈 Data Visualization | Business performance analysis   |

---

## 📁 Project Structure

```text
Manufacturing-Production-Efficiency-Analytics/
│
├── README.md
├── generate_data.py
│
├── data/
│   └── manufacturing_production_data.csv
│
├── dashboard/
│   └── D.pbix
│
├── notebooks/
│   ├── 01_data_analysis.py
│   └── 02_visualization.py
│
├── sql/
│   ├── 01_create_database.sql
│   └── 02_business_analysis.sql
│
└── screenshots/
    ├── Executive Overview.PNG
    ├── Machine & Production Analysis.PNG
    ├── Quality & Defect Analysis.PNG
    └── Production Trends.PNG
```

---

## 📊 Dataset

The dataset contains **2,920 manufacturing records**.

### Dataset Columns

| Column              | Description                   |
| ------------------- | ----------------------------- |
| `Date`              | Production date               |
| `Production_Line`   | Manufacturing production line |
| `Machine_ID`        | Machine identifier            |
| `Product`           | Product manufactured          |
| `Target_Production` | Planned production quantity   |
| `Actual_Production` | Actual production quantity    |
| `Defective_Units`   | Number of defective units     |
| `Downtime_Minutes`  | Machine downtime in minutes   |
| `Operating_Hours`   | Machine operating hours       |

---

## 📈 Key Performance Indicators

| KPI                       |              Value |
| ------------------------- | -----------------: |
| 🎯 Target Production      |      **2,918,029** |
| 🏭 Actual Production      |      **2,625,346** |
| ⚠️ Defective Units        |        **116,782** |
| ⏱️ Total Downtime         | **4,654.55 hours** |
| 📈 Production Achievement |         **89.96%** |
| ✅ Quality Rate            |         **95.56%** |
| ⚠️ Defect Rate            |          **4.44%** |
| ⚙️ Availability           |         **80.07%** |
| 🎯 OEE                    |         **68.85%** |

---

## 🧮 Key Calculations

### Production Achievement

Measures actual production against the planned production target.

```text
Production Achievement =
Actual Production / Target Production × 100
```

### Defect Rate

Measures the percentage of defective units relative to actual production.

```text
Defect Rate =
Defective Units / Actual Production × 100
```

### Quality Rate

Measures the percentage of production that meets quality requirements.

```text
Quality Rate =
1 − Defect Rate
```

### Production Variance

Measures the difference between actual production and target production.

```text
Production Variance =
Actual Production − Target Production
```

A positive value indicates that production exceeded the target, while a negative value indicates that production was below target.

### Overall Equipment Effectiveness (OEE)

OEE is calculated using three major components:

```text
OEE =
Availability × Performance × Quality
```

OEE provides an overall measure of manufacturing equipment effectiveness.

---

# 📑 Power BI Dashboard

The Power BI report consists of **four analytical pages** designed to provide different perspectives of manufacturing performance.

---

## 1️⃣ Executive Overview

Provides a high-level summary of overall manufacturing performance.

### Key Metrics

* Target Production
* Actual Production
* Production Achievement
* OEE
* Availability
* Quality Rate
* Defect Rate
* Downtime

### 📷 Dashboard Preview

![Executive Overview](Screenshots/Executive%20Overview.PNG)

---

## 2️⃣ OEE & Machine Performance

This page focuses on machine-level operational performance.

### Analysis Includes

* OEE by Machine
* Machine performance comparison
* Availability
* Quality
* Downtime
* Production-line performance
* Machine-level production analysis

Conditional formatting and data bars are used to make performance differences easier to identify.

### 📷 Dashboard Preview

![Machine & Production Analysis](Screenshots/Machine%20%26%20Production%20Analysis.PNG)

---

## 3️⃣ Quality & Defect Analysis

This page focuses on manufacturing quality and defect patterns.

### Analysis Includes

* Quality Rate by Production Line
* Defective Units by Product
* Defective Units by Production Line
* Defect Rate Trend
* Production-line quality comparison

The analysis helps identify products and production lines associated with higher defect levels.

### 📷 Dashboard Preview

![Quality & Defect Analysis](Screenshots/Quality%20%26%20Defect%20Analysis.PNG)

---

## 4️⃣ Production Trends & Performance

This page analyzes production output and performance over time.

### Analysis Includes

* Target vs Actual Production Trend
* Downtime Trend by Production Line
* Production Variance by Line
* Production Achievement
* Date-based production analysis

Interactive filters allow users to analyze specific periods, production lines, and products.

### 📷 Dashboard Preview

![Production Trends](Screenshots/Production%20Trends.PNG)

---

## 🎛️ Dashboard Interactivity

The Power BI dashboard includes:

* 📅 Date range slicers
* 🏭 Production Line filters
* 📦 Product filters
* 📊 Interactive charts
* 🎯 KPI cards
* 🔎 Drill-down analysis
* 🎨 Conditional formatting
* 🧭 Page navigation
* 📈 Trend analysis
* ⚙️ Machine performance comparison

---

# 🐍 Python Analysis

Python was used as part of the data analytics workflow.

### Python was used for:

* Manufacturing data generation
* Data preparation
* Exploratory data analysis
* Data visualization
* Identifying patterns in production data

### Python Libraries

* **Pandas**
* **NumPy**
* **Matplotlib**

Python development and analysis were performed using **Visual Studio Code**.

---

# 🗄️ SQL Analysis

SQL was used to demonstrate database-based business analysis and extract meaningful manufacturing insights.

### Database Creation

`sql/01_create_database.sql`

Used to create and prepare the manufacturing database structure.

### Business Analysis

`sql/02_business_analysis.sql`

Contains analytical SQL queries for extracting manufacturing performance insights.

---

# 💡 Business Insights

This dashboard can help manufacturing teams:

* Identify underperforming machines
* Monitor production efficiency
* Compare planned and actual production
* Identify high-defect products
* Analyze downtime patterns
* Compare production-line performance
* Monitor OEE
* Track production trends
* Identify production shortfalls
* Support data-driven operational decisions

---

# 🚀 Potential Future Improvements

Future versions of this project could include:

* Real-time manufacturing data integration
* Predictive maintenance analysis
* Machine failure prediction
* Downtime root-cause analysis
* Production forecasting
* Automated Power BI data refresh
* Machine learning-based production optimization
* Anomaly detection
* Advanced OEE analysis

---

# 📚 Skills Demonstrated

### Data Analytics

* Data Analytics
* Exploratory Data Analysis
* KPI Development
* Business Analysis
* Data Visualization
* Manufacturing Analytics
* Operational Analytics
* Performance Monitoring
* Trend Analysis
* Data-Driven Decision Making

### Technical Skills

* Python
* SQL
* Power BI
* DAX
* Power Query
* Excel / CSV
* Visual Studio Code
* Business Intelligence
* Dashboard Design
* Interactive Reporting

---

# 👩‍💻 Author

**Jayani Kaveesha**

**BSc Physical Science | Data Analytics & Business Intelligence Enthusiast**

### Areas of Interest

* Data Analytics
* Business Intelligence
* Business Analysis
* Power BI
* SQL
* Python
* Data Visualization

---

# ⭐ Project Highlights

### Python → SQL → Power BI

An end-to-end manufacturing analytics project demonstrating how raw manufacturing data can be transformed into meaningful business insights using **Python, SQL, Power BI, Power Query, and DAX**.

The project demonstrates the complete analytics workflow from **data generation and preparation to business analysis, KPI development, visualization, and data-driven decision-making**.
