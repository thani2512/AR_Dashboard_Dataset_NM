import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def generate_3d_data():
"""Generate 3D visualization data for AR"""
df = pd.read_csv('sales_data.csv')
# Create 3D bar chart data
person_monthly = df.groupby(['person', 'month'])['salary'].sum().reset_index()
bars_data = []
for _, row in person_monthly.iterrows():
bars_data.append({
'person': row['person'],
'month': int(row['month']),
'value': int(row['salary']),
'height': float(row['salary'] / 1000), # Scale for AR
'color': get_person_color(row['person'])
})
return {
'bars': bars_data,
'max_value': int(df['salary'].max()),
'grid_size': {'x': 4, 'z': 12} # 4 persons, 12 months
}
def get_person_color(person):
"""Get color for each person"""
colors = {
'Krishna': '#FF6B6B',
'Daniel': '#4ECDC4',
'Bubhesk': '#45B7D1',
'Ali': '#96CEB4'
}
return colors.get(person, '#CCCCCC')