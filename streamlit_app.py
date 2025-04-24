import streamlit as st
import pandas as pd
from modules import home_header

st.set_page_config(
    page_title="Machine Learning Lab",
    page_icon="i",
    layout="wide",
    menu_items={
        "about": "**A machine learning app to explore various Ml-algorithms on diverse data.**",
    },
)

# setting up session states
def setup_session_states():
    # session state keys
    if "my_sidebar" not in st.session_state:
        st.session_state["my_sidebar"] = st.sidebar

    # if "authenticator" not in st.session_state:
    #     st.session_state["authenticator"] = auth

    if "signed_in" not in st.session_state:
        st.session_state["signed_in"] = False

    if "refresh" not in st.session_state:
        st.session_state["refresh"] = False

    if "display_tool" not in st.session_state:
        st.session_state["display_tool"] = True
        
    if "rerun_home" not in st.session_state:
        st.session_state["rerun_home"] = False
        
    if "has_rerun_home" not in st.session_state:
        st.session_state["has_rerun_home"] = False
        
    if "repaint_home" not in st.session_state:
        st.session_state["repaint_home"] = True


def main():
    setup_session_states()

    ml_sidebar = st.session_state["my_sidebar"]
    with ml_sidebar:
        st.write('**Welocme to ML-Rails**')

    home_header()
    # st.title('🖥Machine Learning on Rails')


if __name__ == "__main__":
    main()
