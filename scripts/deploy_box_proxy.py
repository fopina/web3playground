from ape import accounts, project


def main():
    account = accounts.load("acc1")
    project.Box.deploy(sender=account)
