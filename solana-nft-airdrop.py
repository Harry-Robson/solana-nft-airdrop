import subprocess
import time

#Read file for token addresses
token_file = open(r'C:\Users\h\Documents\Freelance\Solana_Owls\testing\token_list_test.txt')
lines = token_file.readlines()
token_file.close()

#Count which address we are up to
count = 0

#Send a 0.1 Solana tip to creator. Feel free to remove or edit tip.
tip = ["solana", "transfer", "2tmH3Yj661FoRwfqFshw1jm4ocFdd2Q17aSAGU9JrMzK", "0.1", "--allow-unfunded-recipient"]
send_tip = subprocess.Popen(tip)

#For the nth address we attempt to send token n
with open(r'C:\Users\h\Documents\Freelance\Solana_Owls\testing\wallet_list_test.txt') as fp:
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
        time.sleep
        if send.returncode != 0:
            print("ERROR sending token " + token + "to recipient: " + recipient)
        else:
            #Add 1 to count to make more understandable to everyone using
            print("Airdrop #" + str(count + 1) + " Complete")

        #Increase the address line count
        count = count + 1

print("DONE")
