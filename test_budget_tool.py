from tools.budget_tool import estimate_budget


budget = estimate_budget(
    flight_cost=5000,
    hotel_price_per_night=3000,
    number_of_days=4
)

print("\nBudget Breakdown:\n")

for key, value in budget.items():

    print(f"{key}: ₹{value}")