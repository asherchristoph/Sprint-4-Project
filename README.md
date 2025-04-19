# Sprint-4-Project
This web application is designed to provide an interactive experience for vehicle sales and advertisement data in the US.  This app is a tool to interact with data visualization via a dashboard built with Streamlit, publsihed on Github, and hosted by render.com.  

Initial exploratory data analysis (EDA) was perfromed in a Jupyter Notebook
Interactive Streamlit dashboard with dropdowns, checkboxes, and visualizations was built using Plotly Express

The features below allow in depth analysis of the data:
- View the distribution of car prices with a histogram
- Explore how price relates to time on the market using a scatter plot
- Filter by vehicle type using a dropdown menu
- Toggle to show only 4WD vehicles using a checkbox

The dataset is stored in `vehicles_us.csv` and includes:
- Price, mileage, year, condition, type, transmission, and more
- Filtered to remove extreme outliers (e.g. price > $100,000)

Language and packages used
- Python 3.12
- [Streamlit](https://streamlit.io/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- Pandas
- Jupyter Notebook (for initial EDA)

To run this app locally, follow the steps below:
1. Clone the repository:
   ```bash
   git clone https://github.com/asherchristoph/Sprint-4-Project.git
   cd Sprint-4-Project
2. Install dependencies using Pipenv:
    pipenv install
    pipenv shell
3 Run the Streamlit app:
    streamlit run app.py
4. Open browser to the displayed localhost link.

