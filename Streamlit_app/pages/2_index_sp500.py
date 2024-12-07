# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score, mean_squared_error
import tensorflow as tf
from datetime import datetime

# Load Data
def load_data():
    df = pd.read_csv("../financial_regression.csv")
    df.dropna(inplace=True)

    def convert_date(x):
        date = datetime.strptime(x, "%Y-%m-%d")
        return [date.month, date.year]

    df["Year"] = df["date"].apply(lambda x: convert_date(x)[1])
    df["Month"] = df["date"].apply(lambda x: convert_date(x)[0])
    return df

def create_monthly_avg_plots(df, year, nums, months):
    temp_df = df[df["Year"] == year]
    grouped = temp_df.groupby("Month")
    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(16, 5))
    for k, col in enumerate(nums):
        mean = pd.DataFrame(grouped[col].mean()).sort_index(ascending=True)
        data = {"month": [months[i - 1] for i in mean.index], col: mean[col].values}
        dd = pd.DataFrame(data)

        sns.barplot(x="month", y=col, data=dd, ax=axes[k], palette="summer")
        axes[k].set_xticklabels(axes[k].get_xticklabels(), rotation=90)
        axes[k].set_title(col)
        axes[k].set_ylabel("")
        axes[k].set_xlabel("Months")
    
    plt.tight_layout()
    return fig

def create_historical_plot(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    df['date'] = pd.to_datetime(df['date'])
    ax.plot(df['date'], df['sp500 close'], color='green')
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    return fig


# App
st.markdown("<h1 style='text-align: center; color: #9ACD32;'>S&P 500 Stock and Price Dynamics</h1>", unsafe_allow_html=True)

df = load_data()
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
nums = df.columns[1:5].tolist()

# Historical plot of S&P 500 close prices
st.subheader("Historical S&P 500 Close Prices")
fig2 = create_historical_plot(df)
st.pyplot(fig2)

# Year selection
years = sorted(df["Year"].unique())
selected_year = st.selectbox("Select a Year", years)

# Monthly average plots
st.subheader(f"Monthly Average Stock Prices for {selected_year}")
fig1 = create_monthly_avg_plots(df, selected_year, nums, months)
st.pyplot(fig1)

