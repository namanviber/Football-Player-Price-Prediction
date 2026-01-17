# ⚽ Football Player Price Prediction

An end-to-end Machine Learning project that predicts the market value (price) of football players based on various performance and popularity metrics. The project includes data analysis, model training, and a web interface for real-time predictions.

## 🌟 Overview

The goal of this project is to estimate the transfer value of football players using features such as:
- **Page Views**: Popularity and interest in the player.
- **FPL Value**: Fantasy Premier League valuation.
- **FPL Selection %**: Percentage of users who have selected the player in their FPL team.
- **FPL Points**: Total points earned in the previous/current season.
- **Big Club Status**: Whether the player belongs to a top-tier "Big Club".

## 🛠️ Tech Stack

- **Language**: [Python](https://www.python.org/)
- **Data Analysis**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/)
- **Web Framework**: [Streamlit](https://streamlit.io/)
- **Model Storage**: Pickle

## 📁 Project Structure

```text
Football-Player-Price-Prediction/
├── templates/          # HTML templates for the web interface
├── Dataset.csv         # The primary dataset
├── ML Assignment 1.ipynb # Data preprocessing and EDA
├── ML_Assignment_2.ipynb # Model training and evaluation
├── Predict_price.ipynb  # Price prediction experimentation
├── app.py              # Streamlit web application
├── main.py             # Alternative entry point/logic
├── predictPrice.pkl    # Pre-trained ML model
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/namanviber/Football-Player-Price-Prediction.git
   cd Football-Player-Price-Prediction
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

## 📊 Methodology

1. **Data Preprocessing**: Handling missing values, encoding categorical variables (e.g., Big Club status), and feature scaling.
2. **Exploratory Data Analysis (EDA)**: Visualizing correlations between page views, FPL metrics, and market price.
3. **Model Training**: Implementing regression algorithms using Scikit-Learn to find the best-performing model.
4. **Export**: Saving the trained model using `pickle` for inference.
