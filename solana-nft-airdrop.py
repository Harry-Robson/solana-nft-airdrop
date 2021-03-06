import subprocess

print("solana-nft-airdrop by Harry Robson © 2022")

#Read file for token addresses
token_file = open(r'token_list.txt')
lines = token_file.readlines()
token_file.close()

#Count which address we are up to
count = 0

#For the nth address we attempt to send token n
with open(r'wallet_list.txt') as fp:
    for line in fp:
        
        token = lines[count]
        token = token.strip('\n')
   
        recipient = line
        recipient = recipient.strip('\n')

        #Construct spl-token transfer command to send token from wallet to recipient
        cmd = ["spl-token", "transfer", token, "1", recipient, "--allow-unfunded-recipient", "--fund-recipient"]

        send = subprocess.Popen(cmd)
        send.communicate()
      
        #Check if all tokens succesfully sent to their respective wallets
        if send.returncode != 0:
            print("ERROR sending token " + token + "to recipient: " + recipient)
        else:
            #Add 1 to count to remove beginner confusion with index
            print("Airdrop #" + str(count + 1) + " Complete")

        #Increase the address line count
        count = count + 1

print("DONE")
