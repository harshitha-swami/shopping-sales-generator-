# Dictionary of stores and their best sale times
store_sales = {
    "Amazon": "Black Friday, Prime Day, Cyber Monday",
    "Walmart": "Black Friday, Cyber Monday, Back to School",
    "Target": "Black Friday, Holiday Sales, Back to School",
    "Best Buy": "Black Friday, Cyber Monday, Holiday Sales",
    "Macy's": "Black Friday, Friends and Family Sale, Semi-Annual Sale",
    "Nordstrom": "Anniversary Sale, Half-Yearly Sale, Black Friday",
    "Home Depot": "Black Friday, Memorial Day, Labor Day",
    "Costco": "Holiday Sales, Seasonal Offers",
    "Kohl's": "Black Friday, Kohl’s Cash Events, Holiday Sales",
    "Sephora": "Hair Daily Deals, Points Multiplier Event, Sephora Savings Event",
    "Nike": "Sign up and get 50% off"
}

# Function to check capitalization
def check_capitalization(store):
    for proper_store in store_sales.keys():
        if store.lower() == proper_store.lower():
            return proper_store  # Return the correctly capitalized store name
    return None  # If no match is found, return None

# Function to get sales information
def get_best_sales(favorite_stores):
    for store in favorite_stores:
        corrected_store = check_capitalization(store)
        if corrected_store:
            print(f"The best sales times for {corrected_store} are: {store_sales[corrected_store]}")
        else:
            print(f"Sorry, we don't have sales information for '{store}'. Make sure to use proper capitalization.")

# Main Program
favorite_stores = input("Enter your favorite shopping stores, separated by commas: ").split(',')

# Strip extra spaces from the input
favorite_stores = [store.strip() for store in favorite_stores]

# Output the best sales times
get_best_sales(favorite_stores)

