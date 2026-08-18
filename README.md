# Data Redundancy Removal System

## Project Overview

The Data Redundancy Removal System is a Python and Flask-based web application designed to detect, classify, and prevent duplicate data.

The system accepts data through manual entry and CSV file uploads. Each record is checked against existing data and classified as Unique, Redundant, or Possible False Positive.

## Features

- Manual data entry
- CSV file upload
- Duplicate data detection
- Unique record identification
- Possible false-positive detection
- Classification history
- Dashboard statistics
- SQLite database
- User-friendly web interface

## Classification

### 🟢 Unique

A record is classified as Unique when no matching or similar record exists in the database.

### 🔴 Redundant

A record is classified as Redundant when the exact same record already exists in the database.

### 🟡 Possible False Positive

A record is classified as a Possible False Positive when similar information already exists, but some information is different.

## Technologies Used

- Python
- Flask
- SQLite
- Pandas
- HTML
- CSS

## Project Structure

```text
DataRedundancyRemoval/
│
├── app.py
├── database.py
├── database.db
├── sample_data.csv
├── requirements.txt
├── .gitignore
├── README.md
│
└── templates/
    ├── index.html
    └── dashboard.html

## How to Run

### 1. Clone the Repository

```bash
git clone <https://github.com/ciliverigouthami/DataRedundancyRemoval.git>

2. Open the Project Folder
cd DataRedundancyRemoval

3. Install Required Packages
pip install -r requirements.txt

4. Run the Application
python app.py

5. Open the Application
http://127.0.0.1:5000


You **do not type these commands into your README and then execute them**.

---

### 2. Terminal — where commands are actually executed

For example, when we eventually want to download your GitHub project onto another computer, we would open **PowerShell/Terminal** and run:

```powershell
git clone https://github.com/ciliverigouthami/DataRedundancyRemoval.git

