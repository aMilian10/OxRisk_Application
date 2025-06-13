#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 12:35:09 2025

@author: maximilian
"""

Python 3.9.13 (main, Aug 25 2022, 18:29:29) 
Type "copyright", "credits" or "license" for more information.

IPython 7.31.1 -- An enhanced Interactive Python.

conda update anaconda
conda install spyder=6.0.7
  File "/var/folders/9b/cn9nrl2s1z5129ys5314fkdh0000gn/T/ipykernel_44497/573809825.py", line 1
    conda update anaconda
          ^
SyntaxError: invalid syntax


# === IMPORT LIBRARIES ===
import pandas as pd
import requests

# === LOAD PERSONALITY CSV DATA ===
personality_url = "https://raw.githubusercontent.com/karwester/behavioural-finance-task/refs/heads/main/personality.csv"
personality_df = pd.read_csv(personality_url)

print("Personality Data Preview:")
print(personality_df.head())

# === CONNECT TO SUPABASE API ===
SUPABASE_URL = "https://pvgaaikztozwlfhyrqlo.supabase.co"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB2Z2FhaWt6..."
HEADERS = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}"
}

# === FETCH FINANCIAL ASSETS DATA ===
assets_url = f"{SUPABASE_URL}/rest/v1/assets?select=*"
response = requests.get(assets_url, headers=HEADERS)

# Check if request was successful
print("\nAPI Response Status Code:", response.status_code)

# Show response text (in case it's not formatted correctly)
print("Raw Response Text:\n", response.text)

# === ATTEMPT TO CONVERT TO DATAFRAME ===
try:
    assets_df = pd.DataFrame(response.json())
    print("\nAssets Data Preview:")
    print(assets_df.head())
except Exception as e:
    print("Failed to parse API response:", e)
    
Personality Data Preview:
   _id  confidence  risk_tolerance  composure  impulsivity  impact_desire
0    1       0.550           0.510      0.565        0.161          0.999
1    2       0.486           0.474      0.439        0.818          0.048
2    3       0.565           0.568      0.578        0.832          0.977
3    4       0.652           0.625      0.642        0.507          0.407
4    5       0.477           0.483      0.515        0.006          0.871

API Response Status Code: 401
Raw Response Text:
 {"message":"Invalid API key","hint":"Double check your Supabase `anon` or `service_role` API key."}
Failed to parse API response: If using all scalar values, you must pass an index

import pandas as pd
import requests

# Load the CSV again just in case
csv_url = "https://raw.githubusercontent.com/karwester/behavioural-finance-task/refs/heads/main/personality.csv"
personality_df = pd.read_csv(csv_url)

# Supabase connection details
SUPABASE_URL = "https://pvgaaikztozwlfhyrqlo.supabase.co"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB2Z2FhaWt6dG96d2xmaHlycWxvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE2MjUsImV4cCI6MjA2QxNzYyNX0.iAqMXnJ_sJuBMtA6FPNCRcYnKw95YkJvY3OhCIZ77vI"

# Correct full API endpoint
endpoint = f"{SUPABASE_URL}/rest/v1/assets?select=*"

headers = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Make the GET request
response = requests.get(endpoint, headers=headers)

# Check the response
print("Status Code:", response.status_code)
print("Preview of raw JSON:", response.text[:300])  # show just a snippet

# Convert to DataFrame if successful
if response.status_code == 200:
    try:
        assets_df = pd.DataFrame(response.json())
        print("\nAssets Data Preview:")
        print(assets_df.head())
    except Exception as e:
        print("Error converting JSON to DataFrame:", e)
else:
    print("Failed to retrieve data from Supabase.")
    
Status Code: 401
Preview of raw JSON: {"message":"Invalid API key","hint":"Double check your Supabase `anon` or `service_role` API key."}
Failed to retrieve data from Supabase.

import pandas as pd
import requests

# Load the CSV again just in case
csv_url = "https://raw.githubusercontent.com/karwester/behavioural-finance-task/refs/heads/main/personality.csv"
personality_df = pd.read_csv(csv_url)

# Supabase connection details
SUPABASE_URL = "https://pvgaaikztozwlfhyrqlo.supabase.co"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB2Z2FhaWt6dG96d2xmaHlycWxvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc4NDE2MjUsImV4cCI6MjA2MzQxNzYyNX0.iAqMXnJ_sJuBMtA6FPNCRcYnKw95YkJvY3OhCIZ77vI"

# Correct full API endpoint
endpoint = f"{SUPABASE_URL}/rest/v1/assets?select=*"

headers = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Make the GET request
response = requests.get(endpoint, headers=headers)

# Check the response
print("Status Code:", response.status_code)
print("Preview of raw JSON:", response.text[:300])  # show just a snippet

# Convert to DataFrame if successful
if response.status_code == 200:
    try:
        assets_df = pd.DataFrame(response.json())
        print("\nAssets Data Preview:")
        print(assets_df.head())
    except Exception as e:
        print("Error converting JSON to DataFrame:", e)
else:
    print("Failed to retrieve data from Supabase.")
    
Status Code: 200
Preview of raw JSON: [{"_id":1,"asset_allocation":"Equities","asset_allocation_id":39958838,"asset_currency":"USD","asset_value":217.06,"created":"2025-02-25T09:18:34.158728+00:00"}, 
 {"_id":1,"asset_allocation":"Commodities","asset_allocation_id":83197857,"asset_currency":"GBP","asset_value":159.05,"created":"2025-05-

Assets Data Preview:
   _id asset_allocation  ...  asset_value                           created
0    1         Equities  ...       217.06  2025-02-25T09:18:34.158728+00:00
1    1      Commodities  ...       159.05  2025-05-18T09:18:34.162165+00:00
2    2             Cash  ...       231.12  2025-03-06T09:18:34.162165+00:00
3    2             Cash  ...       321.75  2025-02-22T09:18:34.163356+00:00
4    3           Crypto  ...       181.15  2025-04-17T09:18:34.163356+00:00

[5 rows x 6 columns]

# Step 1: Rename columns to match merge key (assuming _id in assets_df == id in personality_df)
assets_df = assets_df.rename(columns={"_id": "id"})

# Step 2: Convert all asset values to GBP using a made-up conversion rate
conversion_rates = {
    "GBP": 1.0,
    "USD": 0.79
}

assets_df["asset_value_gbp"] = assets_df.apply(
    lambda row: row["asset_value"] * conversion_rates.get(row["asset_currency"], 1),
    axis=1
)

# Step 3: Group by ID and calculate total assets
asset_totals = assets_df.groupby("id")["asset_value_gbp"].sum().reset_index()
asset_totals = asset_totals.rename(columns={"asset_value_gbp": "total_assets_gbp"})

# Step 4: Merge with personality data
merged_df = pd.merge(personality_df, asset_totals, on="id", how="left")

# Step 5: Find the individual with the highest total assets
top_individual = merged_df.sort_values(by="total_assets_gbp", ascending=False).iloc[0]

print("🎯 Top Individual Summary:")
print(f"ID: {top_individual['id']}")
print(f"Total Assets (GBP): {top_individual['total_assets_gbp']:.2f}")
print(f"Risk Tolerance Score: {top_individual['risk_tolerance']}")
Traceback (most recent call last):

  File "/var/folders/9b/cn9nrl2s1z5129ys5314fkdh0000gn/T/ipykernel_44497/2729373832.py", line 20, in <module>
    merged_df = pd.merge(personality_df, asset_totals, on="id", how="left")

  File "/Users/maximilian/opt/anaconda3/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 107, in merge
    op = _MergeOperation(

  File "/Users/maximilian/opt/anaconda3/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 700, in __init__
    ) = self._get_merge_keys()

  File "/Users/maximilian/opt/anaconda3/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 1110, in _get_merge_keys
    left_keys.append(left._get_label_or_level_values(lk))

  File "/Users/maximilian/opt/anaconda3/lib/python3.9/site-packages/pandas/core/generic.py", line 1840, in _get_label_or_level_values
    raise KeyError(key)

KeyError: 'id'


print("Assets DF Columns:", assets_df.columns.tolist())
print("Personality DF Columns:", personality_df.columns.tolist())
Assets DF Columns: ['id', 'asset_allocation', 'asset_allocation_id', 'asset_currency', 'asset_value', 'created', 'asset_value_gbp']
Personality DF Columns: ['_id', 'confidence', 'risk_tolerance', 'composure', 'impulsivity', 'impact_desire']

# Merge on assets_df.id and personality_df._id
merged_df = pd.merge(personality_df, asset_totals, left_on="_id", right_on="id", how="left")

# Sort and print the top individual
top_individual = merged_df.sort_values(by="total_assets_gbp", ascending=False).iloc[0]

print("🎯 Top Individual Summary:")
print(f"ID: {top_individual['_id']}")
print(f"Total Assets (GBP): {top_individual['total_assets_gbp']:.2f}")
print(f"Risk Tolerance Score: {top_individual['risk_tolerance']}")
🎯 Top Individual Summary:
ID: 284.0
Total Assets (GBP): 148378.33
Risk Tolerance Score: 0.481