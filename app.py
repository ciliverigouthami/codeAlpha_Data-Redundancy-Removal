from flask import Flask, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    # Check whether a file was uploaded
    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]

    # Check whether the user selected a file
    if file.filename == "":
        return "No file selected"

    # Read the CSV file
    df = pd.read_csv(file)

    # Count rows before removing duplicates
    before = len(df)

    # Remove duplicate rows
    df_cleaned = df.drop_duplicates()

    # Count rows after removing duplicates
    after = len(df_cleaned)

    # Calculate number of duplicates removed
    duplicates_removed = before - after

    # Create output folder if it doesn't exist
    output_folder = "output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save cleaned CSV file
    output_file = os.path.join(output_folder, "cleaned_data.csv")

    df_cleaned.to_csv(output_file, index=False)

    # Display result
    return f"""
    <h1>Data Cleaning Completed!</h1>

    <p>Original rows: {before}</p>
    <p>Rows after cleaning: {after}</p>
    <p>Duplicates removed: {duplicates_removed}</p>

    <br>

    <a href="/download">
        <button>Download Cleaned File</button>
    </a>

    <br><br>

    <a href="/">Go Back</a>
    """


@app.route("/download")
def download_file():

    output_file = "output/cleaned_data.csv"

    return send_file(
        output_file,
        as_attachment=True,
        download_name="cleaned_data.csv"
    )


if __name__ == "__main__":
    app.run(debug=True)