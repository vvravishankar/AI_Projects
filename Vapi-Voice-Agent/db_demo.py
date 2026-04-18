from __future__ import annotations

from sqlalchemy import text

from database import engine#, init_db


def run_sql(query: str):
	"""Run a raw SQL query on the same DB used by `database.py`.

	Example:
		rows = run_sql("SELECT * FROM appointments")
		print(rows)
	"""
	#init_db()  # ensures the appointments table exists
	with engine.begin() as conn:
		result = conn.execute(text(query))
		return result.fetchall() if result.returns_rows else result.rowcount


#query = """INSERT INTO appointments (id, patient_name, reason, start_time, canceled, created_at)
#VALUES 
#(1, 'Ravi Kumar', 'General Checkup', '2026-04-20 10:30:00', FALSE, '2026-04-18 17:30:00'),
#(2, 'Neha Sharma', 'Dental Cleaning', '2026-04-21 14:00:00', FALSE, '2026-04-18 17:31:00'),
#(3, 'Amit Verma', 'Eye Examination', '2026-04-22 09:00:00', TRUE, '2026-04-18 17:32:00'),
#(4, 'Priya Singh', 'Follow-up Consultation', '2026-04-23 11:15:00', FALSE, '2026-04-18 17:33:00');
#"""
query = """SELECT * FROM appointments"""
print(run_sql(query))