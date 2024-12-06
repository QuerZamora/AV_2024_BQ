import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load the dataset
@st.cache_data
def load_data():
    file_path = "final_dataset.csv"  # Change this if the file is in a different location
    data = pd.read_csv(file_path)
    return data

# Main function
def main():
    # Load the dataset
    df = load_data()

    # Title and description
    st.markdown("<h1 style='text-align: center; color: #9ACD32;'>Interactive Data Exploration</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 20px; color: #000000;">
    In this part of the website it is displayed an interactive Dataset Analysis. Select the variables desired to be shown and displayed in the differents plots.
    </p>
    """, unsafe_allow_html=True)

    # Dataset information
    st.markdown("<h2 style='color: #6B8E23;'>General Overview</h2>", unsafe_allow_html=True)
    st.write("**Dataset dimensions:**", df.shape)
    st.write("**Preview:**")
    st.dataframe(df.head())

    st.write("**Statistical summary:**")
    st.write(df.describe())

    # Column selection for analysis
    st.markdown("<h2 style='color: #6B8E23;'>Specific Analysis</h2>", unsafe_allow_html=True)
    cols_to_analyze = st.multiselect("Select columns for analysis:", options=df.columns)

    if cols_to_analyze:
        st.write(f"**Analysis of selected columns:** {', '.join(cols_to_analyze)}")
        st.write(df[cols_to_analyze].describe())

        # Distribution visualizations
        st.markdown("<h3 style='color: #9ACD32;'>Histograms of Selected Columns</h3>", unsafe_allow_html=True)
        for col in cols_to_analyze:
            st.write(f"**Histogram for {col}:**")
            plt.figure(figsize=(8, 4))
            sns.histplot(df[col].dropna(), kde=True, color='#9ACD32')
            st.pyplot(plt)

    # Temporal trends
    if "date" in df.columns:
        st.markdown("<h2 style='color: #6B8E23;'>Temporal Trends</h2>", unsafe_allow_html=True)
        time_col = st.selectbox("Select column for temporal trends:", options=cols_to_analyze)
        
        if time_col:
            st.write(f"**Temporal trend of {time_col}:**")
            df['date'] = pd.to_datetime(df['date'])
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df, x="date", y=time_col, color="#228B22")
            plt.xticks(rotation=45)
            st.pyplot(plt)

    # Correlation analysis
    st.markdown("<h2 style='color: #6B8E23;'>Correlation Heatmap</h2>", unsafe_allow_html=True)
    st.write("**Correlation heatmap:**")
    corr = df.select_dtypes(include='number').corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, cmap="YlGn", fmt=".2f")
    st.pyplot(plt)

# Run the main function
if __name__ == "__main__":
    main()
