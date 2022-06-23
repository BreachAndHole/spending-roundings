from boundary import BOUNDARIES, RoundingBoundary


def _calculate_rounding(amount: float, boundary: RoundingBoundary) -> float:
    rounding_amount = round(boundary.ceiling - amount % boundary.ceiling, 2)
    return rounding_amount


def calculate_all_roundings(spending: list[float]) -> list[float]:
    result = []
    for spend in spending:
        for j, boundary in enumerate(BOUNDARIES):
            if boundary.start <= spend < boundary.end:
                amount = _calculate_rounding(spend, boundary)
                result.append(amount)
                break
    return result


def is_float(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False


def parse_user_spending(user_data: str) -> list[float]:
    user_data = user_data.replace(',', '.')
    return [float(item) for item in user_data.split() if is_float(item)]


def form_roundings_result(
    spending: list[float], roundings: list[float]
    ) -> str:
    result = ''
    for i, (spend, rounding) in enumerate(zip(spending, roundings), 1):
        result += f'{i}: spending {str(spend).rjust(8)} ₽ - rounding {rounding} ₽\n'
    result += f'Total: {sum(roundings)} ₽'
    return result


if __name__ == '__main__':
    # raw_data = input('Enter your spending: ')
    raw_data = '1 22 333 4444 55555'
    parsed_data = parse_user_spending(raw_data)
    roundings = calculate_all_roundings(parsed_data)
    print(form_roundings_result(parsed_data, roundings))
