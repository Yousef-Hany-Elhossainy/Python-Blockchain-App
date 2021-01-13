blockchain = [[1]]

def get_last_blockchain_value():
    if len(blockchain) <1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount,last_transaction = [1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([get_last_blockchain_value(),transaction_amount])
    
def get_transaction_value():
    user_input = float(input("Enter the transaction amount: "))
    return user_input


def get_user_choice():
    user_input = input("Enter Choice: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print("outputting block")
        print(block)
    print(blockchain)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid    




while  True :
    print("Please choose: ")
    print("1: Add a transaction.")
    print("2: Output the blockchain blocks.")
    print("e: EXIT")
    print("h: Manipulate the chain")
    #print("v: Verify Chain Validity")


    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount,get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'e':
        break
    #elif user_choice == 'v':
    else:
        print("Input is not valid!")
    if not verify_chain():
        print("Blockchain is invalid")
        break
    else:
        print("Blockchain is valid")
    

print("Done.")