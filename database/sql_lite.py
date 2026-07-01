import sqlite3
import json

DATABASE = "resume.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        email TEXT,
        phone TEXT,
        linkedin TEXT,
        github TEXT,
        portfolio TEXT,

        skills TEXT,
        education TEXT,
        experience TEXT,
        projects TEXT,
        certifications TEXT,
        languages TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_resume(resume_data):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO resumes (

        name,
        email,
        phone,
        linkedin,
        github,
        portfolio,
        skills,
        education,
        experience,
        projects,
        certifications,
        languages

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        resume_data.get("name"),
        resume_data.get("email"),
        resume_data.get("phone"),
        resume_data.get("linkedin"),
        resume_data.get("github"),
        resume_data.get("portfolio"),

        json.dumps(resume_data.get("skills", [])),
        json.dumps(resume_data.get("education", [])),
        json.dumps(resume_data.get("experience", [])),
        json.dumps(resume_data.get("projects", [])),
        json.dumps(resume_data.get("certifications", [])),
        json.dumps(resume_data.get("languages", []))

    ))

    conn.commit()
    conn.close()


def get_all_resumes():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM resumes")

    data = cursor.fetchall()

    conn.close()

    return data