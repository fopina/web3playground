// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.8.19;

import "@openzeppelin/token/ERC20/IERC20.sol";

/**
 * @title BulkTransfer
 * @dev Bulk transfer NFTs
 */
contract BulkTransfer {

    /**
     * @dev Store value in variable
     * @param token token contract address
     * @param to recipient address
     * @param amount token amount
     */
    function bulkTransfer(address token, address to, uint256 amount) public returns (bool) {
        return IERC20(token).transferFrom(msg.sender, to, amount);
    }
}
