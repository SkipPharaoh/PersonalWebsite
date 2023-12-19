---
title: Interactive Dashboard
publishDate: 2020-03-02 00:00:00
img: /assets/stock-1.jpg
img_alt: Iridescent ripples of a bright blue and pink liquid
description: |
  This repository contains a Plotly-Dash Dashboard depicting the major US airline flight performance 2005 to 2020.
tags:
  - Dashboards
  - Statistics
  - Data-Viz
permalink: https://www.kaggle.com/code/sonyalawrence/final-dashboard-assignment-with-ibm
---

# Create an Interactive Dashboard using Dash

## Story:
As a data analyst, you have been given a task to monitor and report US domestic airline flights performance from 2005 to 2020.Your goal is to analyze the performance of the reporting airline to improve flight reliability thereby improving customer reliability.

Below are the key report items:

- Yearly airline performance report 
- Yearly average flight delay statistics

For the chosen year provide,

- Number of flights under different cancellation categories using bar chart.
- Average flight time by reporting airline using line chart.
- Percentage of diverted airport landings per reporting airline using pie chart.
- Number of flights flying from each state using choropleth map.
- Number of flights flying to each state from each reporting airline using treemap chart.
- Yearly average flight delay statistics

For the chosen month provide,

- Monthly average carrier delay by reporting airline for the given year.
- Monthly average weather delay by reporting airline for the given year.
- Monthly average national air system delay by reporting airline for the given year.
- Monthly average security delay by reporting airline for the given year.
- Monthly average late aircraft delay by reporting airline for the given year.
NOTE: You have worked created the same dashboard components in Flight Delay Time Statistics Dashboard section. We will be reusing the same.

## Expected Layout Requirements:
Create the expected result
Two dropdown menus: For choosing report type and year
Each dropdown will be designed as follows:
   - An outer division with two inner divisions
   - One of the inner divisions will have information about the dropdown and the other one is dropdown
   - Layout for adding graphs
   - Callback function to compute data, create graph and return to the layout
    
## Sample Output 1:
![Screenshot (28)](https://user-images.githubusercontent.com/92489108/167524885-46be2044-ed1a-462f-8018-a7d2ec77a001.png)

## Sample Output 2:
![Screenshot (27)](https://user-images.githubusercontent.com/92489108/167524907-f67b3e37-65df-44a8-8d17-893ca5006b5e.png)
