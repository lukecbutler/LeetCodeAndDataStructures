accounts = [[2,8,7],[7,1,3],[1,9,5]]
# return int, richest customer (array with maximum values)

richestCustomer = 0
for account in accounts:
    wealth = sum(account)
    if wealth > richestCustomer:
        richestCustomer = wealth
print(richestCustomer)
