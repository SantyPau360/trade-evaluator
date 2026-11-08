"""
Calculadora riesgo
Qué tienes que calcular y mostrar con print:
Riesgo en dinero: el capital multiplicado por el porcentaje de riesgo, dividido 100. (* y /)
Distancia al stop y al objetivo: la resta entre los precios. (-)
Ratio beneficio/riesgo: distancia al objetivo dividida por distancia al stop. (/)
Cantidad de contratos: riesgo en dinero dividido por la distancia al stop, sin decimales, y cuánto sobra. (// y %)
Comparaciones: ¿el ratio es mayor o igual a 2? ¿el riesgo es menor o igual a 2%? (>=, <=)
Operación válida: que se cumplan las dos condiciones anteriores y además que el stop no sea igual a la entrada. (and, not, !=)
Activo permitido: comprobar que activo esté en la lista ["NQ", "ES"]. (in)
Simular una racha: restar tres veces el riesgo en dinero al capital, y luego sumar una ganancia. (-= y +=)
Crecimiento compuesto: capital multiplicado por 1.02 elevado a la 10. (**)
Mensaje final: que diga "Operar" si la operación es válida y "No operar" si no, en una sola línea. (ternario: x if condicion else y)
"""

def evaluate_trade(capital, pct_risk, entry, sl, tp, asset):
    monetary_risk = capital * pct_risk / 100
    print(f"Monetary risk: {monetary_risk}")

    distance_stop = abs(entry - sl)
    print(f"Distance between the entry and the SL: {distance_stop}")
    distance_tp = abs(tp - entry)
    print(f"Distance between the entry and the TP: {distance_tp}")

    if sl > entry < tp:
        print("SL and TP are both above the Entry")
        return "No Trade"
    elif sl < entry > tp:
        print("TP and SL are below the Entry point")
        return "No Trade"
    elif distance_stop == 0:
        print("SL is the same as the Entry")
        return "No Trade"
    else:
        ratio = distance_tp / distance_stop
        print(f"Risk/Reward ratio: {ratio}")

        contracts = monetary_risk // distance_stop
        contracts_left = monetary_risk % distance_stop
        print(f"Number of Contracts: {contracts} and {contracts_left} are left over")

        comparison_1 = ratio >= 2
        comparison_1_str = "Yes" if comparison_1 else "No"
        print(f"The ratio is greater than or equal to 2: {comparison_1_str}")
        comparison_2 = pct_risk <= 2
        comparison_2_str = "Yes" if comparison_2 else "No"
        print(f"The risk is less than or equal to 2% of the capital: {comparison_2_str}")
        asset_valid = asset in ["ES", "NQ"]
        print(f"The asset is: {asset}")
        trade_valid = (comparison_1 and comparison_2) and asset_valid
        trade_valid_str = "Yes" if trade_valid else "No"

        print(f"Is the Trade valid? : {trade_valid_str}")
        capital -= monetary_risk*3
        print(f"Your current capital is: {capital}")
        capital += monetary_risk * ratio
        print(f"Your current capital is: {capital}")
        compound_growth = capital*(1.02**10) - capital
        print(f"Your capital has generated compound interest of {compound_growth}")
        final_message = "Trade" if trade_valid else "No Trade"
        return final_message

cases = [(50000, 1, 18000, 17950, 18100, "NQ", "Trade"),
         (50000, 1, 18000, 18500, 17000, "NQ", "Trade"),
         (50000, 1, 18000, 18050, 18100, "NQ", "No Trade"),
         (50000, 1, 18000, 18000, 18100, "NQ", "No Trade"),
         (50000, 1, 18000, 17950, 18050, "NQ", "No Trade"),  
         (50000, 3, 18000, 17950, 18100, "NQ", "No Trade"), 
         (50000, 1, 18000, 17950, 18100, "XX", "No Trade")]  

number = 0

for capital, riesgo_pct, entry, sl, tp, assets, expected in cases:
    result = evaluate_trade(capital, riesgo_pct, entry, sl, tp, assets)
    number += 1
    if result == expected:
        print(result)
        print(f"Case {number} of {len(cases)}")
        print("-----------------------------")
    else:
        print(result)
        print(f"Fail in the case: {number}")
        print("-----------------------------")
