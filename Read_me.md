# Cosmetic Data Rating Overview Rating Generator using SQLite + Python

This project provides an interactive tool for generating ratings of cosmetic products based on their ingredients toxicities published on Pubchem. Users can enter any cosmetic products, and the system will generate:

- A structured cosmetic ingredients overview
- Ingredietns explanations
- Toxicology summaries
- Rating of the product

## 🛠 Tech Stack

- Python 3.90+
- SQLite
- Data published on Kaggle

## Usage

- clone the repository
- run locally python3 -m streamlit run streamlit_app.py
- Converting the cosmetic data file as I desired with SQLite (e.g., Cosmetic Product, Rating, Cosmetic Ingredients)
- Click Generate Overview

## Data Source

The source data for the cosmetic product list was obtained from a public dataset.The original file ('Cosmetic Ingredients.db') is too large for GitHub's file limits.
You can access or download the orignal data source file here :
[Cosmetics datasets] (<https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets>)

## Setup and Usage

To run this project locally, please download the database file from the source link above and place it in the following directory structure:

`Think-Dirty/data/Cosmetic Ingredients.db`

Once the file is in place, you can run the Python scripts in the `scripts/` folder.
