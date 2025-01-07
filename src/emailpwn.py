import requests
import hashlib

def check_email_pwned():
    
    email = input("Enter your email: ")
    api_key = input("Enter your API KEY: ")
    
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'
    
    # header for request
    headers = {'User-Agent': 'Mozilla/5.0',
              'hibp-api-key': api_key,
              'api-version':  '3',
              'content-type': 'application/json'}
    
    try:
        # GET request
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            breaches = response.json()
            if breaches:
                print(f"Email address: {email} found on the leaks:")
                for breach in breaches:
                    print(f"- {breach['Name']} ---> {breach['Domain']}")
            else:
                print(f"Email address: {email} not found on the leaks")
        elif response.status_code == 404:
            print(f"Email address: {email} not found on the leaks")
        else:
            print(f"Request error: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la connexion à l'API: {e}")