// contracts/Box.sol
// SPDX-License-Identifier: MIT
// Testing proxy contracts: https://medium.com/coinmonks/beginners-guide-to-transparent-proxy-pattern-f40d6085bf3c
pragma solidity ^0.8.0;

import "@openzeppelin/proxy/transparent/TransparentUpgradeableProxy.sol";

contract BoxProxy is TransparentUpgradeableProxy {
    constructor() TransparentUpgradeableProxy(address _logic, address admin_, bytes memory _data) {}
}