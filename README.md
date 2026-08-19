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

## How the System Works

1. User enters data manually or uploads a CSV file.
2. The system checks the new record against existing records.
3. Each record is classified as:
   - Unique
   - Redundant
   - Possible False Positive
4. Unique records are stored in the database.
5. Duplicate records are identified as redundant.
6. The dashboard displays classification statistics and history.
7. Users can download the cleaned CSV file.

## Project Output

The dashboard displays:

- Total records checked
- Number of unique records
- Number of redundant records
- Number of possible false positives
- Classification history
- Stored unique records
- Cleaned CSV output

## Testing

The system was tested using sample CSV files containing:

- Unique records
- Duplicate records
- Similar records with minor differences

The application successfully classified the records into Unique, Redundant, and Possible False Positive categories.

## Internship Task

This project was developed as part of the CodeAlpha Cloud Computing Internship.

### Task 1: Data Redundancy Removal System

The objective of this task is to identify and classify data as unique, redundant, or possible false positive and prevent duplicate data from being added to the database.

## Author

**Ciliveri Gouthami**

B.Tech – Artificial Intelligence and Machine Learning