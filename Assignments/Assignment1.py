print("WELCOME TO TATA NEU")
print("----------------------------------")
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
product_price = float(input("Enter Price: "))
categories = input("Enter Categories (comma-separated): ")
product_categories = categories.split(",")
available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)
discount_percentage = float(input("Enter Discount Percentage: "))
features_input = input("Enter Product Features (comma-separated): ")
product_features = set(features_input.split(","))
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}
print("\nPRODUCT DETAILS SUMMARY")
print("-----------------------------------")
print("Using Comma Separation:")
print("Product ID, Name, Price:", product_id, product_name, product_price, sep=", ")
print("\nUsing Percentage Formatting:")
print("Product Discount: %.2f%%" % discount_percentage)
print("\nUsing f-strings:")
print(f"Product Name: {product_name}")
print(f"Price: ₹{product_price:.2f}")
print(f"Stock Available: {stock_details[0]} units")
print(f"Categories: {product_categories}")
print(f"Features: {product_features}")
print("\nUsing .format() Method:")
print("Supplier Details: Name - {}, Contact - {}, Location - {}"
      .format(supplier_details["name"], supplier_details["contact"], supplier_details["location"]))

print("-----------------------------------")
