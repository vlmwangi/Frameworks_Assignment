# Frameworks_Assignment
# CORD-19 (metadata.csv) Data Exploration Project

This project is a simple Python and Streamlit application for exploring the CORD-19 dataset (COVID-19 research papers).  
It demonstrates **basic data analysis** and **interactive visualization**.

---

## Project Structure

- **`analysis.py`**  
  This file contains the **data cleaning and analysis code**.  
  It loads the dataset, performs some preprocessing, and creates visualizations (using Matplotlib/Seaborn).  
  You can run it directly in the terminal to generate static plots.

- **`app.py`**  
  This is the **Streamlit web application**.  
  It provides an interactive interface where you can explore the dataset using sliders, dropdowns, and plots.  
  You run this with Streamlit to launch a local web app in your browser.


---

## Requirements
Install dependencies before running the project:
bash
pip install pandas matplotlib seaborn streamlit

---

# Running the Analysis Script
To generate static visualizations:
bash
python analysis.py

# Running the Streamlit App
To launch the interactive web app:

bash
streamlit run app.py

This will open a local web server (usually http://localhost:8501) where you can interact with the app.

# Features
View basic dataset information and sample rows.
Filter papers by year range.
Filter papers by journal.

# Interactive plots:
Distribution of papers by year.
Top 10 journals by number of papers.
