from typing import List

from ramapi import get_endpoint
from models import ApiParameters, EventSchema
import os

from dotenv import load_dotenv

load_dotenv()

org = os.environ["EVENTBRITE_ORGANIZATION_ID"]

ENDPOINT = f"organizations/{org}/events/"


def get_all_paginated_events(
    endpoint: str, pages: int, params: ApiParameters
) -> List[EventSchema]:
    events = []
    for page in range(1, pages + 1):
        params.page = page
        print(f"Calling page {page}")
        response = get_endpoint(endpoint, params)
        print(response.pagination.continuation)
        events.extend(response.events)
    return events


if __name__ == "__main__":
    params = ApiParameters()
    response = get_endpoint(ENDPOINT, params)
    events = get_all_paginated_events(
        ENDPOINT,
        response.pagination.page_count,
        params,
    )
    print(f"Total recods: {len(events)}")
