import streamlit as st

def main():
    st.set_page_config(page_title="References", layout="wide")

    # Title and explanation
    st.markdown("<h1 style='text-align: center; color: #9ACD32;'>References</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #6B8E23;'>Sources and Data Used in Goldytics</h2>", unsafe_allow_html=True)

    # Explanation about the dataset and sources
    st.markdown(
        """
        <p style="font-size: 20px; color: #000000;">
        The <strong>Goldytics</strong> project makes use of various data sources and references for the analysis and prediction of gold and stock index prices.
        Below you will find key references used in the project:
        </p>
        """, unsafe_allow_html=True
    )

    # Section for post-its with references stacked one under the other
    st.markdown(
        """
        <div class="container" style="display: block; margin-top: 20px;">
            <div class="post-it" style="background-color: #E6F9A4; padding: 20px; border-radius: 8px; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2); width: 100%; margin-bottom: 20px;">
                <h3 style="color: #9ACD32;">📊 Financial Data from Kaggle</h3>
                <p style="font-size: 18px; color: #6B8E23; text-align: left;">
                The financial data used in this project is sourced from Kaggle. The dataset contains historical financial data, including gold prices and stock index movements, which is essential for both data exploration and prediction tasks.
                </p>
                <p style="font-size: 18px; color: #6B8E23; text-align: left;">
                You can access the dataset here: <a href="https://www.kaggle.com/datasets/franciscogcc/financial-data/data" target="_blank" style="color: #FF6347; font-weight: bold;">Kaggle Financial Data</a>
                </p>
            </div>
            <div class="post-it" style="background-color: #E6F9A4; padding: 20px; border-radius: 8px; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2); width: 100%; margin-bottom: 20px;">
                <h3 style="color: #9ACD32;">📚 Tableau Online Profile</h3>
                <p style="font-size: 18px; color: #6B8E23; text-align: left;">
                In the following link it can be found the Tableau Profile where the workbook and the dashboards are published.
                </p>
                <p style="font-size: 18px; color: #6B8E23; text-align: left;">
                Access the reference here: <a href="https://public.tableau.com/app/profile/queralt.zamora/vizzes" target="_blank" style="color: #FF6347; font-weight: bold;">Tableau Profile</a>
                </p>
            </div>
            <div class="post-it" style="background-color: #E6F9A4; padding: 20px; border-radius: 8px; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2); width: 100%; margin-bottom: 20px;">
                <h3 style="color: #9ACD32;">📊 S&P 500 Analysis Notebook</h3>
                <p style="font-size: 18px; color: #6B8E23; text-align: left;">
                A really interesting S&P 500 notebook analysis was used for one of the pages of this web. It can be found in the following link!
                </p>
                <p style="font-size: 18px; color: #6B8E23; text-align: left;">
                Access the reference here: <a href="https://www.kaggle.com/code/a3amat02/gold-s-p-dynamics-breakdown-and-forecasting" target="_blank" style="color: #FF6347; font-weight: bold;">S%P500 Notebook</a>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

