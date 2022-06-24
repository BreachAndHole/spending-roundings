def prepare_roundings_results(spending: list[float], roundings: list[float]) -> str:
    result = ''
    for i, (spend, rounding) in enumerate(zip(spending, roundings), 1):
        result += f'{i}: spending {str(spend).rjust(8)} ₽ - rounding {rounding} ₽\n'
    result += f'Total: {sum(roundings)} ₽'
    return result
