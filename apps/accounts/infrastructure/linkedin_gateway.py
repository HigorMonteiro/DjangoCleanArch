import requests

class LinkedInGateway:
    @staticmethod
    def fetch_user_info(linkedin_url):
        response = requests.get(f"https://api.linkedin.com/v2/me?url={linkedin_url}")

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error fetching LinkedIn info")
