import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# webapp ka title
st.markdown('''
# **Exploratory Data Anslysis web application**
This app developed by codanics youtube channel called **EDA app**
  ''')

# how to upload a file from pc

with st.sidebar.header(" Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example csv file](full_grouped.csv)")


# profile report for pandas

if uploaded_file is not None:
    @st.cache

    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for csv file, upload kar b do ab ya kam nhai lena?')
    if st.button('Press to use example data'):
    # example dataset

     def load_data():
        a = pd.DataFrame( np.random.rand(100, 5),
                            columns=['age', 'banana', 'codanic', 'Deutchland', 'Ear'])
        return a
    
    # df = load_data()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**profiling report with pandas**')
    st_profile_report(pr)