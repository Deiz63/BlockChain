import requests
import pandas as pd

# Function to get the list of tradable pairs and save to CSV
def get_tradable_pairs_and_save_to_csv():
    url = 'https://api.kraken.com/0/public/AssetPairs'
    response = requests.get(url)
    data = response.json()
    pairs = data['result']
    
    # Extract each pair's details into a list of dictionaries
    pairs_list = []
    for pair in pairs:
        pair_info = pairs[pair]
        pair_info['pair_name'] = pair  # Add the pair name to the dictionary
        pairs_list.append(pair_info)
    
    # Normalize the list of dictionaries
    df = pd.json_normalize(pairs_list)
    
    # Save the DataFrame to a CSV file
    csv_file_path = 'kraken_tradable_pairs.csv'
    df.to_csv(csv_file_path, index=False)
    print(f'DataFrame saved to {csv_file_path}')

# Call the function
get_tradable_pairs_and_save_to_csv()
