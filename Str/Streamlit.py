import streamlit as st
import pandas as pd
import numpy as ny
from streamlit_option_menu import option_menu
'Example Dataframe'

select_menu = st.sidebar

with select_menu:
    menu = option_menu('Field vs Occupation',('Introduccion','Datos','Conclusion'), menu_icon= 'justify', icons= ('body-text','braces','book'))

if menu == 'Conclusion':
    option = st.selectbox('Seleccione el gráfico a visualizar', 
                          ['Campo de estudio', 'Ocupación', 'Edades', 'Genero', 'Años de experiencia',
                           'Nivel de educación','Tasa de crecimiento profesional', 'Satisfacción laboral',
                           'Balance vida personal/laboral','Oportunidades laborales',])

    if option == 'Campo de estudio':
        st.image("./Graphs/Campo_de_estudio.png")

    elif option == 'Ocupación':
        st.image("./Graphs/Ocupaciones.png")

    elif option == 'Edades':
        st.image("./Graphs/Edades.png")

    elif option == 'Genero':
        st.image("./Graphs/Genero.png")
    
    elif option == 'Años de experiencia':
        st.image("./Graphs/Años_de_experiencia.png")

    elif option == 'Nivel de educación':
        st.image("./Graphs/Nivel_de_educación.png")

    elif option == 'Satisfacción laboral':
        st.image("./Graphs/Satisfacción_laboral.png")

    elif option == 'Tasa de crecimiento profesional':
        st.image("./Graphs/Tasa_de_crecimiento_profesiones.png")

    elif option == 'Balance vida personal/laboral':
        st.image("./Graphs/Balance.png")

    elif option == 'Edades':
        st.image("./Graphs/Edades.png")

    elif option == 'Genero':
        st.image("./Graphs/Genero.png")
    
    elif option == 'Años de experiencia':
        st.image("./Graphs/Años_de_experiencia.png")

    elif option == 'Nivel de educación':
        st.image("./Graphs/Nivel_de_educación.png")
        
    elif option == 'Satisfacción laboral':
        st.image("./Graphs/Satisfacción_laboral.png")

    elif option == 'Tasa de crecimiento profesional':
        st.image("./Graphs/Tasa_de_crecimiento_profesiones.png")
    
    elif option == 'Ocupación':
        st.image("./Graphs/Ocupaciones.png")

    elif option == 'Edades':
        st.image("./Graphs/Edades.png")

    elif option == 'Genero':
        st.image("./Graphs/Genero.png")
    
    elif option == 'Años de experiencia':
        st.image("./Graphs/Años_de_experiencia.png")

    elif option == 'Nivel de educación':
        st.image("./Graphs/Nivel_de_educación.png")
        
    elif option == 'Satisfacción laboral':
        st.image("./Graphs/Satisfacción_laboral.png")

    

    
    
   