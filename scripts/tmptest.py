from ape import accounts, project, Contract


def main():
    contract = project.BulkTransfer.deployments[-1]
    print(f'Using deployment {contract}')

    a1 = accounts.load("acc1")
    a2 = accounts.load("acc2")

    def bcheck():
        print('== Balance check')
        print(f'a1: {a1.balance / 1000000000000000000}')
        print(f'a2: {a2.balance / 1000000000000000000}')
    
    bcheck()

    print(contract.bulkTransferToken('0xD9D01A9F7C810EC035C0e42cB9E80Ef44D7f8692', a2, int(0.01 * 1000000000000000000), sender=a1))

    bcheck()
