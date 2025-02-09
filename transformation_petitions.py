import json
import pandas as pd
import uuid
from collections import Counter


# Define the file path
my_data = "input_data.json"

# Open and read the JSON file
with open(my_data, "r") as file:
    data = json.load(file)

# Print the JSON data
#print(data)


# Step 2: Extract Relevant Fields
petitions = []  # Create an empty list to store petitions
for petition in data:
    petition_id = str(uuid.uuid4())  # Create a unique ID for each petition
    title = petition["label"]["_value"]  # Get the title
    abstract = petition["abstract"]["_value"]  # Get the abstract
    petitions.append({
        "petition_id": petition_id,
        "text": f"{title} {abstract}"  # Combine title and abstract into one field
    })

# Create a DataFrame
df = pd.DataFrame(petitions)  # Convert the list into a DataFrame
# Print the first few rows to check
print(df.head())


# Tokenize, filter words, and count frequencies
def get_words(text):
    words = text.split()
    return [word.lower() for word in words if len(word) >= 5]

df["filtered_words"] = df["text"].apply(get_words)

# Collect all words across petitions
all_words = [word for words in df["filtered_words"] for word in words]
word_counts = Counter(all_words)

# Get the 20 most common words
top_20_words = [word for word, _ in word_counts.most_common(20)]

# Add columns for the most common words
for word in top_20_words:
    df[word] = df["filtered_words"].apply(lambda words: words.count(word))

# test the result
def test_get_words():
    text = "Government reforms are necessary for economy growth."
    result = get_words(text)
    assert "government" in result
    assert "reforms" in result
    assert "are" not in result  # Less than 5 letters
test_get_words()



# Save the result to a CSV file
output_columns = ["petition_id"] + top_20_words
output_df = df[output_columns]
output_df.to_csv("output_petitions.csv", index=False)

print("Output saved to output_petitions.csv")