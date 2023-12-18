# setup

* install ape

```
pipenv install
```

* create two wallets

```
ape accounts generate acc1
ape accounts generate acc2
ape accounts generate acc3
```

* Fund `acc1` with https://faucet.avax.network/

* Split with `acc2`

```
a1 = accounts.load('acc1')
a2 = accounts.load('acc2')
a1.transfer(a2, int(a1.balance / 2))
```

------

sKewl Token:

0x2ceEbD7b004646ea6DE1b7b1679105371458F0Dd on Fuji
0x2cDBD48204929c6AD7b77CEd8d3E61364764E1D9 on FujiTest

sKewl Poop:

0x6Dd6802E2189a8D94f6cc1A5180f6c893e0bE13b on FujiTest

------

Gas tests

# single NFT via transfer
46232

# set approve on NFT
49322

# bulkTransferNFT: 2 * (addr+snail)
113327

## Testing

Run test scripts with `ape run <SCRIPT>`. Available scripts inside [scripts](scripts)
