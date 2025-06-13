#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optimised and secure version of the OxfordRisk data pipeline script.
"""

import os
import pandas as pd
import requests
from dotenv import load_dotenv

# --- Load environment variables from .env file ---
load_dotenv()
API_KEY = os.getenv("SUPABASE_API_KEY")

# --- Constants ---
PERSONALITY_CSV_URL = "https://raw.githubusercontent.com/karwester/behavioural-finance-task/refs/heads/main/personality.csv"
SUPABASE_URL = "https://pvgaaikztozwlfhyrqlo.supabase.co"
HEADERS = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}"
}

# --- Load Personality Data ---
def load_personality_data(url):
    try:
        df = pd.read_csv(url)
        print("Loaded Personality Data:\n", df.head())
        return df
    except Exception as e:
        print(f"Error loading personality data: {e}")
        return pd.DataFrame()

# --- Fetch Financial Assets from Supabase ---
def fetch_assets_data(base_url, headers):
    endpoint = f"{base_url}/rest/v1/assets?select=*"
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        df = pd.DataFrame(response.json())
        print("Loaded Assets Data:\n", df.head())
        return df
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(f"Failed to parse JSON: {e}")
    return pd.DataFrame()

# --- Main Execution ---
def main():
    personality_df = load_personality_data(PERSONALITY_CSV_URL)
    assets_df = fetch_assets_data(SUPABASE_URL, HEADERS)

if __name__ == "__main__":
    main()
