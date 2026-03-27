import json
from app import app, db

with app.app_context():
    db.create_all()

client = app.test_client()

# Test 1: POST /api/student successful
data = {'student_id': 101, 'first_name': 'Narendra', 'last_name': 'Mishra', 'roll_number': 'MA19M010'}
resp = client.post('/api/student', data=json.dumps(data), content_type='application/json')
print('POST /api/student successful case:', resp.status_code, resp.data)

# Test 3: POST /api/student missing parameter
resp2 = client.post('/api/student', data=json.dumps({'first_name': 'Narendra'}), content_type='application/json')
print('POST /api/student missing param:', resp2.status_code, resp2.data)
