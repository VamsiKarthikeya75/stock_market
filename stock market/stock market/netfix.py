import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Check if the model file exists
model_file_path = 'C:/Users/manda durgavenkatesh/Downloads/stock market/stock market/data.sav'
if not os.path.exists(model_file_path):
    st.error("Model file not found. Please check the file path.")
    st.stop()

# Load the saved model
with open(model_file_path, 'rb') as f:
    Companystockprice_model = pickle.load(f)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Company stock price prediction using ML',
                           ['Home'],
                           default_index=0)

# Company stock price prediction Page
if selected == 'Home':
    # Page title
    st.title('Company stock price prediction using ML')

    # Getting the input data from the user
    Close = st.text_input('Close')
    Name = st.selectbox('Name', ['GOOGL', 'MSFT', 'AMZN'])

    # Code for Prediction
    companystock_price = ''

    # Creating a button for Prediction
    if st.button('Company stock price Result'):
        # Preprocess the input data
        input_df = pd.DataFrame({'Close': [Close], 'Name': [Name]})
        
        # Use the DataFrame to make predictions
        Companystockprice_prediction = Companystockprice_model.predict(input_df)
        # Convert the prediction to integer format
        Companystockprice_prediction_int = int(Companystockprice_prediction[0])
        st.success('The predicted amount is {}'.format(Companystockprice_prediction_int))

elif selected == 'About':
    st.text("Let's Learn")
    st.text("Built with Streamlit")
