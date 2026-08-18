import sqlite3

DATABASE = "database.db"


# =========================================================
# CREATE DATABASE AND TABLES
# =========================================================

def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # Main records table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL,
            course TEXT NOT NULL,
            UNIQUE(name, age, city, course)
        )
    """)

    # Classification history table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classification_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL,
            course TEXT NOT NULL,
            classification TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


# =========================================================
# CLASSIFY NEW DATA
# =========================================================

def classify_record(name, age, city, course):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # -----------------------------------------------------
    # CHECK FOR EXACT DUPLICATE
    # -----------------------------------------------------

    cursor.execute("""
        SELECT *
        FROM records
        WHERE LOWER(name) = LOWER(?)
        AND age = ?
        AND LOWER(city) = LOWER(?)
        AND LOWER(course) = LOWER(?)
    """, (name, age, city, course))

    exact_match = cursor.fetchone()

    if exact_match:

        connection.close()

        return (
            "REDUNDANT",
            "This record already exists in the database."
        )

    # -----------------------------------------------------
    # CHECK FOR SIMILAR RECORD
    # -----------------------------------------------------

    cursor.execute("""
        SELECT *
        FROM records
        WHERE LOWER(name) = LOWER(?)
        OR (age = ? AND LOWER(city) = LOWER(?))
    """, (name, age, city))

    similar_match = cursor.fetchone()

    connection.close()

    if similar_match:

        return (
            "FALSE_POSITIVE",
            "A similar record exists, but some information is different."
        )

    # -----------------------------------------------------
    # NO MATCH FOUND
    # -----------------------------------------------------

    return (
        "UNIQUE",
        "No matching record found. This is a unique record."
    )


# =========================================================
# ADD RECORD TO DATABASE
# =========================================================

def add_record(name, age, city, course):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO records
            (name, age, city, course)
            VALUES (?, ?, ?, ?)
        """, (name, age, city, course))

        connection.commit()

        connection.close()

        return (
            True,
            "Unique record added successfully."
        )

    except sqlite3.IntegrityError:

        connection.close()

        return (
            False,
            "Redundant record detected. This record already exists."
        )


# =========================================================
# GET ALL STORED RECORDS
# =========================================================

def get_all_records():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            city,
            course
        FROM records
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records


# =========================================================
# GET NUMBER OF STORED RECORDS
# =========================================================

def get_record_count():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM records
    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count


# =========================================================
# GET BASIC DASHBOARD STATISTICS
# =========================================================

def get_dashboard_statistics():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM records
    """)

    total_records = cursor.fetchone()[0]

    connection.close()

    return {
        "total_records": total_records
    }


# =========================================================
# SAVE CLASSIFICATION HISTORY
# =========================================================

def save_classification(
    name,
    age,
    city,
    course,
    classification
):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO classification_history
        (
            name,
            age,
            city,
            course,
            classification
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        age,
        city,
        course,
        classification
    ))

    connection.commit()

    connection.close()


# =========================================================
# GET CLASSIFICATION STATISTICS
# =========================================================

def get_classification_statistics():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # -----------------------------------------------------
    # TOTAL CHECKED
    # -----------------------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM classification_history
    """)

    total_checked = cursor.fetchone()[0]

    # -----------------------------------------------------
    # UNIQUE COUNT
    # -----------------------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM classification_history
        WHERE classification = 'UNIQUE'
    """)

    unique_count = cursor.fetchone()[0]

    # -----------------------------------------------------
    # REDUNDANT COUNT
    # -----------------------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM classification_history
        WHERE classification = 'REDUNDANT'
    """)

    redundant_count = cursor.fetchone()[0]

    # -----------------------------------------------------
    # FALSE POSITIVE COUNT
    # -----------------------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM classification_history
        WHERE classification = 'FALSE_POSITIVE'
    """)

    false_positive_count = cursor.fetchone()[0]

    connection.close()

    # Return all statistics
    return {
        "total_checked": total_checked,
        "unique": unique_count,
        "redundant": redundant_count,
        "false_positive": false_positive_count
    }

# =========================================================
# GET CLASSIFICATION HISTORY
# =========================================================

def get_classification_history():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            city,
            course,
            classification
        FROM classification_history
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history