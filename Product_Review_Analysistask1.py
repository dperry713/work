# List of reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The service was excellent, and the staff was very friendly.",
    "I had a bad experience with this company.",
    "The quality is average, nothing special.",
    "The customer support was poor, not very helpful."
]

# Keywords to search for
keywords = ["good", "excellent", "bad", "poor", "average"]

# Function to capitalize keywords in reviews
def capitalize_keywords(reviews, keywords):
    # Loop through each review
    for review in reviews:
        # For each keyword, replace it with the uppercase version in the review
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        # Print the modified review
        print(review)

# Call the function to capitalize keywords and print reviews
capitalize_keywords(reviews, keywords)
