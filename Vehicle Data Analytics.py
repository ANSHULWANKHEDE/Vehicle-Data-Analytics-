import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate synthetic vehicle telemetry data
def generate_vehicle_telemetry_data(num_vehicles, start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date, freq='H')
    num_records = len(date_range) * num_vehicles
    
    vehicle_data = {
        'Timestamp': np.tile(date_range, num_vehicles),
        'Vehicle_ID': np.repeat(np.arange(1, num_vehicles + 1), len(date_range)),
        'Speed': np.random.uniform(0, 120, num_records),
        'Fuel_Level': np.random.uniform(10, 100, num_records),
        'Engine_Temperature': np.random.uniform(70, 120, num_records),
        'Odometer': np.random.uniform(0, 100000, num_records),
        'GPS_Latitude': np.random.uniform(-90, 90, num_records),
        'GPS_Longitude': np.random.uniform(-180, 180, num_records)
    }

    telemetry_df = pd.DataFrame(vehicle_data)
    return telemetry_df

# Function to generate synthetic maintenance records
def generate_maintenance_data(num_vehicles, start_date, end_date, num_records):
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    maintenance_data = {
        'Date': np.random.choice(date_range, num_records),
        'Vehicle_ID': np.random.randint(1, num_vehicles + 1, num_records),
        'Maintenance_Type': np.random.choice(['Oil Change', 'Tire Rotation', 'Brake Check', 'Engine Check'], num_records),
        'Cost': np.random.uniform(50, 300, num_records)
    }

    maintenance_df = pd.DataFrame(maintenance_data)
    return maintenance_df

# Function to generate synthetic customer feedback data
def generate_feedback_data(num_vehicles, start_date, end_date, num_records):
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    feedback_data = {
        'Date': np.random.choice(date_range, num_records),
        'Vehicle_ID': np.random.randint(1, num_vehicles + 1, num_records),
        'Feedback_Score': np.random.randint(1, 6, num_records),
        'Feedback_Text': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Terrible'], num_records)
    }

    feedback_df = pd.DataFrame(feedback_data)
    return feedback_df

# Parameters for data generation
num_vehicles = 100  # Number of vehicles
start_date = '2023-01-01'
end_date = '2023-12-31'
num_maintenance_records = 1000
num_feedback_records = 1000

# Generate datasets
telemetry_df = generate_vehicle_telemetry_data(num_vehicles, start_date, end_date)
maintenance_df = generate_maintenance_data(num_vehicles, start_date, end_date, num_maintenance_records)
feedback_df = generate_feedback_data(num_vehicles, start_date, end_date, num_feedback_records)

# Save to CSV files
telemetry_df.to_csv('large_vehicle_telemetry.csv', index=False)
maintenance_df.to_csv('large_vehicle_maintenance.csv', index=False)
feedback_df.to_csv('large_vehicle_feedback.csv')

# Output the shape of the generated data
print(f"Telemetry Data: {telemetry_df.shape}")
print(f"Maintenance Data: {maintenance_df.shape}")
print(f"Feedback Data: {feedback_df.shape}")