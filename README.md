# Exploratory Data Analysis: Trends and Insights in Streaming Services

## Table of Contents
- [Project Description](#project-description)
- [Research Questions](#research-questions)
- [Datasets](#datasets)
- [Strategy & Metrics](#strategy-metrics)
- [Data Cleaning](#data-cleaning)
- [Data Manipulation](#data-manipulation)
- [Data Visualization](#data-visualization)
- [Dependencies](#dependencies)
- [Installation & Setup](#installation-setup)
- [How to Run](#how-to-run)
- [Contributors](#contributors)

## Project Description
This project aims to perform an in-depth Exploratory Data Analysis (EDA) on the competition between streaming giants Netflix and Disney+ as they vie for subscribers and market share. With Disney+ recently surpassing Netflix in total streaming customers, we will investigate the strategies employed by both platforms to attract more subscribers.

## Research Questions
1. How many shows are Netflix and Disney+ releasing per month, and how does this impact the show ratings and number of users?
2. Are Netflix and Disney+ focusing more on TV shows or movies?
3. What content is available on Netflix and Disney+ in different countries?
4. What is the distribution of release years for the content on both platforms?
5. Which countries are the movies and shows originating from?

## Datasets
- Main Netflix Kaggle dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows
- Main Disney+ Kaggle dataset: https://www.kaggle.com/code/jonspags/disney-and-netflix-an-exploratory-data-analysis

## Strategy & Metrics
1. Create separate branches for Netflix and Disney+ analysis.
2. Evaluate the following metrics:
   - Company reports (vision, objectives, strategies)
   - Subscription fees
   - Demographics of subscribers
   - Ad spend on Google and Facebook ads
   - Geographical differences
   - Change in market share over time

## Data Cleaning
- Filter 'Data Added' column to November 2019 - November 2021 (2 years), to match the data range of the smallest dataset (Disney).
- Remove null values.

## Data Manipulation
- Perform necessary transformations for the analysis.

## Data Visualization
Create graphs to analyze data by:
- Content type
- Top 10 countries of origin
- Release year by content type
- Year added by content type
- Month added by content type
- Ratings
- Duration
  - Seasons (TV shows)
  - Length (movies): bins = [0,15,30,60,75,90,300], labels = ['<15mins', '15-30mins','30-60mins', '60-75 mins', '75-90 mins','90mins+']
- Top 10 directors
- Top 10 actors

## Dependencies
This project requires the following libraries:
- pandas
- matplotlib
- numpy

## Installation & Setup
1. Ensure you have Python installed (preferably Python 3.7 or higher).
2. Install the required libraries using pip:
pip install pandas matplotlib numpy python
3. Clone or download the project repository.

## How to Run
To run the project, open the Jupyter Notebook in your preferred Jupyter environment and run the cells in sequence.

## Contributors
Robert Franklin (GitHub: Frankr22) and Trang Nguyen (GitHub: trangnguyenpp)
