
# 🚀 CS 725 - Strokes Uncovered: Machine Learning Exploration and Predictive Insights under the guidance of Professor Sunita Sarawagi. 
![Strokes](https://i.imgur.com/2zNegPi.png)

![Strokes Uncovered](https://img.shields.io/badge/Strokes%20Uncovered-Machine%20Learning%20Exploration%20and%20Predictive%20Insights-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue)
![License](https://img.shields.io/badge/License-MIT-red)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/yourarnav/CS699-SW-Lab)
## Contributors 🧑‍💻

Meet the brilliant minds behind this project:

- **Anuj Attri (23M0808)** 👨‍🎓
- **Arnav Attri (23M0811**) 👨‍🎓
- **Satheeshkumar M (23D0198)** 👨‍🎓
- **Piyush Paliwal (30005245)** 👨‍🎓

## Project Title 📝

***🧠 Strokes Uncovered: Machine Learning Exploration and Predictive Insights for Stroke Prevention*** 🧠

## Abstract 🌐

Stroke, a cerebrovascular disease, is the second leading cause of death worldwide, carrying significant health and economic implications. The project, titled **Strokes Uncovered**, presents an in-depth exploration of machine learning techniques applied to the prediction and prevention of strokes, with a focus on addressing the feedback received from our TA.

We acknowledge the significance of traditional machine learning models in predicting strokes based on structured data from CSV files. However, we recognize the opportunity to advance our research by incorporating deep learning techniques, specifically Convolutional Neural Networks (CNN), which were recently introduced by our professor in the class and we employ that with particular emphasis on analyzing Brain CT scan images.

## Relevance of Our Project 🌍

To further underscore the importance of our project, we reference recent high-profile news articles:

- In a recent article by The Washington Post, published on October 19, 2023, experts predict a potential 50% increase in stroke-related deaths by the year 2050. This alarming projection highlights the urgency of developing effective strategies for stroke prevention. 📈

- The New York Times, in an October 18, 2023 report, shed light on the higher incidence and severity of strokes in women. This emphasizes the need for targeted prevention efforts to address this gender-specific health concern. 🚺

- Additionally, Forbes' recent piece on October 29, 2023, emphasizes the stark reality that, on World Stroke Day, a staggering 33,425 individuals are estimated to suffer from strokes, with only 1,000 of them receiving life-saving treatments. This underscores the critical need for improved stroke prediction and intervention strategies. 💔

## A Tale of Two Datasets 📊

### 4.1 First Dataset - Patient Information

This dataset is publicly available on Kaggle, has more than 5000 tuples and contains the following attributes in a CSV file:

- **ID:** A unique identifier for each patient.
- **Gender:** Categories include "Male," "Female," or "Other."
- **Age:** The patient's age.
- **Hypertension:** A binary indicator where 0 means the patient doesn't have hypertension, and 1 means they have hypertension.
- **Heart Disease:** A binary indicator where 0 indicates the absence of any heart diseases, and 1 indicates the presence of a heart disease.
- **Marital Status:** Two categories, "No" and "Yes," representing whether the patient is married or not.

### 4.2 Second Dataset - Brain Stroke CT Image Dataset

This publicly available dataset on Kaggle contains two classes of images:

1. **Normal Brain Images:** It includes 1551 images representing normal brain scans.

2. **Stroke Images:** This category consists of 950 images depicting brain scans of patients who have suffered a stroke.

## Under the Hood: Model Implementation 🧠

### 5.1 Introduction

Within the framework of our project, the solution approach laid out plays a pivotal role in driving our project forward. In this section, we will dive deep into the details of our carefully crafted solution approach, highlighting how it addresses critical project goals and leads our journey toward stroke prediction and prevention.

### 5.2 Data Collection

In this phase, we meticulously collected and prepared two essential publicly available datasets: patient information and brain CT images. The first dataset comprises comprehensive patient records, while the second dataset contains brain CT scans of patients, categorized into normal and stroke images. This robust foundation equips us for in-depth data analysis and model development.

### 5.3 Exploratory Data Analysis (EDA)

In this section, we conduct exploratory data analysis (EDA) to gain insights into various aspects of our dataset. We utilize Plotly Express (px) and Seaborn to create a range of visualizations that provide us with valuable insights into our dataset, enhancing our understanding of key factors related to stroke prediction.

### 5.4 Data Preprocessing

In the data preprocessing phase, we undertake several critical tasks to enhance the quality and suitability of our datasets for model training. These tasks include:

- **Null Handling:** We address missing data using imputation strategies to ensure our machine learning models perform optimally.
- **Outliers Handling:** To mitigate the impact of outliers, we employ outlier detection and removal techniques in the BMI column to improve the model's resilience to anomalies.
- **Duplicate Checking:** Rigorous duplicate checking is performed to maintain data integrity, ensuring that each data point is unique and contributes meaningfully to model training, as duplicates in the dataset can skew the analysis.
- **Category Data Encoding:** We transform categorical attributes into numerical formats suitable for machine learning by employing encoding techniques such as one-hot encoding or label encoding.

These preprocessing steps are integral in refining our datasets, facilitating subsequent stages of feature engineering and model training. They are vital for achieving reliable and accurate stroke predictions.

### 6 Model Selection

For brain stroke prediction, we selected a diverse ensemble of ML models, including traditional models:

- **Logistic Regression:** A fundamental model for binary classification.
- **K-Nearest Neighbors (KNN):** Effective for proximity-based predictions.
- **Decision Tree:** Useful for hierarchical data structure interpretation.

Additionally, we incorporated advanced models for their ensemble capabilities and performance:

- **Random Forest:** A powerful ensemble method for improving accuracy.
- **XGBoost:** Known for its gradient boosting techniques.
- **Stacking Model:** Combining multiple models for enhanced predictions.

To leverage the potential of medical imaging data, we included a specialized deep learning model:

- **Convolutional Neural Network (CNN) with TensorFlow:** Renowned for image analysis.

## Semester Roadmap: A Technical Journey Towards Excellence 🗺️

After successfully navigating through the complex terrain of Exploratory Data Analysis (EDA), we're now embarking on an exciting journey to address the significant challenges in the field of stroke prediction and prevention. In the coming weeks, we'll focus on the following important technical milestones:

1. **Data Preprocessing:** We'll meticulously refine and optimize our dataset, ensuring that it's well-prepared for the subsequent modeling phase.

2. **Balancing Data Visualization:** Using advanced data sampling techniques, we aim to create a balanced dataset, guaranteeing fairness and accuracy in our analysis.

3. **Modeling and Evaluation:** This is the high point of our expedition, where we'll carefully build and fine-tune our machine learning models to predict strokes with exceptional precision.

4. **Model Deployment - Building a Web Application:** The grand finale of our technical journey will be the creation of an interactive web application. This application will allow users to directly experience the outcomes of our hard work and research.

**Files in this GitHub Repository**
- `Mid Report.ipynb`: Jupyter Notebook containing the project code. 👨🏼‍💻
- `environment.yml`: Environment file for recreating the project's Python environment.
- `README.md`: You're reading it right now! 😉
- `requirements.txt`: Python package requirements. 🌐
- `stroke.csv`: The dataset used for analysis. 🗄️
- `Setup steps.txt`: Detailed terminal steps for running the project.
- `CS_725_Mid_Term.pdf`: Additional information about the project's roadmap.🚗

## Setup 🛠️

Follow these steps in your terminal to set up the environment:

1. **Navigate to the Project Folder:**
   - Open your terminal and use the `cd` command to go to the folder where you cloned or downloaded this repository.

2. **Activate the Conda Environment:**
   - Activate the Conda environment using the following command:
     ```bash
     conda activate lightgbm-env
     ```
3. **Launch Jupyter Notebook:**
   - Start Jupyter Notebook by running:
     ```bash
     jupyter notebook
     ```
4. **Deactivate Conda Environment:**
   - Once you're done working with the Jupyter (ipynb) notebook, deactivate the Conda environment using:
     ```bash
     conda deactivate
     ```
This **setup** will get you ready to work on your project with the required environment. Enjoy your data exploration and analysis!

Feel free to explore, contribute, and uncover the secrets of strokes with us! 🕵️‍♀️🔍
---

**License**: This project is licensed under the [MIT License](LICENSE).
