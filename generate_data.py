import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# For reproducible results
np.random.seed(42)
random.seed(42)

# Configuration
start_date = datetime(2025, 1, 1)
num_days = 365

production_lines = ["Line 1", "Line 2", "Line 3", "Line 4"]
machines = {
    "Line 1": ["M101", "M102"],
    "Line 2": ["M201", "M202"],
    "Line 3": ["M301", "M302"],
    "Line 4": ["M401", "M402"]
}

products = ["Product A", "Product B", "Product C", "Product D"]

data = []

for day in range(num_days):
    current_date = start_date + timedelta(days=day)

    for line in production_lines:
        for machine in machines[line]:

            product = random.choice(products)

            target_production = random.randint(800, 1200)

            efficiency_factor = random.uniform(0.75, 1.05)

            actual_production = int(
                target_production * efficiency_factor
            )

            defective_units = random.randint(
                int(actual_production * 0.01),
                int(actual_production * 0.08)
            )

            downtime_minutes = random.randint(10, 180)

            operating_hours = round(
                8 - (downtime_minutes / 60),
                2
            )

            data.append([
                current_date,
                line,
                machine,
                product,
                target_production,
                actual_production,
                defective_units,
                downtime_minutes,
                operating_hours
            ])

# Create DataFrame
columns = [
    "Date",
    "Production_Line",
    "Machine_ID",
    "Product",
    "Target_Production",
    "Actual_Production",
    "Defective_Units",
    "Downtime_Minutes",
    "Operating_Hours"
]

df = pd.DataFrame(data, columns=columns)

# Save dataset
df.to_csv("data/manufacturing_production_data.csv", index=False)

print("Dataset generated successfully!")
print(f"Total records: {len(df)}")

print("\nFirst 5 records:")
print(df.head())