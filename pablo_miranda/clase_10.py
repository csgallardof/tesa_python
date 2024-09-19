
print("CSV")

with open("products.csv", "r") as file:
    print("Product CSV Lines: ", len(file.readlines()))

with open("monthly_sales.csv", "r") as file:
    print("Monthly Sales CSV Lines: ", len(file.readlines()))
