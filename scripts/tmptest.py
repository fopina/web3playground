from ape import accounts, project, exceptions


def main():
    # hacky "test" because of lack of funds in "ape test" accounts
    contract = project.BulkTransfer.deployments[-1]
    sk = project.sKewlToken.at("0x2cDBD48204929c6AD7b77CEd8d3E61364764E1D9")
    sknft = project.sKewlPoo.at("0x6Dd6802E2189a8D94f6cc1A5180f6c893e0bE13b")

    print(f"Using deployment {contract}")

    a1 = accounts.load("acc1")
    a2 = accounts.load("acc2")
    a3 = accounts.load("acc3")

    def bcheck():
        print("== Balance check")
        print(f"a1: {sk.balanceOf(a1) / 1000000000000000000}")
        print(f"a2: {sk.balanceOf(a2) / 1000000000000000000}")
        print(f"a3: {sk.balanceOf(a3) / 1000000000000000000}")

    bcheck()

    # reset allowance if needed
    if sk.allowance(a1, contract) > 0:
        sk.approve(contract, int(0), sender=a1)

    try:
        print(contract.bulkTransfer(sk, [(a2, int(0.01 * 1000000000000000000))], sender=a1))
        raise Exception("should have failed!")
    except exceptions.ContractError as e:
        if "insufficient allowance" not in str(e):
            raise

    sk.approve(contract, int(0.04 * 1000000000000000000), sender=a1)

    try:
        print(contract.bulkTransfer(sk, [(a2, int(0.05 * 1000000000000000000))], sender=a1))
        raise Exception("should have failed!")
    except exceptions.ContractError as e:
        if "insufficient allowance" not in str(e):
            raise

    print(sk.transfer(a2, int(0.01 * 1000000000000000000), sender=a1))
    print(contract.bulkTransfer(sk, [(a2, int(0.01 * 1000000000000000000)), (a3, int(0.01 * 1000000000000000000))], sender=a1))
    print(contract.bulkTransferAllowFailure(sk, [(a2, int(0.01 * 1000000000000000000)), (a3, int(0.01 * 1000000000000000000))], sender=a1))

    bcheck()
