---
title: Machine Learning Basketball
publishDate: 2022-05-01 00:00:00
img: /assets/stock-1.jpg
img_alt: A group of basketball players attempting to score
description: |
  This is the final assignment for the IBM Data Science Professional Certificate Machine Learning Module.
tags:
  - Machine Learning
  - Decision Tree
  - Classification
permalink: https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/98cc15ea-9aae-4589-8167-41d10ca95476/view?access_token=5f45ee82c2f6db1ea945e79bfd935e51e3c9eb0cff038bf204c07aef2c361a6c
---

## ML & Sports Betting
This is the final assignment for the IBM Data Science Professional Certificate Machine Learning Module

### Objective
Apply ML to a dataset to make inferences about a basketball team's likelihood of making it to the final four

### Instructions
In this scenario, you are a Data Scientist working for a college basketball team. Your coaches have asked you to look at historical data to see which team metrics (individually or combined) make a team more likely to make it into the Final Four. 

For example:
  - If a team is more efficient defensively does this have a direct relationship to their ability to get into the Final Four? 
  - How does defensive efficiency contribute to overall wins? 

Something to keep in mind is that when trying to predict results of basketball tournaments there are many variables that need to be taken into account. As a result, creating accurate models is incredibly hard. In the sports betting industry an accuracy rate of anything over 55% is considered good as it indicates profits. Your job is to figure out if there is a combination of metrics that give a team more of a chance of making it into this tournament.

You will load a historical data set from previous seasons, clean the data, and apply different classification algorithms to the data. You are expected to use the following algorithms to build your models:

- k-Nearest Neighbour
- Decision Tree
- Support Vector Machine
- Logistic Regression

The results are reported as the accuracy of each classifier, using the following metrics when applicable:
- Jaccard index
- F1-score
- Accuracy
- Log Loss

### Review Criteria
The project is considered successful if the following requirements are met:
  * Build a KNN model using a value of k equals five, find the accuracy on the validation data 
  * Determine the accuracy for the first 15 values of k the on the validation data:.
  * Determine the minimum value for the parameter that improves results on validation data.
  * Building model using Support Vector Machine. 
  * Train a logistic regression model and determine the accuracy of the validation data (set C=0.01) 
  * Calculate the F1 score and Jaccard Similarity score for each model from above.
  * Use the Hyperparameter that performed best on the validation data
  
### Accuracy Scores Observed in Model
![image](https://user-images.githubusercontent.com/92489108/179370179-8b973fd9-9c98-4948-9e68-664aa65eb260.png)  
