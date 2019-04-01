from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class Title:
    bid: str
    isbn: str
    title_name: str
    author: str
    publish_year: str
    media_code: str
    media_desc: str


@dataclass
class SearchResponse:
    status: str
    message: str
    error_message: Optional[str]
    total_records: Optional[int]
    next_record_position: Optional[int]
    set_id: Optional[str]
    titles: Optional[Iterable[Title]]


@dataclass
class TitleDetail:
    bid: str
    title_name: str
    author: str
    other_authors: str
    publisher: Optional[str]
    physical_desc: str
    subjects: Iterable[str]
    summary: str
    notes: str
    isbn: str
    issn: Optional[str]
    n_title_name: Optional[str]
    n_author: Optional[str]
    n_publisher: Optional[str]


@dataclass
class GetTitleDetailsResponse:
    status: str
    message: str
    error_message: Optional[str]
    title_detail: Optional[TitleDetail]


@dataclass
class Item:
    item_no: str
    branch_id: str
    branch_name: str
    location_code: str
    location_desc: str
    call_number: str
    status_code: str
    status_desc: str
    media_code: Optional[str]
    media_desc: str
    status_date: str
    due_date: Optional[str]
    cluster_name: Optional[str]
    category_name: Optional[str]
    collection_code: Optional[str]
    collection_min_age_limit: Optional[str]


@dataclass
class GetAvailabilityInfoResponse:
    status: str
    message: str
    error_message: Optional[str]
    next_record_position: Optional[int]
    set_id: Optional[str]
    items: Optional[Iterable[Item]]
