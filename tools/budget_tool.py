def estimate_budget(
    flight_cost,
    hotel_price_per_night,
    number_of_days,
    daily_expense=2000
):
    """
    Estimate total travel budget.
    """

    hotel_cost = (
        hotel_price_per_night
        * number_of_days
    )

    local_expense = (
        daily_expense
        * number_of_days
    )

    total_cost = (
        flight_cost
        + hotel_cost
        + local_expense
    )

    return {

        "flight_cost": flight_cost,

        "hotel_cost": hotel_cost,

        "local_expense": local_expense,

        "total_cost": total_cost
    }