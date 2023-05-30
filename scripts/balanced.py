from ape import accounts


def main():
    accs = [
        [accounts.load("acc1")],
        [accounts.load("acc2")],
        [accounts.load("acc3")],
    ]
    for a in accs:
        b = a[0].balance
        a.append(b)

    line = sum(a[1] for a in accs) / len(accs)
    for a in accs:
        a.append(a[1] - line)

    def _sort():
        accs.sort(key=lambda x: x[2], reverse=True)

    while True:
        _sort()
        print(accs)
        recv = accs[-1]
        snd = accs[0]
        if recv[2] >= 0:
            print("DONE")
            break
        if snd[2] <= 0:
            print("no bal")
            break
        amt = int(min(snd[2], abs(recv[2])))
        print(snd, recv, amt)
        print(snd[0].transfer(recv[0], amt))
        recv[2] += amt
        snd[2] -= amt
