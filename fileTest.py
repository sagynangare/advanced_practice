def get_transaction_from_file(filename="out.txt"):
    try:
        with open(filename) as f:
            content = f.readline()
            f.close()
    except IOError as e:
        print("I/O error ({0}):{1}".format(errorno, e.strerror))
        exit()
    transactions = []
    for line in content:
        transactions.append(frozenset(line.strip().split()))
        print(line)
    return transactions
get_transaction_from_file()
