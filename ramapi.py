import requests
from dataclasses import asdict

from models import ApiResponse, ApiParameters

BASE_URL = "https://www.eventbriteapi.com/v3/"


def get_endpoint(endpoint: str, params: ApiParameters) -> ApiResponse:
    """Return `ApiResponse` from EventBrite `endpoint`"""
    response = requests.get(url=f"{BASE_URL}{endpoint}", params=asdict(params))
    response.raise_for_status()
    response = ApiResponse(**response.json())

    return response
