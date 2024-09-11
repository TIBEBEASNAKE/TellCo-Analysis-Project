import streamlit as st
from pages.task3_task4_dashboard import show_experience_dashboard

def main():
    st.set_page_config(page_title="TellCo Analysis Dashboard", page_icon=":bar_chart:", layout="wide")

    # Title of the dashboard
    st.title("TellCo Analysis Dashboard")
    st.markdown("""
    Welcome to the TellCo Analysis Dashboard. Explore different analyses and insights using the navigation options on the left. 
    Select a page from the sidebar to get started.
    """)
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home",])

    if selection == "Home":
        st.image("https://via.placeholder.com/800x400?text=Welcome+to+TellCo+Analysis", use_column_width=True)
        st.subheader("Overview")
        st.markdown("""
        This dashboard provides insights into user data through various analyses. 
        Use the sidebar to navigate to different sections and explore the data.
        """)


if __name__ == "__main__":
    main()
