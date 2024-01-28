stock_name:input("Enter stock's name : " )
num_purchase=float(input("Enter the total number of purchased share : "))
dollar_amount_per_purchase_share=float(input("Enter the dollar amount paid per a purchased share: "))
total_purchase=num_purchase * dollar_amount_per_purchase_share

num_sold=float(input("Enter the total number of sold share : "))
dollar_amount_per_sold_share=float(input("Enter the dollar amount paid per a sold share : "))
total_sold=num_sold * dollar_amount_per_sold_share

purchase_commission=0
sale_commission=0

total_sale_amount=num_sold*dollar_amount_per_sold_share
profit=total_sale_amount - total_purchase - purchase_commission- sale_commission

profit 


if num_purchase <1000:
    purchase_commission + 100
    print("Purchase CommissionL ", purchase_commission)
else:
    purchase_commission
    print("Purchase Commission : ", purchase_commission)

if num_sold <1000 :
    sale_commission +100
    print("Sold commssion: ", sale_commission)
else 1000 <num_sold <2000:
    sale_commission +50
    print("Sold commission :", sale_commission)



print("*** Welcome to Stock Value Calculator Progma! ***")
print("Enter stock's name : " ,num_purchase)
print("Enter the dollar amount paid per a purchased share: ",  dollar_amount_per_purchase_share)
print("Enter the total number of sold share: ",  dollar_amount_per_sold_share)
print("Enter the dollar amout paid per a sold share : ",  num_sold)
print("Purchasing Report" )
print("Stock Name", stock_name)
print("Total Purchase Amount : ", total_purchase)
print("Selling Report")
print("Total Sold Amount: ", total_sold)
# print("Sold commision : " , )
# print("sold commission : ",  ?????????) 

