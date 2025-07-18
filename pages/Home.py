import streamlit as st
import pandas as pd
import numpy as np


def display_ml_tools():
    """Display tools in the ML Lab"""
    ml_tools = [
        ("Machine Learning Prediction", "Tool For Prediction", model_prediction),
        ("ML Model Training", "Tool For training ML models", model_training),
    ]
    ml_tool_prompts = [
        "Tool to predict feature values",
        "Tool for training models",
    ]

    st.session_state.placeholder.markdown("---")
    button_cols1 = st.session_state.placeholder.columns(3)
    button_cols2 = st.session_state.placeholder.columns(3)

    for i, ((tool_name, suffix, tool), help_text) in enumerate(zip(ml_tools, ml_tool_prompts)):
        col = button_cols1[i] if i < 3 else button_cols2[i - 3]
        if col.button(f"{tool_name} {suffix}", help=help_text):
            st.session_state.cs_tool = tool
            # st.session_state.display_tool = False
            return True
    return False

@st.fragment
def summarize_dataset(data_df):
    profile = ProfileReport(data_df, title="EPL Data Report", explorative=True)
    profile.to_widgets()


def model_prediction():
    pass


def model_training():
    pass


@st.fragment
def home_header():
    placeholder = st.container()
    tool_selected = False
    if "placeholder" not in st.session_state:
        st.session_state.placeholder = placeholder
    else:
        st.session_state.placeholder = st.container()

    st.session_state.display_tool = False
    st.session_state.placeholder.write("In home_header")
    # with st.session_state.placeholder:

    # st.write(f"Repaint home is {st.session_state.repaint_home}\nDisplay tool is {st.session_state.display_tool}")
    home_tab, data_report_tab = st.tabs(['Dataset Highlight', 'Data Report'])
    epl_df = None
    with home_tab:
        if (st.session_state.repaint_home) & (not st.session_state.display_tool):
            st.session_state.placeholder.title(":scales: Machine Learning on Rails")
    
            # st.session_state.repaint_home = False
            if "messages" not in st.session_state:
                st.session_state.messages = []
                # st.session_state.gre
            intro = """👋 Welcome to Machine Learning on Rails. This app aims to take you through model training and prediction using well-known (existing)
                          Machine Learning (ML) algorithms for classification, regression and clustering. You will be able to also load your own custom model to explore.
                          Join as I seek to bring a deeper understanding of ML to many.
                    """
            st.session_state.placeholder.markdown(intro)
            # st.session_state.display_tool = True
            tool_selected = display_ml_tools()
        else:
            st.info('No painting would be done')
    
        # if st.session_state.cs_tool != "":
        #     paint_tool_page()
    
        if tool_selected:
            st.rerun()
    
        st.info("Featuring EPL Data with including current season")
        
        epl_df = pd.read_csv('https://raw.githubusercontent.com/fredericklaud/fl-data/refs/heads/main/England%20CSV.csv')
        with st.expander('EPL Data'):
          st.write(epl_df)

    with data_report_tab:
        if epl_df is not None:
            st.write("report coming soon")
            # summarize_dataset(epl_df)
