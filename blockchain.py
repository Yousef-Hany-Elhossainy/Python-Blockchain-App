import functools
import hashlib
import json
from collections import OrderedDict


from hash_util import hash_string_256,hash_block

MINING_REWARD = 10

genesis_block = {
        'previous_hash': '',
        'block_index': 0,
        'transaction' : [],
        'proof' : 100
    }
blockchain = [genesis_block]
open_transactions = []
owner = "Yousef"
participants = {'Yousef'}



def valid_proof(transactions,last_hash,proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions,last_hash,proof):
        proof += 1
    return proof


def get_last_blockchain_value():
    """Returns the value of the last block in the blockchain"""
    if len(blockchain) <1:
        return None
    return blockchain[-1]


def get_balance(participant):
    """Returns the balance of the participant by subtracting the amount_sent from the amount_received."""

    tx_sender = [[tx['amount'] for tx in block['transaction'] if tx['sender'] == participant ] for block in blockchain]

    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    
    tx_sender.append(open_tx_sender)

    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += sum(tx)
    
    tx_recipient = [[tx['amount'] for tx in block['transaction'] if tx['recipient'] == participant ] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += sum(tx)
        
    return amount_received - amount_sent


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return   sender_balance >= transaction['amount']


def add_transaction(recipient,sender = owner,amount = 1.0):
    """Append a transaction to the open_transactions with a sender, recipient and amount.
    Add the sender and recipient to the participants. """

    # transaction = {
    #     'sender' : sender,
    #     'recipient' : recipient,
    #     'amount' : amount
    # }
    transaction = OrderedDict([('sender',sender) ,('recipient',recipient),('amount',amount)])
    if verify_transaction(transaction):        
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():

    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()

    # reward_transaction = {
    #     'sender' : 'MINING',
    #     'recipient' : owner,
    #     'amount' : MINING_REWARD
    # }
    reward_transaction = OrderedDict([('sender', 'MINING'),('recipient', owner),('amount', MINING_REWARD)])
    copied_transactions =open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transaction' : copied_transactions,
        'proof': proof
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
        if not valid_proof(block['transaction'][:-1],block['previous_hash'],block['proof']):
            print("Invalid proof of work")
            return False
            
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])
   

waiting_for_input = True


while  waiting_for_input :
    print("Please choose: ")
    print("1: Add a transaction.")
    print("2: Mine a new block.")
    print("3: Output the blockchain blocks.")
    print("4: Output participants.")
    print("5: Check transactions Validity")
    print("e: EXIT")
    print("h: Manipulate the chain")
    #print("v: Verify Chain Validity")

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount = amount):
            print("Added transaction.")
        else:
            print("Transaction failed.")
        print(open_transactions)
    elif user_choice =='2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("There are some invalid transactions")
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
    print('Balance of {} is {}'.format('Yousef',get_balance('Yousef')))
    
    

print("Done.")