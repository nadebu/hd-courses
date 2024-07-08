from dataclasses import dataclass
from typing import Dict, List, Literal, Optional, Any
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ["EVENTBRITE_API"]


@dataclass
class ApiPagination:
    object_count: int
    page_number: int
    page_size: int
    page_count: int
    continuation: Optional[str]
    has_more_items: bool


@dataclass
class EventSchema:
    name: Dict[str, str]
    description: Dict[str, str]
    url: str
    start: Dict[str, str]
    end: Dict[str, str]
    organization_id: int
    created: str
    changed: str
    published: str
    capacity: int
    capacity_is_custom: bool
    status: Literal["draft", "live", "started", "ended", "completed", "canceled"]
    currency: str
    listed: bool
    shareable: bool
    invite_only: bool
    online_event: bool
    show_remaining: bool
    tx_time_limit: int
    hide_start_date: bool
    hide_end_date: bool
    locale: str
    is_locked: bool
    privacy_setting: str
    is_series: bool
    is_series_parent: bool
    inventory_type: str
    is_reserved_seating: bool
    show_pick_a_seat: bool
    show_seatmap_thumbnail: bool
    show_colors_in_seatmap_thumbnail: bool
    source: str
    is_free: bool
    version: str
    summary: str
    facebook_event_id: int
    logo_id: int
    organizer_id: int
    venue_id: int
    category_id: int
    subcategory_id: int
    format_id: int
    id: int
    resource_uri: str
    is_externally_ticketed: bool
    series_id: int
    logo: Dict[Dict[Dict[str, int], Any], Dict[str, Any]]


@dataclass
class ApiResponse:
    pagination: ApiPagination
    events: List[EventSchema]

    def __post_init__(self):
        self.pagination = ApiPagination(**self.pagination)
        self.events = [EventSchema(**x) for x in self.events]


@dataclass
class ApiParameters:
    token: str = api_key
    continuation: Optional[str] = None
