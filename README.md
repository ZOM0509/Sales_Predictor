# Sales_Predictor

A data analysis project that predicts sales based on advertising spending across different media channels (TV, Radio, and Newspaper).
Overview
This project analyzes the relationship between advertising spending and sales performance using visualization and statistical analysis to help businesses optimize their advertising budget allocation.
Features

Correlation analysis between different advertising channels and sales
Regression analysis with confidence intervals
Statistical summaries of advertising performance
Visual representations of relationships between variables

Prerequisites

Python 3.8 or higher
Required Python packages (see requirements.txt)

Installation

Clone the repository

bashCopygit clone https://github.com/yourusername/sales-predictor.git
cd sales-predictor

Create a virtual environment (recommended)

bashCopy# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

Install required packages

bashCopypip install -r requirements.txt

Download the dataset


Download the 'Advertising.csv' file from the repository
Place it in the project root directory

Usage
Run the main script:
bashCopypython sales_predictor.py
The script will generate:

A correlation heatmap showing relationships between all variables
Regression plots for each advertising channel
Statistical summaries in the console

Data Format
The Advertising.csv file should contain the following columns:

TV: TV advertising spending
Radio: Radio advertising spending
Newspaper: Newspaper advertising spending
Sales: Sales amount

File Structure
Copysales-predictor/
│
├── sales_predictor.py    # Main analysis script
├── Advertising.csv       # Dataset
├── requirements.txt      # Package dependencies
└── README.md            # This file
