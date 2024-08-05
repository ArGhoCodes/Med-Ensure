# Med-Ensure

Med-Ensure is a web application designed to predict medical insurance costs using linear regression. Leveraging a dataset from Kaggle, this project provides a robust solution for estimating insurance premiums based on various input features.

Overview

Med-Ensure is built to help users predict their medical insurance costs based on several personal attributes such as age, gender, BMI, and smoking status. The application uses a linear regression model to provide accurate predictions, assisting users in understanding potential insurance expenses.

Features

*Insurance Cost Prediction: Input personal attributes to get a prediction of medical insurance costs.

*User-friendly Interface: Intuitive web interface for easy input and result viewing.

*Data Visualization: Interactive charts displaying the relationship between features and insurance costs.

Technology Stack

Frontend : Streamlit

Machine Learning: Scikit-learn (Linear Regression)

Data: Kaggle Medical Insurance Dataset

Installation

To set up Med-Ensure locally, follow these steps:

Clone the repository:

bash

git clone https://github.com/yourusername/med-ensure.git
cd med-ensure

Create a virtual environment:

bash

python -m venv venv

Install the dependencies:

bash

pip install -r requirements.txt

Run the application:

bash

run streamlit app.py

Open http://127.0.0.1:5000 in your browser to access the application.

Usage

Navigate to the Web Application: Open the URL provided after running the application.

Enter Personal Details: Fill in the form with your age, gender, BMI, and smoking status.

Get Prediction: Submit the form to see the predicted insurance cost.

Data

The dataset used in this project is the Medical Insurance Cost Dataset from Kaggle. The dataset includes the following features:

Age

Sex

BMI

Children

Smoker

Region

Charges (Target Variable

Contributing

Contributions to Med-Ensure are welcome! 

To contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Create a new Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.


