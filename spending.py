from parser import parse_user_spending
from calculator import calculate_all_roundings
from printer import prepare_roundings_results


def main_loop():
    while True:
        raw_data = input('Enter your spending: ')

        parsed_data = parse_user_spending(raw_data)
        roundings = calculate_all_roundings(parsed_data)

        print(prepare_roundings_results(parsed_data, roundings))

        choice = input('Continue (y/n): ').lower()
        if choice != 'y':
            break


if __name__ == '__main__':
    main_loop()
