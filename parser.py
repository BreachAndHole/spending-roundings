def _is_float(text: str) -> bool:
    """ Check if argument is convertible to float"""
    try:
        float(text)
        return True
    except ValueError:
        return False


def parse_user_spending(user_data: str) -> list[float]:
    """
    Extract only ints and floats (dot and coma separated)
    from user input
    """
    user_data = user_data.replace(',', '.')
    split_data = user_data.split()
    return [round(float(item), 2) for item in split_data if _is_float(item)]
