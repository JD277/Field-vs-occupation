import streamlit as st
import pandas as pd
import numpy as ny
import test_model as tm
from streamlit_option_menu import option_menu
from pandas.api.types import( is_categorical_dtype,
    is_numeric_dtype,
    is_object_dtype,)

#Genera un menú ocultable a la izquierda de la página
select_menu = st.sidebar


#Función que filtra los datos del dataset según los parámetros seleccionados
def filter(df = pd.DataFrame):


    filtered = st.checkbox("Filtrar datos")

    if not filtered:
        return df
    
    modified_container = st.container()

    df = df.copy()

    with modified_container:

        #Permite seleccionar el criterio por el cual se quiere filtrar
        columns_filter = st.multiselect("Seleccione los filtros:", df.columns)
        for columns in columns_filter:
            left, right = st.columns((1,21))

            #Permite seleccionar tags para mostrar elementos específicos en las variables cualitativas
            if is_object_dtype(df[columns]):
                categories = right.multiselect(f"Seleccione los datos deseados de {columns}", df[columns].unique(),default= list(df[columns].unique()))
                df = df[df[columns].isin(categories)]

            #Muestra un slider para seleccionar el rango númerico que se desea visualizar dentro
            #dentro de las variables cuantitativas
            elif is_numeric_dtype(df[columns]):
                min_value = int(df[columns].min())
                max_value = int(df[columns].max())

                slider = right.slider(f"Seleccione el rango de valores de {columns}",
                                      min_value, max_value, (min_value,max_value), 1)
                
                df = df[df[columns].between(*slider)]
    
    #Retorna la tabla modificada
    return df

#Menú de selección dentro del menú ocultable 
with select_menu:
    menu = option_menu('Field of Study vs Occupation',
                       ('Introduccion','Objetivos del estudio', 'Datos','Gráficos', 'Conclusiones'), 
                       menu_icon= 'justify', icons= ('body-text','bar-chart-steps', 'braces','book', 'journal-check'))
    logo = st.image('UDO.png')

if menu == 'Introduccion':
    container = st.container()
    st.title('*Análisis Exploratorio de Datos para identificar patrones clave entre los campos de estudio y las ocupaciones laborales*')
    
    header = st.header('Los estudios en relación a la elección de carrera', divider = 'red')
    st.markdown('''<span style='font-size: 24px;'>El estudiar una carrera de cualquier índole puede que 
                haga parecer predecible el area de trabajo de una persona, y si bien es así en
                la mayoría de ocasiones, que termine trabajando en algo ligeramente/completamente
                diferente sucede con suficiente frecuencia como para que se tenga que tomar en
                cuenta esta posibilidad. <br />   
                Teniendo en cuenta esto, surge la duda, ¿Qué produce este cambio entre
                especialidad y area laboral? Esta es una pregunta para la cual no se puede declarar
                un único culpable, puesto a que una serie de factores son los responsables de la
                situación presentada; sin embargo, si es posible tomar estos factores y analizarlos,
                con tal de llegar a una conclusión que satisfaga la incognita planteada. <br />  
                Por medio del uso del dataset **Field of Study vs Occupation** y la aplicación de las estructuras de
                datos adecuadas, se realizará un análisis de datos exploratorio (EDA) de forma que se logre
                contestar la pregunta.</span>''', True)

