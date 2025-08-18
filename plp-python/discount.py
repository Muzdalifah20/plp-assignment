def  calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    total = price  (1 - discount_percent / 100)
  else:
    total = price
  return total

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent:
  print(f"Final price after {discount_percent}% discount: {final_price:.2f")
else:
  print(f"No discount applied. The original price is {price:.f2}")
