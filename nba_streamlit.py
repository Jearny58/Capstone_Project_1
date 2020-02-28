'''
Script that runs a Streamlit data exploration app for NBA statistical data from the past five seasons (not including the current season).
'''
import streamlit as st
import pandas as pd

@st.cache
def load_data():
    '''
    Loads in data from CSV file.
    '''
    return pd.read_csv('Data/df_all.csv')


def main():
    '''
    Main function for the application.
    '''
    st.header("NBA Data Exploration")
    df = load_data()
    st.dataframe(df.head())
    
    
# run main program
main()