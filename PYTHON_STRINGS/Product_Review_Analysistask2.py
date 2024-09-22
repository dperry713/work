# List of reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The service was excellent, and the staff was very friendly.",
    "I had a bad experience with this company.",
    "The quality is average, nothing special.",
    "The customer support was poor, not very helpful."
]

# List of positive and negative words
positive_words = ["good", "excellent", "friendly", "impressed"]
negative_words = ["bad", "poor", "average", "special"]

# Function to tally positive and negative words in reviews
def tally_sentiment(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    # Loop through each review
    for review in reviews:
        # Split the review into words
        words = review.lower().split()
        
        # Count positive and negative words
        for word in words:
            if word.strip(".,!") in positive_words:
                positive_count += 1
            elif word.strip(".,!") in negative_words:
                negative_count += 1

    return positive_count, negative_count

# Call the function and print the result
positive_count, negative_count = tally_sentiment(reviews, positive_words, negative_words)
print(f"Total Positive Words: {positive_count}")
print(f"Total Negative Words: {negative_count}")
