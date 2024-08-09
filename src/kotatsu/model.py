from dataclasses import dataclass


@dataclass
class Manga:
    id: int
    title: str
    alt_title: str
    url: str
    public_url: str
    rating: float
    nsfw: bool
    cover_url: str
    large_cover_url: str
    state: str
    author: str
    source: str
    tags: list[str] = ()  # // removed. tag has an individual entity


@dataclass
class FavoritesEntry:
    manga_id: int
    category_id: int
    sort_key: int
    created_at: int
    deleted_at: int
    manga: Manga


@dataclass
class Category:
    category_id: int
    created_at: int
    sort_key: int
    title: str
    order: str
    track: bool
    show_in_tab: bool


@dataclass
class HistoryRecord:
    manga_id: int
    created_at: int
    updated_at: int
    chapter_id: int
    page: int
    scroll: float
    percent: float
    manga: Manga
