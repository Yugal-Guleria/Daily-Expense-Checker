9


#Asking user for their Budget

budget = input("Enter your daily budget: ")

#Asking spend acccording to user type

food = float(input("What is your today food expense? "))
transportation = float(input(" what is your today transportation expense? "))
entertainment = float(input("What is your today entertainment expense? "))
utilities = float(input("What is your today utilities expense? "))
other = float(input("What is your today other expenses? "))

# Total Calculations
total = food + transportation + entertainment + utilities + other
budget_float = float(budget)

# Budget comparison logic with emoji based status
print("\n" + "="*50)
if total <= budget_float * 0.5:
    print("✅ EXCELLENT You're spending wisely!")
    budget_percent = (total/budget_float)*100
    print("   " + str(total) + " / " + str(budget_float) + " → " + str(budget_percent) + "% of budget used")
    print("   💡 Consider saving more or investing the surplus.")
elif total <= budget_float:
    print("⚠️  CAUTION You're near your budget limit!")
    budget_percent = (total/budget_float)*100
    print("   " + str(total) + " / " + str(budget_float) + " → " + str(budget_percent) + "% of budget used")
    print("   💡 Try to cut down on non-essential spending.")
else:
    print("🚨 ALERT You've exceeded your budget!")
    budget_percent = (total/budget_float)*100
    print("   " + str(total) + " / " + str(budget_float) + " → " + str(budget_percent) + "% of budget used")
    difference = total - budget_float
    print("   💡 Immediate action: reduce by ₹" + str(difference))
print("="*50)

# Extra Category Based Insights
print("\n📊 CATEGORY-WISE BREAKDOWN:")

food_percentage = (food / total) * 100
print("🍔 Food: ₹" + str(food) + " (" + str(food_percentage) + "%)")
if food_percentage > 40:
    print("   ⚠️  High! Consider cooking at home or cheaper alternatives.")

transport_percentage = (transportation / total) * 100
print("🚗 Transport: ₹" + str(transportation) + " (" + str(transport_percentage) + "%)")
if transport_percentage > 30:
    print("   ⚠️  High! Check carpool, public transit, or biking options.")

entertainment_percentage = (entertainment / total) * 100
print("🎮 Entertainment: ₹" + str(entertainment) + " (" + str(entertainment_percentage) + "%)")

utilities_percentage = (utilities / total) * 100
print("💡 Utilities: ₹" + str(utilities) + " (" + str(utilities_percentage) + "%)")

other_percentage = (other / total) * 100
print("📦 Other: ₹" + str(other) + " (" + str(other_percentage) + "%)")
if other_percentage > 20:
    print("   ⚠️  High! Track small daily purchases more carefully.")
