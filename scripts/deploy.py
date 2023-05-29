from ape import accounts, project


def main():
    account = accounts.load("acc2")
    project.Storage.deploy(sender=account)
    # account.deploy(project.Storage)
