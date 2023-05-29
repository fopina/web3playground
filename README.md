# setup

* install ape

```
pip install -r requirements.txt
```

* create two wallets

```
ape accounts generate acc1
ape accounts generate acc2
```

* Fund `acc1` with https://faucet.avax.network/

* Split with `acc2`

```
a1 = accounts.load('acc1')
a2 = accounts.load('acc2')
a1.transfer(a2, int(a1.balance / 2))
```

