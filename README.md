# solana-nft-airdrop
Airdrop a list of Solana token addresses (including NFTs) to a list of wallet addresses. 

## Installation
Clone the latest commit to your machine by clicking 'Code' and then 'Download Zip'.

## Prerequisites
* [Solana Tool Suite](https://docs.solana.com/cli/install-solana-cli-tools)
* [spl-token command line utility](prerequisite)
* A list of SPL token addresses (including NFTs) that you would like to airdrop. You can get a hash list using the [Magic Eden Hash List Generator](https://magiceden-io.webpkgcache.com/doc/-/s/magiceden.io/mintlist-tool). You will then need add the token addresses to be one per line in token_list.txt.
* A list of Solana wallet addresses. These should also be formatted as 1 per line in wallet_list.txt.
* You must use the command: ```solana config set -k <your key file>``` to ensure that the currently selected wallet contains all the tokens listed in token_list.txt.
* The Solana wallet should have enough funds to cover the airdrop and account creation costs.

## Voluntary Tip
* This script, in it's current state, will tip me 0.1 Solana for every usage. Feel free to remove this if you want.


