import requests

# Extract csv from the link
def download_csv(url, save_path):
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"CSV file downloaded successfully to {save_path}")
    else:
        print(f"Failed to download CSV. Status code: {response.status_code}")


csv_url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/stress.csv"
save_path = ".\data\stress.csv"
download_csv(csv_url, save_path)
