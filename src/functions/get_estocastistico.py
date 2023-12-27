def get_estocastico(data, ventana_estocastico, ventana_estocastico_sk, ventana_estocastico_sd):

    # sort values
    data = data.sort_values(by=['dtime'], ascending=True)

    # Calcular valor mas bajo
    lowest_value = data["low"].rolling(window = ventana_estocastico).min()

    # Calcular el valor mas alto
    highest_value = data["high"].rolling(window = ventana_estocastico).max()

    # Calcular Estocatico K
    data["estocastico_k"] = ((data["close"] - lowest_value) / (highest_value - lowest_value)) * 100

    # Calcular Estocastico SK
    data["estocastico_sk"] = data["estocastico_k"].rolling(ventana_estocastico_sk).mean()

    # Calcular Estocastico SD
    data["estocastico_sd"] = data["estocastico_sk"].rolling(ventana_estocastico_sd).mean()

    return data