# MobileDeviceBehavior

## Overview
This project aims to analyze mobile device usage patterns and classify user behavior based on various metrics. It utilizes machine learning algorithms to predict user behavior classes ranging from light to extreme usage.

## Dataset
The dataset contains 700 samples of user data, including metrics such as:

- User ID: Unique identifier for each user
- Device Model: Model of the user's smartphone
- Operating System: The OS of the device (iOS or Android)
- App Usage Time: Daily time spent on mobile applications (in minutes)
- Screen On Time: Average hours per day the screen is active
- Battery Drain: Daily battery consumption (in mAh)
- Number of Apps Installed: Total apps available on the device
- Data Usage: Daily mobile data consumption (in megabytes)
- Age: Age of the user
- Gender: Gender of the user (Male or Female)
- User Behavior Class: Classification of user behavior (1 to 5)

## Features
- Data preprocessing and encoding of categorical variables.
- Utilization of Random Forest Classifier for predicting user behavior.
- Evaluation of model accuracy.
- Saving the trained model as a pickle file for future use.

## Requirements
- Python 3.x
- Pandas
- Scikit-learn
- Pickle

## Installation
You can install the required libraries using pip:

```bash
pip install pandas scikit-learn
