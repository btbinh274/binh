import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the seaborn dataset
mpg_df = sns.load_dataset("mpg")

# Display the first few rows of the dataframe
st.write(mpg_df.head())

# Create a scatterplot using Seaborn
fig, ax = plt.subplots()
sns.scatterplot(x="weight", y="mpg", data=mpg_df, ax=ax)

# Display the plot in Streamlit
st.pyplot(fig)
