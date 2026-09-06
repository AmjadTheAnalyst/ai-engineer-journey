# ==============================================================================
# 📦 PROBLEM: Smart Shipping Calculator (Medium Level)
# ==============================================================================
# You are building a custom shipping calculator for an e-commerce platform.
# Write a Python script that takes a package's weight and shipping speed,
# then calculates the final shipping fee based on the rules below.
#
# 📥 Inputs to create:
# 1. weight (float): Package weight in kilograms.
# 2. is_express (str): "yes" or "no" for express shipping speed.
#
# 📋 Pricing Rules (Order of execution and boundaries matter!):
# 1. Invalid Input: If weight is 0 or less -> Print "Invalid weight"
#
# 2. Free Tier: If weight is <= 2 kg AND standard shipping ("no") -> Fee: $0
#
# 3. Standard Tier: If weight is <= 2 kg AND express shipping ("yes") -> Fee: $10
#
# 4. Medium Tier: If weight is > 2 kg and up to 10 kg:
#    - Standard shipping ("no") -> Fee: $15
#    - Express shipping ("yes") -> Fee: $25
#    * SPECIAL RULE: If weight is EXACTLY 5.0 kg, apply a $5 discount.
# 5. Heavy Tier: If weight is > 10 kg and up to 20 kg -> Fee: $40 (for both speeds)
#
# 6. Oversized Tier: If weight is > 20 kg -> Print "Requires freight shipping"
#
# 🧪 Test Cases to verify your logic:
# - weight = 1.5,  is_express = "no"  -> Expected Output: Shipping Fee: $0
# - weight = 1.5,  is_express = "yes" -> Expected Output: Shipping Fee: $10
# - weight = 5.0,  is_express = "yes" -> Expected Output: Shipping Fee: $20
# - weight = 12.0, is_express = "no"  -> Expected Output: Shipping Fee: $40
# - weight = 25.0, is_express = "no"  -> Expected Output: Requires freight shipping
# ==============================================================================

# Write your solution below:
package_weight = float(input("Package weight in kilograms: "))
standard_shipping = input("Is package needs express speed? (yes/no): ")
price15 = 15 - ((5*15)/100)
price25 = 25 - ((5*25)/100)
#defining pricing rules
if (package_weight <=0):
    print("Invalid weight")
elif (package_weight <=2 and standard_shipping == "no"):
    print("This is a Free Tier and costs 0$")
elif (package_weight <=2 and standard_shipping == "yes"):
    print("This is a Standard Tier and costs 10$")
#if weight is exactly 5kg, then there is 5% discount offer.
elif (package_weight >2 and package_weight <10):
    if (standard_shipping == "no" and package_weight != 5.0):
        print("This is a Medium Tier and costs 15$")
    elif (standard_shipping == "no" and package_weight == 5.0):
        print("This is Medium Tier and costs 15$")
        print("Hurry, There is 5percent Discount")
        print("Final cost after discount is", price15)
    if (standard_shipping == "yes" and package_weight != 5.0):
            print("This is a Medium Tier and costs 25$")
    elif (standard_shipping == "yes" and package_weight == 5.0):
        print("This is Medium Tier and costs 25$")
        print("Hurry, There is 5percent Discount")
        print("Final cost after discount is", price25)
elif (package_weight >10 and package_weight <20):
    print("This is a Heavy tier and costs 40$")
elif (package_weight >20):
    print("This is a Oversized Tier and requires freight shipping")
else:
    print("Something went wrong")

