# Aviva_Technical_Task

# Petition Word Frequency Transformation

This repository contains a Python script that transforms government petition data from a JSON format into a CSV file. The output includes a unique identifier for each petition and the frequency of the 20 most common words (with at least 5 letters) across all petitions.

---

## **Task Requirements**

1. Input 
   - A JSON file containing petitions with fields for `label`, `abstract`, and `numberOfSignatures`.

2. **Output**: 
   - A CSV file with one row per petition, containing:
     - `petition_id`: A unique identifier for each petition.
     - 20 columns, each representing one of the most common words across all petitions (words must be 5+ letters long).
