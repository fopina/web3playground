from ape import accounts, project


def main():
    sk = project.sKewlToken.at("0x2cDBD48204929c6AD7b77CEd8d3E61364764E1D9")
    sknft = project.sKewlPoo.at("0x6Dd6802E2189a8D94f6cc1A5180f6c893e0bE13b")

    for acc in accounts:
        print(
            f"""{acc.alias} ({acc.address}):
    - AVAX: {acc.balance / 1000000000000000000}
    - SKEWL: {sk.balanceOf(acc) / 1000000000000000000}
    - SKPOO: {sknft.balanceOf(acc)}"""
        )
