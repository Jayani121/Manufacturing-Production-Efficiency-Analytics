import pandas as pd

# Load dataset
df = pd.read_csv("data/manufacturing_production_data.csv")

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# ============================================================
# KPI CALCULATIONS
# ============================================================

# Good units
df["Good_Units"] = df["Actual_Production"] - df["Defective_Units"]

# Production Achievement
df["Production_Achievement_%"] = (
    df["Actual_Production"] / df["Target_Production"]
) * 100

# Quality Rate
df["Quality_Rate_%"] = (
    df["Good_Units"] / df["Actual_Production"]
) * 100

# Defect Rate
df["Defect_Rate_%"] = (
    df["Defective_Units"] / df["Actual_Production"]
) * 100

# Planned production time = 8 hours
planned_minutes = 8 * 60

# Availability
df["Availability_%"] = (
    (planned_minutes - df["Downtime_Minutes"])
    / planned_minutes
) * 100

# Performance
# Based on actual production compared with target production
df["Performance_%"] = (
    df["Actual_Production"] / df["Target_Production"]
) * 100

# OEE
df["OEE_%"] = (
    df["Availability_%"]
    * df["Performance_%"]
    * df["Quality_Rate_%"]
) / 10000


# ============================================================
# OVERALL KPI SUMMARY
# ============================================================

print("\n========== OVERALL KPI SUMMARY ==========")

print(
    f"Total Target Production: "
    f"{df['Target_Production'].sum():,.0f}"
)

print(
    f"Total Actual Production: "
    f"{df['Actual_Production'].sum():,.0f}"
)

print(
    f"Total Defective Units: "
    f"{df['Defective_Units'].sum():,.0f}"
)

print(
    f"Total Downtime (hours): "
    f"{df['Downtime_Minutes'].sum() / 60:,.2f}"
)

print(
    f"Average Production Achievement: "
    f"{df['Production_Achievement_%'].mean():.2f}%"
)

print(
    f"Average Quality Rate: "
    f"{df['Quality_Rate_%'].mean():.2f}%"
)

print(
    f"Average Defect Rate: "
    f"{df['Defect_Rate_%'].mean():.2f}%"
)

print(
    f"Average Availability: "
    f"{df['Availability_%'].mean():.2f}%"
)

print(
    f"Average OEE: "
    f"{df['OEE_%'].mean():.2f}%"
)


# ============================================================
# PRODUCTION LINE ANALYSIS
# ============================================================

print("\n========== PRODUCTION LINE PERFORMANCE ==========")

line_analysis = df.groupby("Production_Line").agg(
    Target_Production=("Target_Production", "sum"),
    Actual_Production=("Actual_Production", "sum"),
    Defective_Units=("Defective_Units", "sum"),
    Downtime_Minutes=("Downtime_Minutes", "sum"),
    Average_OEE=("OEE_%", "mean")
).reset_index()

line_analysis["Achievement_%"] = (
    line_analysis["Actual_Production"]
    / line_analysis["Target_Production"]
) * 100

line_analysis["Defect_Rate_%"] = (
    line_analysis["Defective_Units"]
    / line_analysis["Actual_Production"]
) * 100

print(line_analysis.round(2))


# ============================================================
# MACHINE PERFORMANCE
# ============================================================

print("\n========== MACHINE PERFORMANCE ==========")

machine_analysis = df.groupby("Machine_ID").agg(
    Target_Production=("Target_Production", "sum"),
    Actual_Production=("Actual_Production", "sum"),
    Defective_Units=("Defective_Units", "sum"),
    Downtime_Minutes=("Downtime_Minutes", "sum"),
    Average_OEE=("OEE_%", "mean")
).reset_index()

machine_analysis["Achievement_%"] = (
    machine_analysis["Actual_Production"]
    / machine_analysis["Target_Production"]
) * 100

print(machine_analysis.round(2))


# ============================================================
# PRODUCT PERFORMANCE
# ============================================================

print("\n========== PRODUCT PERFORMANCE ==========")

product_analysis = df.groupby("Product").agg(
    Target_Production=("Target_Production", "sum"),
    Actual_Production=("Actual_Production", "sum"),
    Defective_Units=("Defective_Units", "sum"),
    Average_OEE=("OEE_%", "mean")
).reset_index()

product_analysis["Achievement_%"] = (
    product_analysis["Actual_Production"]
    / product_analysis["Target_Production"]
) * 100

print(product_analysis.round(2))