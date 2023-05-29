from ape import accounts


def main():
    acc1 = accounts.load('acc1')
    acc2 = accounts.load('acc2')
    b1 = acc1.balance
    b2 = acc2.balance
    line = (b1 + b2) / 2
    if b1 > line:
        acc1.transfer(acc2, int(b1 - line))
    else:
        acc2.transfer(acc1, int(b2 - line))
