import requests

def get_ip_info():

    ip_address = input("Enter IP address: ")

    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        data = response.json()

        ip = data.get("ip", "N/A")
        hostname = data.get("hostname", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country", "N/A")
        loc = data.get("loc", "N/A")
        org = data.get("org", "N/A")
        isp = data.get("isp", "N/A")

        print(f"IP Address: {ip}")
        print(f"Hostname: {hostname}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Location: {loc}")
        print(f"Organization: {org}")
        print(f"ISP: {isp}")

    except Exception as e:
        print(f"Error occurred: {e}")

