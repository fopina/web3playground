require('@nomiclabs/hardhat-ethers');
require("@nomiclabs/hardhat-truffle5");
const { pkey } = require("./secrets.json")

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.19",
  networks: {
    fuji: {
      url: `https://api.avax-test.network/ext/bc/C/rpc`,
      accounts: [pkey],
    },
  },
};
