import os
import random
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/person-data')
def person_data():
 try:
    import pandas as pd
    df = pd.read_csv("sales_data.csv")
    persons = df['person'].unique().tolist()
    data = {}
    for person in persons:
      person_df = df[df['person'] == person]
      total = int(person_df['salary'].sum())
      monthly = {int(row['month']): int(row['salary']) for _, row in
person_df.iterrows()}
      data[person] = {
        "total_salary": total,
        "monthly": monthly
    }
    return jsonify(data)

 except Exception as e:
    return jsonify({'error': str(e)}), 500
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
   