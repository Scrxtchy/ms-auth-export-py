import sqlite3
from sys import argv
from qrcode import QRCode
db = sqlite3.connect(argv[1])
cur = db.execute("SELECT name,username,oath_secret_key,identity_provider FROM accounts WHERE account_type = 0")

for entry in cur.fetchall():
	print(f"{entry[0]} - {entry[1]}")
	qr = QRCode()
	qr.add_data(f"otpauth://totp/{entry[0]}:{entry[1]}?secret={entry[2]}{'&issuer=' + entry[3] if entry[3] != '' else ''}")
	qr.print_ascii()
cur.close()
db.close()