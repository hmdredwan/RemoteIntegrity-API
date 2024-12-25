import requests
import time
import csv

# Step 1: Fetch data from the Countries GraphQL API
def fetch_countries():
    graphql_endpoint = "https://countries.trevorblades.com/"
    query = {
        "query": """
        query {
            countries {
                name
                capital
                currency
            }
        }
        """
    }

    try:
        response = requests.post(graphql_endpoint, json=query)
        response.raise_for_status()
        data = response.json()
        countries = data['data']['countries']
        print("Fetched countries successfully.")
        return countries
    except requests.exceptions.RequestException as e:
        print(f"Error fetching countries: {e}")
        return []

# Step 2: Post country details to the REST API
def post_country_details(country):
    rest_endpoint = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": f"Country: {country['name']}",
        "body": f"Capital: {country['capital']}, Currency: {country['currency']}",
        "userId": 1
    }

    retries = 0
    max_retries = 5

    while retries < max_retries:
        try:
            response = requests.post(rest_endpoint, json=payload)
            if response.status_code == 403:
                print("403 Forbidden: Skipping the request.")
                return None
            response.raise_for_status()
            print("Country details posted successfully.")
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 500:
                wait_time = 2 ** retries
                print(f"500 Internal Server Error: Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                retries += 1
            else:
                print(f"Error posting country details: {e}")
                return None
    print("Max retries reached. Failed to post country details.")
    return None

# Step 5: Save data to a CSV file
def save_to_csv(countries, filename="countries.csv"):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Country Name", "Capital", "Currency"])
            for country in countries:
                writer.writerow([country['name'], country.get('capital', 'N/A'), country.get('currency', 'N/A')])
        print(f"Countries saved to {filename} successfully.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# Main method
def main():
    # Step 1: Fetch data
    countries = fetch_countries()
    if not countries:
        print("No countries fetched. Exiting.")
        return

    # Step 2: Select one country
    selected_country = countries[0]
    print(f"Selected country: {selected_country['name']}")

    # Step 3: Post the selected country's details to the REST API
    post_response = post_country_details(selected_country)
    if post_response:
        print(f"Response from REST API: {post_response}")

    # Step 5: Save all fetched countries to a CSV file
    save_to_csv(countries)

if __name__ == "__main__":
    main()

