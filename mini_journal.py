"""
EJERCICIO: Mini journal de trading en memoria
Temas: listas, diccionarios, bucles, funciones

DATOS
trades = [
    {"asset": "NQ", "result": "win",  "pnl": 500},
    {"asset": "NQ", "result": "loss", "pnl": -250},
    {"asset": "ES", "result": "win",  "pnl": 300},
    {"asset": "NQ", "result": "loss", "pnl": -250},
    {"asset": "ES", "result": "loss", "pnl": -150},
    {"asset": "NQ", "result": "win",  "pnl": 500},
]

CONSIGNA
Calcula y muestra con print:
1. Cantidad total de operaciones, de ganadas y de perdidas.
2. Win rate (porcentaje de operaciones ganadas).
3. PnL total y PnL promedio por operacion.
4. Mejor y peor operacion.
5. Solo las operaciones de "NQ": cuantas son y su PnL total.
6. Un diccionario que cuente las operaciones por activo
   (usando un for y .get()).
7. Agrega con append una operacion nueva
   ({"asset": "NQ", "result": "win", "pnl": 400})
   y vuelve a calcular el PnL total y el win rate.

REGLAS
- Cada calculo debe ser una funcion que reciba la lista de
  operaciones y devuelva el resultado (con return, no con print).
- Antes de programar, escribe en comentarios cada paso con tus palabras.
- Resuelve un punto a la vez y ejecutalo antes de pasar al siguiente.
- Nombres de variables y funciones en un solo idioma (ingles).

RESULTADOS ESPERADOS
- Total: 6 | Ganadas: 3 | Perdidas: 3 | Win rate: 50.0
- PnL total: 650 | PnL promedio: 108.33 (aprox.)
- Mejor: 500 | Peor: -250
- NQ: 4 operaciones, PnL 500
- Conteo por activo: {"NQ": 4, "ES": 2}
- Con la operacion nueva: PnL total 1050, win rate 57.14 (aprox.)
"""

trades = [
    {"asset": "NQ", "result": "win", "pnl": 500},
    {"asset": "NQ", "result": "loss", "pnl": -250},
    {"asset": "ES", "result": "win", "pnl": 300},
    {"asset": "NQ", "result": "loss", "pnl": -250},
    {"asset": "ES", "result": "loss", "pnl": -150},
    {"asset": "NQ", "result": "win", "pnl": 500},
]


def total_operation(trades):
    operations = len(trades)
    wins = 0
    losses = 0
    win_rate = 0
    for trade in trades:
        if trade["result"] == "win":
            wins += 1
        elif trade["result"] == "loss":
            losses += 1
    if operations == 0:
        return operations, wins, losses, win_rate
    win_rate = wins * 100 / operations
    return operations, wins, losses, win_rate


def gets_pnl(trades):
    pnls = []
    for trade in trades:
        pnls.append(trade["pnl"])
    return pnls


def summarize_pnl(trades):
    pnls = gets_pnl(trades)
    operations = len(trades)
    sum_pnls = sum(pnls)
    if operations == 0:
        return 0, 0
    average_pnl = sum_pnls / operations
    return sum_pnls, average_pnl


def best_worst(trades):
    pnls = gets_pnl(trades)
    if not pnls:
        return None, None
    else:
        best = max(pnls)
        worst = min(pnls)
        return best, worst


def summarize_asset(trades, asset):
    pnl_asset = []
    for trade in trades:
        if trade["asset"] == asset:
            pnl_asset.append(trade["pnl"])
    asset_operations = len(pnl_asset)
    sum_asset = sum(pnl_asset)
    return asset_operations, sum_asset


def counter_via_dictionary(trades):
    counter = {}
    for trade in trades:
        asset = trade["asset"]
        counter[asset] = counter.get(asset, 0) + 1
    return counter


def print_report(trades, asset):
    operations, wins, losses, win_rate = total_operation(trades)
    print(
        f"Total: {operations} | Wins: {wins} | Losses: {losses} | Win Rate: {win_rate:.2f}"
    )
    sum_pnls, average_pnl = summarize_pnl(trades)
    print(f"Pnl total: {sum_pnls} | Average pnl = {average_pnl:.2f}")
    best, worst = best_worst(trades)
    print(f"Best trade: {best} | Worst trade: {worst}")
    asset_operations, sum_asset = summarize_asset(trades, asset)
    print(f"{asset}: {asset_operations} operations, pnl: {sum_asset}")
    counter = counter_via_dictionary(trades)
    print(f"Counter for assets: {counter}")


print("-----before-----")
print_report(trades, "NQ")

trades.append({"asset": "NQ", "result": "win", "pnl": 400})

print("-----after-----")
print_report(trades, "NQ")
