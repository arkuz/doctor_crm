import os

python = 'python'

os.remove('webapp.db')
os.system(f'{python} create_db.py')
os.system(f'{python} add_test_doctors_to_db.py')
os.system(f'{python} add_test_timing_to_db.py')
os.system(f'{python} add_test_cases_to_db.py')
