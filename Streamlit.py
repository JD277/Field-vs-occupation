import streamlit as st
import pandas as pd
import numpy as ny
from streamlit_option_menu import option_menu


select_menu = st.sidebar


with select_menu:
    menu = option_menu('Field vs Occupation',('Introduccion','Datos','Conclusion'), menu_icon= 'justify', icons= ('body-text','braces','book'))
    logo = st.image('UDO.png')

if menu == 'Introduccion':
    header = st.header('Los estudios en la elección de carrera', divider = 'red')
    st.markdown('''El estudiar una carrera de cualquier índole puede que 
                haga parecer predecible el area de trabajo de una persona, y si bien es así en
                la mayoría de ocasiones, que termine trabajando en algo ligeramente/completamente
                diferente sucede con suficiente frecuencia como para que se tenga que tomar en
                cuenta esta posibilidad.   
                Teniendo en cuenta esto, surge la duda, ¿Qué produce este cambio entre
                especialidad y area laboral? Esta es una pregunta para la cual no se puede declarar
                un único culpable, puesto a que una serie de factores son los responsables de la
                situación presentada; sin embargo, si es posible tomar estos factores y analizarlos,
                con tal de llegar a una conclusión que satisfaga la incognita planteada.
                Por medio del uso del dataset "Field vs Occupation" y la aplicación de las estructuras de
                datos adecuadas, el presente ánalisis de datos pretende llegar a una conclusión
                satisfactoria''')


if menu == 'Datos':
    'Los datos usados para el estudio son los siguientes:'
    dataset = pd.read_csv('career_change_prediction_dataset.csv')
    st.write(dataset)

if menu == 'Conclusion':
    option = st.selectbox('Seleccione el gráfico a visualizar', 
                          ['Campo de estudio', 'Ocupación', 'Edades', 'Genero', 'Años de experiencia',
                           'Nivel de educación','Tasa de crecimiento profesional', 'Satisfacción laboral',
                           'Balance vida personal/laboral','Oportunidades laborales', 'Salario', 'Seguridad laboral',
                           'Brecha de habilidades','Influencia familiar','Mentoria', 'Certificaciones',
                           'Experiencia de freelancing','Movilidad geografica','Red profesional',
                           'Eventos de cambio de carrera', 'Adopcion de la tecnologia'])

    match option:
        case 'Campo de estudio':
            st.image("./Graphs/Campo_de_estudio.png")

        case 'Ocupación':
            st.image("./Graphs/Ocupaciones.png")

        case 'Edades':
            st.image("./Graphs/Edades.png")

        case 'Genero':
            st.image("./Graphs/Genero.png")
        
        case 'Años de experiencia':
            st.image("./Graphs/Años_de_experiencia.png")

        case 'Nivel de educación':
            st.image("./Graphs/Nivel_de_educación.png")

        case 'Satisfacción laboral':
            st.image("./Graphs/Satisfacción_laboral.png")

        case 'Tasa de crecimiento profesional':
            st.image("./Graphs/Tasa_de_crecimiento_profesiones.png")

        case 'Balance vida personal/laboral':
            st.image("./Graphs/Balance.png")

        case 'Oportunidades laborales':
            st.image("Graphs/Oportunidades_laborales.png")

        case 'Salario':
            st.image("Graphs/Salario.png")
        
        case 'Seguridad laboral':
            st.image("Graphs/Seguridad_laboral.png")

        case 'Brecha de habilidades':
            st.image("Graphs/Brecha_de_habilidades.png")
            
        case 'Influencia familiar':
            st.image("Graphs/Influencia_familiar.png")

        case 'Mentoria':
            st.image("Graphs/Mentoria.png")
        
        case 'Certificaciones':
            st.image("Graphs/Certificaciones.png")

        case 'Experiencia de freelancing':
            st.image("Graphs/Experiencia_de_freelancing.png")

        case 'Movilidad geografica':
            st.image("Graphs/Movilidad_geografica.png")
        
        case 'Red profesional':
            st.image("Graphs/Redes_profesionales.png")

        case 'Eventos de cambio de carrera':
            st.image("Graphs/Eventos_de_cambio_de_carrera.png")
            
        case 'Adopcion de la tecnologia':
            st.image("Graphs/Adopcion_de_la_tecnologia.png")

    

    
    
   