import streamlit as st
from sqlalchemy.orm import sessionmaker
import sqlite3
import os

# Get database path from environment (or use default)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///accounts.db")

# Extract actual file path from SQLAlchemy format
db_path = DATABASE_URL.replace("sqlite:///", "")

def get_db_connection():
    """Establish a direct SQLite connection"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Enables column name access
    return conn

# Test if DB connection works
try:
    conn = get_db_connection()
    print("✅ Database connected successfully!")
    conn.close()
except Exception as e:
    print("❌ Database connection failed:", str(e))
from models import YouTubeAccount

def main():
    st.title("YouTube Automation Control Panel")

    # Add new account section
    st.subheader("Add New Account")
    region = st.selectbox("Region", ["India", "US", "UK", "Other"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Add Account"):
        if email and password:
            db = SessionLocal()
            new_acc = YouTubeAccount(region=region, email=email, password=password)
            db.add(new_acc)
            db.commit()
            db.close()
            st.success(f"Account {email} added!")
    
    # Show stats
    st.subheader("Account Stats")
    db = SessionLocal()
    total = db.query(YouTubeAccount).count()
    active = db.query(YouTubeAccount).filter_by(is_active=True).count()
    st.write(f"Total Accounts: {total}, Active: {active}")
    db.close()

    st.write("---")
    st.write("**Note**: For scheduling uploads, run `main.py` or use Celery Beat.")
    
if __name__ == "__main__":
    main()
