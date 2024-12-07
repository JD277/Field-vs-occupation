import streamlit as st
import pandas as pd
import numpy as ny
from streamlit_option_menu import option_menu
'Example Dataframe'


select_menu = st.sidebar

with select_menu:
    menu = option_menu('Menú principal',('Introduccion','Datos','Conclusion'))
array = ny.random.randn(10, 5)
dt = pd.DataFrame(
    array,
    columns= (['column %i' % i for i in range(5)])
    )
option = st.selectbox('Chose your favorite number', dt['column 0'])


dt
