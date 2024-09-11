import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import sys
import os

def show_experience_dashboard():
    st.title('User Experience Analysis')

    # Add the 'scripts' directory to the Python path
    sys.path.append(os.path.abspath(os.path.join('..', 'scripts')))
    from load_data import load_data

    # Define your SQL query
    query = "SELECT * FROM public.xdr_data"  # Replace with your actual table name

    # Load data into a DataFrame
    data = load_data(query)

    # Relevant columns for clustering
    features = [
        'Avg RTT DL (ms)',
        'Avg Bearer TP DL (kbps)',
        'TCP DL Retrans. Vol (Bytes)'
    ]

    # Aggregate data by user
    user_data = data.groupby('MSISDN/Number').agg({
        'Avg RTT DL (ms)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'TCP DL Retrans. Vol (Bytes)': 'mean'
    }).reset_index()

    # Check for NaNs
    st.write("NaN values before imputation:")
    st.write(user_data.isnull().sum())

    # Define the preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
            ]), features)
        ]
    )

    # Apply the preprocessing pipeline
    X_preprocessed = preprocessor.fit_transform(user_data)

    # K-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    user_data['Cluster'] = kmeans.fit_predict(X_preprocessed)

    # Check for NaNs after imputation
    st.write("NaN values after imputation:")
    st.write(user_data.isnull().sum())

    # Display scatter plot
    st.subheader('Experience Clusters')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='Avg RTT DL (ms)', y='Avg Bearer TP DL (kbps)', hue='Cluster', data=user_data, ax=ax, palette="viridis")
    ax.set_title("User Experience Clusters")
    st.pyplot(fig)

if __name__ == "__main__":
    show_experience_dashboard()
