# solana-nft-airdrop
Airdrop a list of Solana token addresses (including NFTs) to a list of wallet addresses. 

## Installation
Clone the latest commit to your machine by clicking 'Code' and then 'Download Zip'.

## Prerequisites
* [Solana Tool Suite](https://docs.solana.com/cli/install-solana-cli-tools)
* [spl-token command line utility](prerequisite)
* [Python 3.10 or higher](https://www.python.org/download/releases/3.1/)
* A list of SPL token addresses (including NFTs) that you would like to airdrop. You can get a hash list using the [Magic Eden Hash List Generator](https://magiceden-io.webpkgcache.com/doc/-/s/magiceden.io/mintlist-tool). You will then need add the token addresses to be one per line in token_list.txt.
* A list of Solana wallet addresses. These should also be formatted as 1 per line in wallet_list.txt.
* You must use the command: ```solana config set -k <your key file>``` to ensure that the currently selected wallet contains all the tokens listed in token_list.txt.
* The Solana wallet should have enough funds to cover the airdrop and account creation costs.

## Usage
* Open command prompt
* Navigate to the repo directory ```cd /users/tom/github/solana-nft-airdrop```
* Run the python script using command ```python3 solana-nft-airdrop.py```
* Any failed transactions will appear in the command prompt.
* A succesful airdrop will print ```Airdrop #1 Complete``` to the command prompt.
* Once all tokens have been airdropped ```DONE``` will be printed.

## Airdrop costs
* It costs 0.00204428 Solana to airdrop a token to a wallet that does not already have an account corresponding to the sent token.

## Voluntary Tip
* This script, in it's current state, will tip me 0.1 Solana for every usage. Feel free to remove this if you want.


