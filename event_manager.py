import requests
import os
from dotenv import load_dotenv

load_dotenv()

EVENTBRIGHT_ENDPOINT = "https://www.eventbriteapi.com/v3/"
api_key = os.environ["EVENTBRITE_API"]


class EventManager:
    def __init__(self) -> None:
        self.org = os.environ["EVENTBRITE_ORGANIZATION_ID"]
        self.api_params = {"token": api_key}

    def get_org_events(self):
        # Get all of Healthy Dialogues events

        response = requests.get(
            url=f"{EVENTBRIGHT_ENDPOINT}/organizations/{self.org}/events/",
            params=self.api_params,
        )
        response.raise_for_status()
        data = response.json()
        print(data)

    def get_order_details(self):
        response = requests.get(
            url=f"{EVENTBRIGHT_ENDPOINT}/events/901668012297/orders/",
            params=self.api_params,
        )  # change this to be a loop
        response.raise_for_status()
        data = response.json()
        print(data)


data_manager = EventManager()

data_manager.get_order_details()
