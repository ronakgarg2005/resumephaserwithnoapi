from flask import Flask, render_template, request
import os
from database.sql_lite import create_table, save_resume


from config import *

# Master Resume Parser
from parser.resume_parser import parse_resume

app = Flask(__name__)
create_table()


# Configuration
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

# Create uploads folder if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # Get uploaded file
    file = request.files.get("resume")

    if not file or file.filename == "":
        return "No file selected."

    # Check file extension
    extension = file.filename.rsplit(".", 1)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        return "Only PDF and DOCX files are allowed."

    # Save file
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Parse Resume
    resume_data, resume_text = parse_resume(filepath)

    # Debug Output
    print("\n========== Resume Data ==========\n")

    for key, value in resume_data.items():
        print(f"{key} : {value}")

    print("\n===============================\n")

    # Send data to frontend
    resume_data, resume_text = parse_resume(filepath)

    save_resume(resume_data)

    return render_template(
    "result.html",
      filename=file.filename,
      resume_text=resume_text,
      resume_data=resume_data
)


if __name__ == "__main__":
    app.run(debug=True)