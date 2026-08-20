# CSV Data Cleaning & Merge Pipeline

A small Python project for practicing a structured data-processing workflow with Pandas.

## Features

* Load CSV files
* Handle missing input files
* Clean merge keys
* Clean text columns
* Convert numeric columns safely
* Handle missing values
* Detect duplicate merge keys
* Detect merge relationships:

  * one-to-one
  * one-to-many
  * many-to-one
  * many-to-many
* Prevent unexpected many-to-many merges
* Validate Pandas merges
* Save cleaned and merged datasets
* Organize raw, cleaned, and output data separately

## Project Structure

```text
stage1_csv_merge/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── output/
│
├── src/
│   ├── loading.py
│   ├── cleaning.py
│   └── merging.py
│
├── main.py
├── .gitignore
└── README.md
```

## Requirements

* Python
* Pandas

## Run

Activate the virtual environment and run:

```bash
python main.py
```

## Current Learning Goals

This project is part of my Python and data-processing practice, focusing on writing reusable, modular, and reliable code.
