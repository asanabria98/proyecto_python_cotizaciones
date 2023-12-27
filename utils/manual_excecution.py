from src.functions.load_data import load_data
from src.functions.get_estocastistico import get_estocastico
from src.functions.crear_grafico_cotizaciones import crear_grafico_cotizaciones
from src.functions.data_cleaning import data_cleaning
import datetime


# "ETHUSDT" ,"ETHUSD", "BTCUSD", "ETHEUR", "BTCEUR"
# Escoger un par de la lista de arriba
data = load_data(pair = "ETHUSDT", interval = 1440)


date = [datetime.datetime.now() - datetime.timedelta(days = 30), datetime.datetime.now()]

# Clean data
data = data_cleaning(data, date_list = date)


# Calcular Estocasticos
data = get_estocastico(data = data, ventana_estocastico = 10,
                       ventana_estocastico_sk = 3,
                       ventana_estocastico_sd = 3)


# Crear Graficos
fig = crear_grafico_cotizaciones(ohlc = data)

fig.show()
