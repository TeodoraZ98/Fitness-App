from database import connect_db

# 👇 Replace this with your test username
username = "your_test_username"

conn = connect_db()
c = conn.cursor()
c.execute("UPDATE users SET is_premium = 1 WHERE username = ?", (username,))
conn.commit()
conn.close()

print(f"✅ User '{username}' upgraded to premium!")
