genesis_block = {
        'previous_hash': '',
        'block_index': 0,
        'transaction' : []
    }
blockchain = [genesis_block]
open_transactions = []
owner = "Yousef"
participants = {'Yousef'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_last_blockchain_value():
    """Returns the value of the last block in the blockchain"""
    if len(blockchain) <1:
        return None
    return blockchain[-1]


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transaction'] if tx['sender'] == participant ] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    
    tx_recipient = [[tx['amount'] for tx in block['transaction'] if tx['recipient'] == participant ] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
        
    return amount_received - amount_sent


def add_transaction(recipient,sender = owner,amount = 1.0):
    # if last_transaction == None:
    #     last_transaction = [1]
    transaction = {
        'sender' : sender,
        'recipient' : recipient,
        'amount' : amount
    }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transaction' : open_transactions
    }
    blockchain.append(block)
    return True



def get_transaction_value():
    """Returns the input of the user"""
    tx_recipient = input("Enter the recipient of the transaction")
    tx_amount = float(input("Enter the transaction amount: "))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input("Enter Choice: ")
    return user_input


def print_blockchain_elements():
    print("\n" + "-"*30 + "\n")
    for block in blockchain:
        print("outputting block")
        print(block)
    else:
        print("-"*30)
    print(blockchain)
    print("\n" + "-"*30)


def verify_chain():
    """Verify current blockchain and return True if valid, False otherwise"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]) :
            return False
    return True
    

waiting_for_input = True


while  waiting_for_input :
    print("Please choose: ")
    print("1: Add a transaction.")
    print("2: Mine a new block.")
    print("3: Output the blockchain blocks.")
    print("4: Output participants.")
    print("e: EXIT")
    print("h: Manipulate the chain")
    #print("v: Verify Chain Validity")

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount = amount)
        print(open_transactions)
    elif user_choice =='2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
        'previous_hash': '',
        'block_index': 0,
        'transaction' : [{'sender': 'asdfg', 'recipient': 'Yousef', 'amount': 1000}]
    }
    elif user_choice == 'e':
        waiting_for_input = False
    #elif user_choice == 'v':
    else:
        print("Input is not valid!")
    if not verify_chain():
        print("-"*30)
        print_blockchain_elements()
        print("Blockchain is invalid")
        break
    else:
        print("Blockchain is valid")
    print(get_balance('Yousef'))
    
    

print("Done.")