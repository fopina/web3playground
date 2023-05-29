from ape import accounts


def main():
    for acc in accounts:
        print(f'{acc.alias} ({acc.address}): {acc.balance / 1000000000000000000} avax')
