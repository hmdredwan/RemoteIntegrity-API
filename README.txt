This document explains the approach taken to solve the API Test. The implementation is written in Python, with a focus on clear structure, automation, and robust error handling.
Overview
The task is divided into several steps:
1.	Fetch data using a GraphQL API.
2.	Post selected data to a REST API.
3.	Handle potential errors gracefully.
4.	Automate the workflow end-to-end.
5.	Save fetched data to a CSV file for additional data manipulation.

Step-by-Step Approach
1.	GraphQL API Query:
	i. The script sends a POST request to the GraphQL endpoint using the "requests" library.
	ii. The GraphQL query fetches the name, capital, and currency of all countries.
	iii. The response is parsed to extract the relevant fields, and data is stored in a list of dictionaries.
	iv. Error handling is added to log and manage any issues during the data fetch.

2.	REST API Interaction:
    i. Details of one country (e.g., the first from the fetched data) are posted to a mock REST API endpoint.
    ii. The request includes a JSON payload with the country's name, capital, and currency.
    iii. If a 403 Forbidden error occurs, the request is skipped with a logged message.
    iv.  If a 500 Internal Server Error occurs, the script retries the request using exponential backoff, doubling the wait time after each retry (up to 5 retries).
    v. Other errors are logged and handled gracefully.
3.	Error Handling:
    i. All HTTP request errors are caught and logged with specific details.
    ii. 403 and 500 status codes have custom handling:
    iii. 403 errors are skipped.
    iv. 500 errors trigger retries with increasing wait times to handle transient issues.
    v. All errors are logged to the console for debugging.
4.	Automation:
    i. The workflow is automated using a main function, ensuring that:
    ii. Data is fetched from the GraphQL API.
    iii. One country is selected for REST API interaction.
    iv. Data is saved to a CSV file .
    v. The process is seamless and does not require manual intervention once executed.
5.	Data Transformation :
    i. The fetched data is saved to a CSV file using Python's csv module.
    ii. The file includes columns for Country Name, Capital, and Currency.
    iii. Missing fields (e.g., no capital or currency) are handled by substituting "N/A" to ensure data integrity.

How to Run the Script
1.	Install the required Python library:
    "pip install requests"
2.	Execute the script
3.	Output:
    i. A CSV file (countries.csv) will be generated containing data for all countries.
    ii. The script will log messages about the GraphQL and REST API interactions to the console.
    iii. Any errors encountered will also be logged.

Key Features
1.	Error Resilience:
     --->Handles common HTTP errors gracefully, ensuring the script continues to run without crashing.
2.	Automation:
    --->The workflow is fully automated, requiring minimal setup.
3.	Extensibility:
    --->The script is modular, allowing for easy addition of new features or endpoints.
4.	Data Backup:
    --->Saves fetched data to a CSV file for further analysis or backup.

Potential Enhancements
--> Use a configuration file for API endpoints and query settings.
--> Implement unit tests for each function.
--> Extend error handling for additional HTTP status codes.
--> Add command-line arguments for custom behavior.
This approach ensures a robust, scalable, and maintainable solution to the given problem.

