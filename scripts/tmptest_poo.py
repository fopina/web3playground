from ape import accounts, project, exceptions


def pp(tx):
    print('Gas used:', tx.gas_used)


def main():
    # hacky "test" because of lack of funds in "ape test" accounts
    contract = project.BulkTransfer.deployments[-1]
    sk = project.sKewlPoo.at("0x6Dd6802E2189a8D94f6cc1A5180f6c893e0bE13b")

    print(f"Using deployment {contract}")

    a1 = accounts.load("acc1")
    a2 = accounts.load("acc2")
    a3 = accounts.load("acc3")

    def bcheck():
        print("== Balance check")
        print(f"a1: {sk.balanceOf(a1)}")
        print(f"a2: {sk.balanceOf(a2)}")
        print(f"a3: {sk.balanceOf(a3)}")

    bcheck()

    _b = sk.balanceOf(a2)
    if _b > 1:
        # if 2, both tokens stuck there
        print("## Restore transfer from a2")
        pp(sk.transferFrom(a2, a1, 1, sender=a2))
        pp(sk.transferFrom(a2, a1, 2, sender=a2))
    elif _b > 0:
        raise Exception("cannot be")

    _b = sk.balanceOf(a3)
    if _b == 1:
        print("## Restore transfer from a3")
        pp(sk.transferFrom(a3, a1, 1, sender=a3))
    elif _b > 0:
        raise Exception("cannot be")

    # reset allowance if needed
    if sk.isApprovedForAll(a1, contract):
        print("## Reset approvalForAll")
        pp(sk.setApprovalForAll(contract, False, sender=a1))
    if sk.isApprovedForAll(a2, contract):
        print("## Reset approvalForAll")
        pp(sk.setApprovalForAll(contract, False, sender=a2))

    if sk.getApproved(1) != "0x0000000000000000000000000000000000000000":
        print("## Reset approve on 1")
        pp(sk.approve("0x0000000000000000000000000000000000000000", 1, sender=a1))
    if sk.getApproved(2) != "0x0000000000000000000000000000000000000000":
        print("## Reset approve on 2")
        pp(sk.approve("0x0000000000000000000000000000000000000000", 2, sender=a1))

    try:
        pp(contract.bulkTransferNFT(sk, [(a2, 1)], sender=a1))
        raise Exception("should have failed!")
    except exceptions.ContractError as e:
        if "caller is not token owner or approved" not in str(e):
            raise

    print("## Set approve on 1")
    pp(sk.approve(contract, 1, sender=a1))

    try:
        pp(contract.bulkTransferNFT(sk, [(a2, 2)], sender=a1))
        raise Exception("should have failed!")
    except exceptions.ContractError as e:
        if "caller is not token owner or approved" not in str(e):
            raise

    try:
        pp(contract.bulkTransferNFT_S(sk, a2, [1, 2], sender=a1))
        raise Exception("should have failed!")
    except exceptions.ContractError as e:
        if "caller is not token owner or approved" not in str(e):
            raise

    print("## Set approve on 2")
    pp(sk.approve(contract, 2, sender=a1))
    pp(contract.bulkTransferNFT_S(sk, a2, [1, 2], sender=a1))

    try:
        pp(contract.bulkTransferNFT(sk, [(a1, 2), (a3, 1)], sender=a2))
        raise Exception("should have failed!")
    except exceptions.ContractError as e:
        if "caller is not token owner or approved" not in str(e):
            raise

    print("## Set approveAll")
    pp(sk.setApprovalForAll(contract, True, sender=a2))
    pp(contract.bulkTransferNFT(sk, [(a1, 2), (a3, 1)], sender=a2))

    bcheck()
