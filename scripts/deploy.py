from ape import accounts, project


def main():
    account = accounts.load("acc2")
    project.BulkTransfer.deploy(sender=account)
