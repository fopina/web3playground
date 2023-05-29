from ape import accounts, project


def main():
    contract = project.Storage.deployments[-1]
    a1 = accounts.load("acc1")
    a2 = accounts.load("acc2")

    def bcheck():
        print('== Balance check')
        print(f'a1: {a1.balance / 1000000000000000000}')
        print(f'a2: {a2.balance / 1000000000000000000}')
    
    bcheck()

    print(contract.retrieve(sender=a1))
    print(contract.retrieve(sender=a2))
    print(contract.store(5, sender=a1))
    print(contract.retrieve(sender=a1))
    print(contract.retrieve(sender=a2))

    bcheck()
