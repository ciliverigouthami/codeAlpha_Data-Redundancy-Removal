from flask import Flask, render_template, request
from database import (
    create_database,
    add_record,
    classify_record,
    save_classification,
    get_all_records,
    get_record_count,
    get_dashboard_statistics,
    get_classification_statistics,
    get_classification_history
)
import pandas as pd


app = Flask(__name__)


# =========================================================
# CREATE DATABASE
# =========================================================

create_database()


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# ADD SINGLE RECORD
# =========================================================

@app.route("/add", methods=["POST"])
def add():

    name = request.form["name"]
    age = int(request.form["age"])
    city = request.form["city"]
    course = request.form["course"]


    # Classify the record

    classification, message = classify_record(
        name,
        age,
        city,
        course
    )


    # Save classification history

    save_classification(
        name,
        age,
        city,
        course,
        classification
    )


    # -----------------------------------------------------
    # UNIQUE RECORD
    # -----------------------------------------------------

    if classification == "UNIQUE":

        success, add_message = add_record(
            name,
            age,
            city,
            course
        )

        return render_template(
            "index.html",
            classification="UNIQUE",
            message=add_message,
            success=True
        )


    # -----------------------------------------------------
    # REDUNDANT RECORD
    # -----------------------------------------------------

    elif classification == "REDUNDANT":

        return render_template(
            "index.html",
            classification="REDUNDANT",
            message=message,
            success=False
        )


    # -----------------------------------------------------
    # POSSIBLE FALSE POSITIVE
    # -----------------------------------------------------

    else:

        return render_template(
            "index.html",
            classification="FALSE_POSITIVE",
            message=message,
            success=False
        )


# =========================================================
# CSV UPLOAD
# =========================================================

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("file")


    # Check if file was selected

    if file is None or file.filename == "":

        return render_template(
            "index.html",
            message="Please select a CSV file.",
            success=False
        )


    try:

        # Read CSV file

        data = pd.read_csv(file)


        # Check required columns

        required_columns = [
            "name",
            "age",
            "city",
            "course"
        ]


        for column in required_columns:

            if column not in data.columns:

                return render_template(
                    "index.html",
                    message=(
                        f"CSV file is missing the required "
                        f"column: {column}"
                    ),
                    success=False
                )


        # Counters

        unique_count = 0

        duplicate_count = 0

        false_positive_count = 0


        # -------------------------------------------------
        # PROCESS EACH CSV ROW
        # -------------------------------------------------

        for _, row in data.iterrows():

            name = str(row["name"]).strip()

            age = int(row["age"])

            city = str(row["city"]).strip()

            course = str(row["course"]).strip()


            # Classify record

            classification, message = classify_record(
                name,
                age,
                city,
                course
            )


            # Save classification history

            save_classification(
                name,
                age,
                city,
                course,
                classification
            )


            # ---------------------------------------------
            # UNIQUE
            # ---------------------------------------------

            if classification == "UNIQUE":

                add_record(
                    name,
                    age,
                    city,
                    course
                )

                unique_count += 1


            # ---------------------------------------------
            # REDUNDANT
            # ---------------------------------------------

            elif classification == "REDUNDANT":

                duplicate_count += 1


            # ---------------------------------------------
            # FALSE POSITIVE
            # ---------------------------------------------

            elif classification == "FALSE_POSITIVE":

                false_positive_count += 1


        # -------------------------------------------------
        # RESULT MESSAGE
        # -------------------------------------------------

        message = (
            "CSV processed successfully! "
            f"Unique: {unique_count} | "
            f"Redundant: {duplicate_count} | "
            f"Possible False Positive: {false_positive_count}"
        )


        return render_template(
            "index.html",
            message=message,
            success=True
        )


    except ValueError:

        return render_template(
            "index.html",
            message=(
                "Invalid data found in the CSV file. "
                "Please check the age column."
            ),
            success=False
        )


    except Exception as e:

        return render_template(
            "index.html",
            message=f"Error processing CSV: {str(e)}",
            success=False
        )


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    records = get_all_records()

    statistics = get_dashboard_statistics()

    classification_statistics = get_classification_statistics()

    history = get_classification_history()

    return render_template(
        "dashboard.html",
        records=records,
        statistics=statistics,
        classification_statistics=classification_statistics,
        history=history
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)