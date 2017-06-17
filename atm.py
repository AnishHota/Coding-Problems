inp = input().split()
withdraw_amount = float(inp[0])
bank_balance = float(inp[1])
if withdraw_amount%5==0 and withdraw_amount<=(bank_balance-0.5):
    print("%0.2f"%(bank_balance-withdraw_amount-0.50))
else:
    print("%0.2f"%bank_balance)
