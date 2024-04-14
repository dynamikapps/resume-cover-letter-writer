import requests


class IndeedAPIClient:
    def __init__(self, api_key, api_host):
        self.api_key = api_key
        self.api_host = api_host
        self.base_url = "https://indeed12.p.rapidapi.com"

    def search_jobs(self, query, location, page_id="1", fromage="3", radius="50"):
        url = f"{self.base_url}/jobs/search"
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host
        }
        querystring = {
            "query": query,
            "location": location,
            "page_id": page_id,
            "fromage": fromage,
            "radius": radius
        }
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error searching for jobs: {str(e)}")

    def get_job_details(self, job_id):
        url = f"{self.base_url}/job/{job_id}"
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error retrieving job details: {str(e)}")
