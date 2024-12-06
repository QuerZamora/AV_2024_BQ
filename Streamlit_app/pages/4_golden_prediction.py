import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to load the data from the .pkl file
def load_data():
    return pd.read_pickle('gold_prices_until_2030.pkl')

# Function to predict the gold price for a specific date
def predict_for_date(input_date, combined_data):
    try:
        # Check if the date exists in the index
        if input_date in combined_data.index:
            return combined_data.loc[input_date, 'Gold']
        else:
            return "Date not found in the data."
    except Exception as e:
        return f"Error predicting the price: {e}"

# Function to plot the full historical data
def plot_full_historical_data(combined_data):
    # Separate historical data until today
    historical_data = combined_data[combined_data.index <= pd.to_datetime("today")]
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot each year with a different color
    years = historical_data.index.year.unique()
    colors = plt.cm.get_cmap('YlGn', len(years))  # Use yellow-green palette for each year
    
    for i, year in enumerate(years):
        year_data = historical_data[historical_data.index.year == year]
        plt.plot(year_data.index, year_data['Gold'], color=colors(i))
    
    # Mark today with a vertical line
    plt.axvline(pd.to_datetime("today"), color='black', linestyle='--')
    
    # Remove titles, labels, legends, and grid to make it minimalist
    plt.xlabel("")
    plt.ylabel("")
    plt.legend().set_visible(False)
    plt.grid(False)
    
    st.pyplot(plt)

# Function to plot the last 5 years of data and future predictions
def plot_recent_and_predicted_prices(combined_data, input_date):
    # Define the start of prediction and today's date
    today = pd.to_datetime("today")
    five_years_ago = today - pd.DateOffset(years=5)
    
    # Separate the historical data (last 5 years) from combined_data
    historical_data = combined_data[(combined_data.index >= five_years_ago) & (combined_data.index < today)]
    
    # Extract predicted data for the period from today to input_date
    predicted_data = combined_data[(combined_data.index >= today) & (combined_data.index <= input_date)]
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot historical data (last 5 years) in olive green
    plt.plot(historical_data.index, historical_data['Gold'], color='#6B8E23')
    
    # Plot predicted data (future) in light yellow-green
    plt.plot(predicted_data.index, predicted_data['Gold'], color='#9ACD32')
    
    # Add a vertical line to indicate today
    plt.axvline(today, color='black', linestyle='--')
    
    # Remove titles, labels, legends, and grid to make it minimalist
    plt.xlabel("")
    plt.ylabel("")
    plt.legend().set_visible(False)
    plt.grid(False)
    
    # Display the plot
    st.pyplot(plt)

# Main function of the application
def main():
    # Set up the page title and layout
    st.set_page_config(page_title="Gold Price Prediction", layout="wide")

    # Apply the custom styles for the title and subtitles
    st.markdown(
    """
    <style>
    
    /* Center the button */
    .stButton>button {
        display: block;
        margin-left: auto;
        margin-right: auto;
        background-color: #9ACD32;  /* Light yellow-green button */
        color: black;  /* Black text */
        font-size: 24px;  /* Larger button text */
        font-weight: bold;
        padding: 20px 60px;  /* Bigger button */
        border-radius: 8px;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:hover {
        background-color: #6B8E23;  /* Olive green on hover */
    }

    /* Styling for the date input field */
    .stDateInput>label {
        font-size: 24px;  /* Larger label text */
        font-weight: bold;
        color: black;
    }

    .stDateInput>div>input {
        font-size: 22px;  /* Larger input text */
        padding: 12px;  /* Larger input field */
        border-radius: 8px;
        border: 2px solid #9ACD32;  /* Light yellow-green border */
    }
    </style>
    """, unsafe_allow_html=True
    )

    # Page title
    st.markdown("<h1 style='text-align: center; color: #9ACD32;'>Gold Price Prediction</h1>", unsafe_allow_html=True)
 
    # Load the data
    combined_data = load_data()
    
    # Ensure the index is datetime type
    combined_data.index = pd.to_datetime(combined_data.index)

    st.markdown("<h2 style='text-align: center; color: #6B8E23;'>Full Historical Gold Prices by Year</h2>", unsafe_allow_html=True)
    
    plot_full_historical_data(combined_data)
    
    # User input for date
    input_date = st.date_input("Select a date for the prediction:")
    
    if st.button("Predict Gold Price"):
        if input_date:
            input_date_str = input_date.strftime('%Y-%m-%d')
            predicted_price = predict_for_date(input_date_str, combined_data)
            
            # Display the prediction with larger font
            st.markdown(f"<h2 style='text-align: center; color: #6B8E23;'>Predicted Gold Price on {input_date_str}</h2>", unsafe_allow_html=True)

            st.markdown(f"<h1 style='text-align: center; color: #000000;'>{predicted_price}</h1>", unsafe_allow_html=True)
            
            plot_recent_and_predicted_prices(combined_data, input_date_str)
        else:
            st.write("Please select a date.")


# Run the main function
if __name__ == "__main__":
    main()