if menu == 'Objetivos del estudio':
    st.header('Objetivo General', divider = 'red')
    st.markdown('''<span style='font-size: 24px;'>Realizar un análisis exploratorio de datos para identificar patrones clave 
                entre los campos de estudio y las ocupaciones laborales, con el fin de evaluar 
                la eficacia del sistema de selección para estudios superiores y proponer 
                mejoras que permitan de una manera eficiente otorgar oportunidades educativas.</span>''', True)
    
    st.header('Objetivos Específicos', divider= 'red')
    objectives = ['',
                  '''Darle un uso práctico a las estructuras de datos, con tal de observar su utilidad.''',
                  '''Conocer la estructura del dataset **Field of Study vs Occupation**, 
                  identificando sus variables clave y comprendiendo su relevancia para el análisis.''',
                  '''Analizar la distribución de los campos de estudio para identificar 
                  patrones de popularidad y representatividad en la población estudiada.''',
                  '''Relacionar los campos de estudio con las ocupaciones laborales, 
                  evaluando la concordancia entre ambas dimensiones.''',
                  '''Interpretar las diferencias en los ingresos según campo de estudio y ocupación, 
                  destacando posibles disparidades significativas.''',
                  '''Evaluar las tasas de empleabilidad asociadas a diferentes campos de estudio, 
                  identificando áreas con mayor o menor demanda laboral.''',
                  '''Crear visualizaciones que resuman de manera clara y efectiva los hallazgos del EDA, 
                  facilitando su comprensión e interpretación.''',
                  '''Justificar la necesidad de mejorar los sistemas de selección en estudios superiores 
                  a partir de los patrones observados en el análisis.''']
    
    s = ' '

    for text in objectives:
        if text != '':
            s += '\n- ' + text + '\n'
        else:
            s += '\n'

    st.markdown(f'''<span style='font-size: 24px;'>{s}</span>''', True)

if menu == 'Datos':
    st.header('Los datos de :red[Field of Study vs Occupation]', divider= 'red',
               help= 'Si desea buscar algún dato en particular, presione la confirmación de "Filtrar datos"')
    st.markdown('''<span style='font-size: 24px;'>Para poder realizar el estudio optimo de los datos,
                se optó por utilizar las librerías _Streamlit_ y _Pandas_; la primera
                con tal de poder recoger y analizar los datos (además de darles representación a través de gráficas),
                y la segunda con la intención de mostrar el dataset de una forma llamativa y 
                poder utilizar los filtros que se desee. <br />  
                De forma que se puedan usar de manera optima ambas librerías, se optó por almacenar
                los datos a través de listas; esto no solo se debe a la capacidad de esta estructura
                de cambiar de tamaño dinamicamente, sino que también por el uso extenso de estas como
                parametro de multiples de sus funciones, haciendola preferible ante sus competidores.</span>''',True)
    dataset = pd.read_csv('career_change_prediction_dataset.csv')
    st.dataframe(filter(dataset))

if menu == 'Gráficos':
    st.header("Resultados del análisis", divider= 'red')
    st.markdown('''<span style='font-size: 24px;'>Posterior al análisis realizado, se pueden observar las
                gráficas resultantes, a través de las cuales se llegarán a las respectivas conclusiones.</span>''',True)
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

if menu == 'Conclusiones':
    st.header('Respuesta a la incognita',divider= 'red')
    st.markdown('''<span style='font-size: 24px;'>Por medio de la agrupación, análisis y la representación 
                gráfica de los datos propuestos,se han revelado factores clave que influyen en el cambio ocupacional, 
                dentro de estos destacando: <br />  
                - Satisfacción laboral: Muestra una relación directa con la propensión al cambio, 
                siendo los niveles más bajos de satisfacción los que presentan una mayor probabilidad 
                de cambiar de ocupación.<br />  
                - Interés en cambiar de carrera: Siendo autoexplicativa, las personas que desean
                un cambio de especialidad fueron más propensas a realizarlo.<br />  
                - Salario: Uno de los principales motivos por los cuales se elige un trabajo particular,
                las personas con un salario menor al promedio presentaron tendencia a cambiar de carrera,
                funcionando como mayor ejemplo el grupo dentro del menor rango monetario (con una tasa de cambio
                del 100%) <br />  
                Estos hallazgos sugieren que el sistema de selección para estudios superiores podría beneficiarse de un enfoque 
                más integral, que considere estas variables en la orientación vocacional y profesional. <br />  
                Identificar las necesidades individuales y garantizar una mejor alineación entre los campos de estudio, 
                las habilidades requeridas en el mercado laboral y las expectativas personales puede reducir la probabilidad 
                de cambios ocupacionales, optimizando así las oportunidades educativas.</p>''', True)