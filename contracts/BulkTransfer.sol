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
    function bulkTransferToken(address token, address to, uint256 amount) public returns (bool) {
        return IERC20(token).transferFrom(msg.sender, to, amount);
    }

    /**
     * @dev Store value in variable
     * @param to recipient address
     * @param amount token amount
     */
    function bulkTransfer(address payable to, uint256 amount) payable public returns (bool) {
        to.transfer(amount);
        return true;
    }
}
