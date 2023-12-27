import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def crear_grafico_cotizaciones(ohlc):

    fig = make_subplots(rows=3, cols=1, shared_xaxes=False, subplot_titles=['OHLC', 'Estocastico', 'Volumen'])

    # Agregar grafico OHLC
    fig.add_trace(go.Candlestick(x = np.array(ohlc['dtime']),
                         open = ohlc['open'],
                         high = ohlc['high'],
                         low = ohlc['low'],
                         close = ohlc['close'],
                         name= "OHLC",
                         showlegend = True),
                  row = 1, col = 1)

    fig.update(layout_xaxis_rangeslider_visible=False)


    # Agregar grafico estocasticos
    fig.add_trace(go.Scatter(x=np.array(ohlc['dtime']), y = ohlc['estocastico_k'],
                             mode='lines',
                             name='Estocastico K'),
                  row=2, col=1)

    fig.add_trace(go.Scatter(x = np.array(ohlc['dtime']), y = ohlc['estocastico_sk'],
                             mode='lines',
                             name='Estocastico SK'),
                  row=2, col=1)

    fig.add_trace(go.Scatter(x = np.array(ohlc['dtime']), y = ohlc['estocastico_sd'],
                             mode = 'lines',
                             name = 'Estocastico SD'),
                  row=2, col=1)

    fig.add_shape(type="line",
                  x0=np.min(ohlc['dtime']),
                  x1=np.max(ohlc['dtime']),
                  y0=20,
                  y1=20,
                  line=dict(color="red", dash="dash"),
                  row=2, col=1)

    fig.add_shape(type="line",
                  x0=np.min(ohlc['dtime']),
                  x1=np.max(ohlc['dtime']),
                  y0=80,
                  y1=80,
                  line=dict(color="red", dash="dash"),
                  row=2, col=1)

    # Agregar grafica de volumen
    fig.add_trace(go.Scatter(x=np.array(ohlc['dtime']), y = ohlc['volume'],
                             mode='lines',
                             name='Volumen'),
                  row=3, col=1)

    # Modificar layout
    fig.update_layout(height=800, width=1500, title_text = "Grafico OHLC con Osciladores Estocasticos")

    # Modificar Axes
    fig.update_yaxes(title_text = "Precio", row=1, col=1)
    fig.update_yaxes(title_text="Indicador Estocastico", row=2, col=1)
    fig.update_yaxes(range=[0, 100], row=2, col=1)
    fig.update_yaxes(title_text="Volumen", row=3, col=1)
    fig.update_xaxes(title_text="Fecha", row=3, col=1)

    return fig

