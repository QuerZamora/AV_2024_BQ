import streamlit as st
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    data_path = "final_dataset.csv"
    return pd.read_csv(data_path, sep=";")

def create_wordcloud(columns):
    text = " ".join(columns)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    return wordcloud

def main():
    st.set_page_config(page_title="Goldytics App", layout="wide")

    st.markdown(
        """
        <style>
        body {
            background-color: #F0FFF0; /* Light yellow-green background */
            font-family: 'Arial', sans-serif;
        }
        h1 {
            text-align: center;
            color: #9ACD32; /* Yellow-green */
            font-size: 120px;
            font-weight: bold;
        }
        h2 {
            text-align: center;
            color: #6B8E23; /* Olive green */
            font-size: 40px;
            font-weight: bold;
        }
        .post-it {
            background-color: #E6F9A4; /* Light green */
            padding: 20px;
            border-radius: 8px;
            margin: 20px;
            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2);
            font-size: 20px;
            cursor: pointer;
            width: 300px; /* Adjust the width of the post-its */
            height: 250px;
            text-align: center;
        }
        .post-it:hover {
            background-color: #E6F9A4;
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.3);
        }
        .large-font {
            font-size: 28px;
            font-weight: bold;
        }
        .icon {
            font-size: 40px;
            margin-right: 10px;
            color: #6B8E23; /* Olive green */
        }
        .container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap; /* Allows items to wrap in case of overflow */
            gap: 20px; /* Adds space between items */
            margin-top: 30px;
        }
        .section-box {
            background-color: #9ACD32; /* Yellow-green */
            padding: 20px;
            border-radius: 12px;
            width: 280px;
            box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .section-box h3 {
            font-size: 24px;
            color: #6B8E23; /* Olive green */
            margin-bottom: 10px;
        }

        </style>
        """, unsafe_allow_html=True
    )

    # Title and header
    st.markdown('<h1>GOLDYTICS</h1>', unsafe_allow_html=True)
    st.markdown("<h2>Gold and Indexes Price Analysis & Prediction</h2>", unsafe_allow_html=True)

    # Welcome message
    st.markdown('<p class="large-font">Welcome to your go-to platform for analyzing and predicting gold and stock index prices</p>', unsafe_allow_html=True)

    # Data loading
    data = load_data()

    # Section boxes for navigation and post-its for Dash 1, Dash 2
    st.markdown(
        """
        <div class="container">
            <div class="post-it">
                <h3>💰 Gold prices and trends</h3>
                <p>Explore the data and analysis of Dash 1 here. Dive deeper into the datasets and their implications.</p>
                <a href="/gold_prices_and_economic_trends" style="text-decoration: none; color: #6B8E23;">Explore Now</a>
            </div>
            <div class="post-it">
                <h3>💸 Dash 2</h3>
                <p>Discover the analysis and insights provided by Dash 2. Explore further visualizations and results.</p>
                <a href="/dash2" style="text-decoration: none; color: #6B8E23;">Explore Now</a>
            </div>
            <div class="post-it">
                <h3>📊 Data Exploration</h3>
                <p>Analyze historical gold and stock index prices through interactive visualizations.</p>
                <a href="/dataset_exploration" style="text-decoration: none; color: #6B8E23;">Explore Now</a>
            </div>
            <div class="post-it">
                <h3>📈 Price Prediction</h3>
                <p>Predict the future gold price trends up to 2030 using machine learning algorithms.</p>
                <a href="/golden_prediction" style="text-decoration: none; color: #6B8E23;">Explore Now</a>
            </div>
            <div class="post-it">
                <h3>🧑‍💻 References</h3>
                <p>View all the references used in this project for further reading and research.</p>
                <a href="/references" style="text-decoration: none; color: #6B8E23;">Explore Now</a>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
