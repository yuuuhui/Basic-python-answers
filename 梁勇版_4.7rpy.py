amount = eval(input("Enter the amount:"))
remainingamount = int(amount * 100)

onedollar = remainingamount // 100
remainingamount = remainingamount % 100

quarters = remainingamount // 25
remainingamount = remainingamount % 25

dimes = remainingamount // 10
remainingamount = remainingamount % 10

nickles = remainingamount // 5
remainingamount = remainingamount % 5

pennies = remainingamount

print("Your amount",amount,"consists of\n",
      "\t",onedollar,"dollars\n",
      "\t",quarters,"quarters\n",
      "\t",dimes,"dimes\n",
      "\t",nickles,"nickles\n",
      "\t",pennies,"pennies")
