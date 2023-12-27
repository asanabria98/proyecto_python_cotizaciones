import streamlit as st
import krakenex
from pykrakenapi import KrakenAPI
from src.functions.load_data import load_data
from src.functions.get_estocastistico import get_estocastico
from src.functions.crear_grafico_cotizaciones import crear_grafico_cotizaciones
from src.functions.data_cleaning import data_cleaning
import datetime

# Conectarse al API
api = krakenex.API()
k = KrakenAPI(api)

# Titulo del app
st.write("DivisaDirecta: Proyecto Final Python para análisis de datos")

# Create a select box for Pair Options

# Definir opciones de pares
pair_options = ["ETHUSDT" ,"ETHUSD", "BTCUSD", "ETHEUR", "BTCEUR"]
pair =  st.sidebar.selectbox(label = "Selecione la cotizacion de un par de monedas", options= pair_options, key = "select_pair")

# Opciones de ventanas para los estocasticos
ventana_oscilador_estocastico_k = st.sidebar.number_input(label = "Ventana del Oscilador Estocastico K",
                                                          min_value = 10, max_value = 14, value="min")
ventana_oscilador_estocastico_sk = st.sidebar.number_input(label = "Ventana del Oscilador Estocastico SK",
                                                           min_value = 3, max_value = 5, value="min")
ventana_oscilador_estocastico_sd = st.sidebar.number_input(label = "Ventana del Oscilador Estocastico SD",
                                                           min_value = 3, max_value = 5, value="min")

# Cargar data
data = load_data(pair = pair, interval = 1440)

# Definir Intervalo de fecha
date = st.sidebar.date_input(
    "Seleccione un intervalo de fecha",
    value = [datetime.datetime.now() - datetime.timedelta(days = 30), datetime.datetime.now()],
    min_value = min(data["dtime"]),
    max_value =  datetime.datetime.now()
)


data = data_cleaning(data, date_list = date)

# Calcular Estocasticos
data = get_estocastico(data = data, ventana_estocastico = ventana_oscilador_estocastico_k,
                       ventana_estocastico_sk = ventana_oscilador_estocastico_sk,
                       ventana_estocastico_sd = ventana_oscilador_estocastico_sd)

# Crear Graficos
fig = crear_grafico_cotizaciones(ohlc = data)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)