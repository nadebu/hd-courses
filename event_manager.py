import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.eventbriteapi.com/v3/"
api_key = os.environ["EVENTBRITE_API"]


class EventManager:
    def __init__(self) -> None:
        self._org = os.environ["EVENTBRITE_ORGANIZATION_ID"]
        self._api_params = {"token": api_key}

    def get_org_events(self) -> dict:
        # Get all of Healthy Dialogues events

        response = requests.get(
            url=f"{BASE_URL}/organizations/{self._org}/events/",
            params=self._api_params,
        )
        response.raise_for_status()
        data = response.json()
        return data

    def get_order_details(self) -> dict:
        event_id = 901668012297  # done for testing purposes
        response = requests.get(
            url=f"{BASE_URL}/events/{event_id}/orders/",
            params=self._api_params,
        )  # change this to be a parameter after testing
        response.raise_for_status()
        data = response.json()
        return data

    def get_attendee_details(self) -> dict:
        event_id = 901668012297  # done for testing purposes
        response = requests.get(
            url=f"{BASE_URL}/events/{event_id}/attendees/",
            params=self._api_params,
        )  # change to become paramaterized after testing
        response.raise_for_status()
        attendee_data = response.json()
        return attendee_data


if __name__ == "__main__":
    # Used for testing
    data_manager = EventManager()
    print(data_manager.get_attendee_details())
