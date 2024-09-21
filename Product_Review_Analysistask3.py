import textwrap

# Function to summarize review
def summarize_review(review, max_length=30):
    if len(review) <= max_length:
        return review
    else:
        # Use textwrap to shorten without breaking words
        summary = textwrap.shorten(review, width=max_length, placeholder="…")
        return summary

# List of reviews
reviews = [
    "This product is amazing, I love the quality and the features it offers!",
    "The service was decent, but there is room for improvement.",
    "Unfortunately, I had a very poor experience with the product."
]

# Apply the summarize function to each review
for review in reviews:
    print(summarize_review(review))
