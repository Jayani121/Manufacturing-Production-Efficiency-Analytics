import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/manufacturing_production_data.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Create calculated columns
df["Good_Units"] = df["Actual_Production"] - df["Defective_Units"]

df["Production_Achievement_%"] = (
    df["Actual_Production"] / df["Target_Production"]
) * 100

df["Quality_Rate_%"] = (
    df["Good_Units"] / df["Actual_Production"]
) * 100

df["Availability_%"] = (
    (480 - df["Downtime_Minutes"]) / 480
) * 100

df["Performance_%"] = (
    df["Actual_Production"] / df["Target_Production"]
) * 100

df["OEE_%"] = (
    df["Availability_%"]
    * df["Performance_%"]
    * df["Quality_Rate_%"]
) / 10000


# ============================================================
# 1. MONTHLY PRODUCTION TREND
# ============================================================

monthly = df.groupby(
    df["Date"].dt.to_period("M")
).agg(
    Target=("Target_Production", "sum"),
    Actual=("Actual_Production", "sum")
).reset_index()

monthly["Date"] = monthly["Date"].dt.to_timestamp()

plt.figure(figsize=(12, 6))

plt.plot(
    monthly["Date"],
    monthly["Target"],
    marker="o",
    label="Target Production"
)

plt.plot(
    monthly["Date"],
    monthly["Actual"],
    marker="o",
    label="Actual Production"
)

plt.title("Monthly Target vs Actual Production")
plt.xlabel("Month")
plt.ylabel("Production Units")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 2. PRODUCTION BY LINE
# ============================================================

line_production = df.groupby("Production_Line")[
    ["Target_Production", "Actual_Production"]
].sum()

line_production.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Target vs Actual Production by Production Line")
plt.xlabel("Production Line")
plt.ylabel("Production Units")
plt.xticks(rotation=0)
plt.legend(["Target", "Actual"])
plt.tight_layout()
plt.show()


# ============================================================
# 3. DOWNTIME BY MACHINE
# ============================================================

machine_downtime = df.groupby("Machine_ID")[
    "Downtime_Minutes"
].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))

machine_downtime.plot(kind="bar")

plt.title("Total Downtime by Machine")
plt.xlabel("Machine")
plt.ylabel("Downtime (Minutes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 4. DEFECT RATE BY PRODUCT
# ============================================================

product_quality = df.groupby("Product").agg(
    Actual_Production=("Actual_Production", "sum"),
    Defective_Units=("Defective_Units", "sum")
)

product_quality["Defect_Rate_%"] = (
    product_quality["Defective_Units"]
    / product_quality["Actual_Production"]
) * 100

plt.figure(figsize=(9, 6))

product_quality["Defect_Rate_%"].plot(
    kind="bar"
)

plt.title("Defect Rate by Product")
plt.xlabel("Product")
plt.ylabel("Defect Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ============================================================
# 5. OEE BY PRODUCTION LINE
# ============================================================

line_oee = df.groupby("Production_Line")[
    "OEE_%"
].mean().sort_values(ascending=False)

plt.figure(figsize=(9, 6))

line_oee.plot(kind="bar")

plt.title("Average OEE by Production Line")
plt.xlabel("Production Line")
plt.ylabel("OEE (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


print("\nVisualization completed successfully!")