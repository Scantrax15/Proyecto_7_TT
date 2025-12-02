import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Gráficas de anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón
disp_button = st.button('Construir gráfico de dispersión')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="model_year", y="price", color="condition")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Otra versión con casillas de verificación
st.title("Visualización de datos de vehículos")

# Casilla para histograma
show_hist = st.checkbox("Mostrar histograma del odómetro")

# Casilla para scatter plot
show_scatter = st.checkbox(
    "Mostrar diagrama de dispersión (precio vs odómetro)")

# Si la casilla del histograma está activada
if show_hist:
    st.write("Histograma del odómetro:")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist)

# Si la casilla del scatter está activada
if show_scatter:
    st.write("Diagrama de dispersión: precio vs odómetro")
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter)
