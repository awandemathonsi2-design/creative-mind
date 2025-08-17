#Confirm the amount that is due and the addition of all coins which will be linked to the amount owed to the user
amount_due = 50
coins_added = 0

#Print amount due
print("Amount Due: 50")

#While true loop that checks if the coin inserted is in the list which will reduce the amount due and add the coins together
while True:
  coin_amount = int(input("Insert Coin: "))
  if coin_amount in [25, 10, 5]:
    amount_due -= coin_amount
    coins_added += coin_amount

#If the coins are greater than and equal to the amount due then the change owed is printed which results in terminating the execution of the loop
  if coins_added >= 50:
    print(f"Change owed: {coins_added - 50}")
    break
#If the coin inserted is out of the list then the amount due will be repeated
  else:
    print(f"Amount Due: {amount_due}")