// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.8.19;

import "@openzeppelin/token/ERC20/IERC20.sol";
import "@openzeppelin/token/ERC721/IERC721.sol";

/**
 * @title BulkTransfer
 * @dev Bulk transfer NFTs
 */
contract BulkTransfer {
    struct Call {
        address to;
        uint256 amountOrTokenId;
    }

    /**
     * @dev Transfer token to different recipients
     * @param token token contract address
     * @param calls an array of Call structs
     */
    function bulkTransfer(address token, Call[] calldata calls) public {
        uint256 length = calls.length;
        Call calldata call;
        for (uint256 i = 0; i < length;) {
            bool success;
            call = calls[i];
            success = IERC20(token).transferFrom(msg.sender, call.to, call.amountOrTokenId);
            require(success, "bulkTransfer: call failed");
            unchecked { ++i; }
        }
    }

    /**
     * @dev Transfer token to different recipients - commit even if some fail
     * @param token token contract address
     * @param calls an array of Call structs
     */
    function bulkTransferAllowFailure(address token, Call[] calldata calls) public returns (bool[] memory returnData) {
        uint256 length = calls.length;
        returnData = new bool[](length);
        Call calldata call;
        for (uint256 i = 0; i < length;) {
            call = calls[i];
            returnData[i] = IERC20(token).transferFrom(msg.sender, call.to, call.amountOrTokenId);
            unchecked { ++i; }
        }
        return returnData;
    }

    /**
     * @dev Transfer token to different recipients
     * @param token token contract address
     * @param calls an array of Call structs
     */
    function bulkTransferNFT(address token, Call[] calldata calls) public {
        uint256 length = calls.length;
        Call calldata call;
        for (uint256 i = 0; i < length;) {
            call = calls[i];
            IERC721(token).transferFrom(msg.sender, call.to, call.amountOrTokenId);
            unchecked { ++i; }
        }
    }

    /**
     * @dev Transfer token to different recipients
     * @param token token contract address
     * @param to token contract address
     * @param tokenIds an array of Call structs
     */
    function bulkTransferNFT_S(address token, address to, uint256[] calldata tokenIds) public {
        uint256 length = tokenIds.length;
        uint256 tokenId;
        for (uint256 i = 0; i < length;) {
            tokenId = tokenIds[i];
            IERC721(token).transferFrom(msg.sender, to, tokenId);
            unchecked { ++i; }
        }
    }
}
