import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data_path = "../final_dataset.csv"  

def load_data():
    """Load dataset from a CSV file."""
    df = pd.read_csv(data_path)
    return df

def plot_historical_closing_prices(df):
    """Plot historical closing prices for all metals."""
    plt.figure(figsize=(12, 6))
    colors = ['#9ACD32', '#6B8E23', '#ADFF2F', '#556B2F']  # Yellow-green palette
    plt.plot(df['date'], df['silver close'], label='Silver', color=colors[0], alpha=0.7)
    plt.plot(df['date'], df['platinum close'], label='Platinum', color=colors[1], alpha=0.7)
    plt.plot(df['date'], df['palladium close'], label='Palladium', color=colors[2], alpha=0.7)
    plt.plot(df['date'], df['gold close'], label='Gold', color=colors[3], alpha=0.7)
    plt.ylabel("Price", color='#6B8E23')
    plt.legend()
    st.pyplot(plt)

def filter_data_by_metal_and_year(df, metal, year):
    """Filter dataset based on selected metal and year."""
    filtered_df = df[df['year'] == year]
    metal_close_column = f"{metal.lower()} close"
    return filtered_df[['date', metal_close_column]]

def plot_filtered_data(df, metal, year):
    """Plot closing prices for the selected metal and year."""
    filtered_df = df[df['year'] == year]  # Filter data for the selected year
    metal_close_column = f"{metal.lower()} close"
    
    plt.figure(figsize=(12, 6))
    plt.plot(filtered_df['date'], filtered_df[metal_close_column], label=f'{metal} Close', color='#9ACD32', alpha=0.7)
    plt.title(f"{metal} Closing in {year}", color='#6B8E23')
    plt.ylabel("Price", color='#6B8E23')
    st.pyplot(plt)

def main():
    st.set_page_config(page_title="Metals Analysis", layout="wide")

    # custom styles
    st.markdown(
        """
        <style>
        h1, h2 {
            color: #6B8E23;
            text-align: center;
        }
        .stButton>button {
            background-color: #9ACD32; /* Light yellow-green button */
            color: black; /* Black text */
            font-size: 18px;
            padding: 10px 30px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #6B8E23; /* Olive green on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center; color: #9ACD32;'>Metals Analysis</h1>", unsafe_allow_html=True)

    df = load_data()
    df['date'] = pd.to_datetime(df['date'])  

    st.subheader("Historical Prices of Metals")
    plot_historical_closing_prices(df)

    st.subheader("Filter Data by Metal and Year")
    metals = ['Silver', 'Platinum', 'Palladium', 'Gold']
    years = sorted(df['year'].unique())

    selected_metal = st.selectbox("Select Metal", metals)
    selected_year = st.selectbox("Select Year", years)

    filtered_data = filter_data_by_metal_and_year(df, selected_metal, selected_year)

    st.write(f"Filtered Data for {selected_metal} in {selected_year}:")
    plot_filtered_data(df, selected_metal, selected_year)

if __name__ == "__main__":
    main()