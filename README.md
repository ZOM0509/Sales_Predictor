# Sales_Predictor

A data analysis project that predicts sales based on advertising spending across different media channels (TV, Radio, and Newspaper).
Overview
This project analyzes the relationship between advertising spending and sales performance using visualization and statistical analysis to help businesses optimize their advertising budget allocation.
Features

Correlation analysis between different advertising channels and sales
Regression analysis with confidence intervals
Statistical summaries of advertising performance
Visual representations of relationships between variables

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
