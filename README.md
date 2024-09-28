import streamlit as st
import pandas as pd
import seaborn as sns
# load a seaborn dataset
mpg_df = sns.load_dataset("mpg")
mpg_df.head()
# seaborn (‘version 0.9.0 is required’)
ax = sns.scatterplot(x="weight", y="mpg", data=mpg_df)

