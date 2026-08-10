#vehicle rental sysytem

import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect("rental_with_total_price.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Users 
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL)''')
    
    # Vehicles 
    cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
        vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        rate REAL NOT NULL,
        status TEXT DEFAULT 'Available')''')
    
    # Rentals 
    cursor.execute('''CREATE TABLE IF NOT EXISTS rentals (
        rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
        vehicle_id INTEGER REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
        from_date TEXT NOT NULL,
        to_date TEXT NOT NULL,
        total_days INTEGER NOT NULL,
        total_price REAL NOT NULL)''')
    
    # Admin (admin/admin123)
    cursor.execute("INSERT OR IGNORE INTO users (user_id, username, password, role) VALUES (1, 'admin', 'admin123', 'Admin')")
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect("rental_with_total_price.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def register():
    u, p = input("New Username: "), input("New Password: ")
    try:
        conn = get_db()
        conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'Customer')", (u, p))
        conn.commit()
        print("✅ Account created!")
    except sqlite3.IntegrityError:
        print("❌ Username taken!")
    finally:
        conn.close()

def login():
    u, p = input("Username: "), input("Password: ")
    conn = get_db()
    user = conn.execute("SELECT user_id, username, role FROM users WHERE username=? AND password=?", (u, p)).fetchone()
    conn.close()
    if user:
        print(f"\nWelcome {user[1]} ({user[2]})!")
        return {"id": user[0], "role": user[2]}
    print("❌ Invalid credentials!")
    return None


def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---\n1. Add Vehicle\n2. View All Vehicles\n3. Delete Vehicle\n4. View All Rentals\n5. Logout")
        ch = input("Choice: ")
        conn = get_db()
        
        if ch == '1': 
            m, r = input("Model: "), float(input("Daily Rate (₹): "))
            conn.execute("INSERT INTO vehicles (model, rate) VALUES (?, ?)", (m, r))
            conn.commit()
            print("✅ Vehicle added!")
        elif ch == '2': 
            for v in conn.execute("SELECT * FROM vehicles").fetchall():
                print(f"ID: {v[0]} | Model: {v[1]} | Rate: ₹{v[2]}/day | Status: {v[3]}")
        elif ch == '3': 
            vid = int(input("Vehicle ID to delete: "))
            conn.execute("DELETE FROM vehicles WHERE vehicle_id = ?", (vid,))
            conn.commit()
            print("✅ Deleted!")
        elif ch == '4': 
            for r in conn.execute("SELECT r.rental_id, u.username, v.model, r.from_date, r.to_date, r.total_days, r.total_price FROM rentals r JOIN users u ON r.user_id = u.user_id JOIN vehicles v ON r.vehicle_id = v.vehicle_id").fetchall():
                print(f"Rental ID: {r[0]} | User: {r[1]} | Vehicle: {r[2]} | From: {r[3]} | To: {r[4]} | Days: {r[5]} | Total Cost: ₹{r[6]}")
        elif ch == '5':
            conn.close()
            break
        conn.close()


def customer_menu(user):
    while True:
        print("\n--- CUSTOMER MENU ---\n1. View Available Vehicles\n2. Rent Vehicle\n3. Return Vehicle\n4. Logout")
        ch = input("Choice: ")
        conn = get_db()
        
        if ch == '1':
            for v in conn.execute("SELECT * FROM vehicles WHERE status='Available'").fetchall():
                print(f"ID: {v[0]} | Model: {v[1]} | Rate: ₹{v[2]}/day")
        elif ch == '2': 
            vid = int(input("Vehicle ID to rent: "))
            v = conn.execute("SELECT status, rate FROM vehicles WHERE vehicle_id=?", (vid,)).fetchone()
            
            if v and v[0] == 'Available':
                daily_rate = v[1]
                from_d_str = input("From Date (DD/MM/YYYY): ")
                to_d_str = input("To Date (DD/MM/YYYY): ")
                
                try:
                    
                    d1 = datetime.strptime(from_d_str, "%d/%m/%Y")
                    d2 = datetime.strptime(to_d_str, "%d/%m/%Y")
                    total_days = (d2 - d1).days
                    
                    if total_days <= 0:
                        print("❌ End date must be after start date!")
                        conn.close()
                        continue
                    
                   
                    total_price = total_days * daily_rate
                    
                   
                    print(f"\n--- BOOKING SUMMARY ---")
                    print(f"Duration: {total_days} day(s)")
                    print(f"Daily Rate: ₹{daily_rate}")
                    print(f"Total Amount Payable: ₹{total_price}")
                    
                    confirm = input("Confirm Booking? (yes/no): ").lower()
                    if confirm == 'yes':
                        conn.execute("INSERT INTO rentals (user_id, vehicle_id, from_date, to_date, total_days, total_price) VALUES (?, ?, ?, ?, ?, ?)", 
                                     (user['id'], vid, from_d_str, to_d_str, total_days, total_price))
                        conn.execute("UPDATE vehicles SET status='Rented' WHERE vehicle_id=?", (vid,))
                        conn.commit()
                        print("✅ Rented successfully!")
                    else:
                        print("❌ Booking cancelled.")
                        
                except ValueError:
                    print("❌ Invalid date format! Please use DD/MM/YYYY (e.g., 15/08/2026).")
            else:
                print("❌ Vehicle unavailable or invalid ID!")
                
        elif ch == '3': 
            vid = int(input("Vehicle ID to return: "))
            conn.execute("DELETE FROM rentals WHERE user_id=? AND vehicle_id=?", (user['id'], vid))
            conn.execute("UPDATE vehicles SET status='Available' WHERE vehicle_id=?", (vid,))
            conn.commit()
            print("✅ Returned successfully!")
        elif ch == '4':
            conn.close()
            break
        conn.close()


def main():
    init_db()
    while True:
        print("\n=== VEHICLE RENTAL SYSTEM ===\n1. Login\n2. Register\n3. Exit")
        ch = input("Choice: ")
        if ch == '1':
            user = login()
            if user:
                admin_menu() if user['role'] == 'Admin' else customer_menu(user)
        elif ch == '2':
            register()
        elif ch == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()