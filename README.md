# Fake News Classification Using Random Forest Classifier

## Project Description

This project is designed to classify news articles as either **fake** or **real** using a **Random Forest Classifier**. The model is deployed as an interactive but simple web application built with **Streamlit** and packaged in a **Docker** container for easy deployment. The goal of this project is to showcase how machine learning models can be effectively deployed in real-time environments to assist in detecting fake news.

The project leverages text classification techniques, including data preprocessing, feature extraction, and training a Random Forest model to predict whether a given news article is likely to be real or fake.

### Key Features:
- **Random Forest Classifier**: The core machine learning model used for classifying news articles.
- **Streamlit Interface**: An easy-to-use, interactive user interface for testing and using the model.
- **Dockerized Deployment**: The application is containerized using Docker for seamless deployment across different environments.
- **Accuracy**: The model achieves **90%+ accuracy** on the testing data without any hyperparameter tuning.

## Installation

To get started with this project, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/nak5hatra/fake_news_streamlit.git
cd fake_news_streamlit
```

### 2. Setup the project
to install dependencies and setup the project RUN:
``` bash
python setup.py
```
### 3. run the streamlit app
``` bash
streamlit run app.py
```
This will start the Streamlit app, and you can access it in your web browser at http://localhost:8501.

## Optional Docker setup.

### 1. Build Docker Image
Ensure that you have Docker installed on your machine. Once Docker is installed, build the Docker image:

``` bash
docker build -t fake-news-streamlit .
```

### 2. Run the Application in Docker
After the image is built, run the container:
``` bash
docker run -p 8501:8501 fake-news-streamlit
```
This will start the Streamlit app, and you can access it in your web browser at http://localhost:8501.

## Usage
Once the application is up and running, follow these steps to classify news articles:

- Open the Streamlit application in your web browser (http://localhost:8501).
- Enter the news article headline text into the input field provided.
- The model will display the result.

## Technologies Used
- Python: The primary language used for data preprocessing, machine learning, and application logic.
- Streamlit: A Python library for creating interactive web applications.
- Random Forest Classifier: An ensemble learning method used for classification.
- Docker: A platform for developing, shipping, and running applications in containers.
- scikit-learn: Python library for machine learning and data mining.
- pandas: Data manipulation and analysis library.
- nltk: Natural Language Toolkit for text processing.
