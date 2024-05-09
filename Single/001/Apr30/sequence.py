import requests

def fetch_sequence(sequence_id):
    url = f"https://oeis.org/search?q=id:{sequence_id}&fmt=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract the sequence from the response data
        sequence = data['results'][0]['data']
        return sequence
    else:
        return "Error: Failed to retrieve data"

def main():
    sequence_id = input("Enter OEIS sequence ID (e.g., A000055): ")
    result = fetch_sequence(sequence_id)
    print("Sequence:", result)

if __name__ == "__main__":
    main()

