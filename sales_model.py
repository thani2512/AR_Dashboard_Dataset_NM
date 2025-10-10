import pandas as pd
import numpy as np
def get_person_data():
"""Get person salary performance for AR visualization"""
df = pd.read_csv('sales_data.csv')
person_stats = df.groupby('person').agg({
'salary': ['sum', 'mean', 'count']
}).round(2)
return {
person: {
'total_salary': int(stats[('salary', 'sum')]),
'avg_salary': float(stats[('salary', 'mean')]),
'months_recorded': int(stats[('salary', 'count')]),
'position': get_ar_position(person)
}
for person, stats in person_stats.iterrows()
}
def get_trend_data(person=None):
"""Get monthly salary trend for AR timeline"""
df = pd.read_csv('sales_data.csv')
if person:
monthly_trends = df[df['person'] ==
person].groupby('month')['salary'].sum().to_dict()
else:
monthly_trends = df.groupby('month')['salary'].sum().to_dict()
return {str(k): int(v) for k, v in monthly_trends.items()}
def get_ar_position(person):
"""Map persons to AR world positions"""
positions = {
'Krishna': {'x': 0, 'y': 1, 'z': 2},
'Daniel': {'x': 0, 'y': 1, 'z': -2},
'Bubhesk': {'x': 2, 'y': 1, 'z': 0},
'Ali': {'x': -2, 'y': 1, 'z': 0}
}
return positions.get(person, {'x': 0, 'y': 1, 'z': 0})

def get_kpis():
"""Get key performance indicators for dashboard"""
df = pd.read_csv('sales_data.csv')
total_salary = int(df['salary'].sum())
person_totals = df.groupby('person')['salary'].sum()
top_person = person_totals.idxmax()
# Growth rate mock
current_month = df[df['month'] == df['month'].max()]['salary'].sum()
prev_month = df[df['month'] == df['month'].max() - 1]['salary'].sum()
growth_rate = f"{((current_month - prev_month) / prev_month * 100):.1f}%"
return {
'total_salary': total_salary,
'top_person': top_person,
'growth_rate': growth_rate
}