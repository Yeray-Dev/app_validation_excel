import streamlit as st

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from modules.login import login
from modules.utils.create_users import input_info
from modules.main import main_app
from db.database import SessionLocal
from db.models import User



if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"


if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login()
    elif st.session_state.page == "create_user":
        input_info()
else:
    main_app()

