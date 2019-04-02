from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class Title:
    """
Part of `SearchResponse`.

:var str bid:
:var str isbn:
:var str title_name:
:var str author:
:var str publish_year:
:var str media_code:
:var str media_desc:

Example `Title`::

    Title(
        bid='203125808',
        isbn='1328915336 (paperback)',
        title_name='Beren and Lúthien / by  J.R.R. Tolkien ; edited by Christopher Tolkien ; with illustrations by  Alan Lee.',
        author='Tolkien, J. R. R. (John Ronald Reuel), 1892-1973',
        publish_year='2018',
        media_code='BK',
        media_desc='Books'
    )

    """
    bid: str
    isbn: str
    title_name: str
    author: str
    publish_year: str
    media_code: str
    media_desc: str


@dataclass
class SearchResponse:
    """
Returned by `Client.search`.

:var str status:
:var str message:
:var Optional[str] error_message:
:var Optional[int] total_records:
:var Optional[int] next_record_position:
:var Optional[str] set_id:
:var Optional[Iterable[Title]] titles:

Example `SearchResponse`::

    SearchResponse(
        status='OK',
        message='Operation completed successfully',
        error_message=None,
        total_records=52,
        next_record_position=4,
        set_id='PGE3676',
        titles=tuple([
            Title(
                bid='203125808',
                isbn='1328915336 (paperback)',
                title_name='Beren and Lúthien / by  J.R.R. Tolkien ; edited by Christopher Tolkien ; with illustrations by  Alan Lee.',
                author='Tolkien, J. R. R. (John Ronald Reuel), 1892-1973',
                publish_year='2018',
                media_code='BK',
                media_desc='Books'
            ),
            Title(
                bid='204576140',
                isbn='9780008214210 (electronic bk)',
                title_name='Beren and l℗♭©ʻthien [electronic resource]. J. R. R Tolkien.',
                author='Tolkien, J. R. R.',
                publish_year='2017',
                media_code='BK',
                media_desc='Books'
            )
        ])
    )

    """
    status: str
    message: str
    error_message: Optional[str]
    total_records: Optional[int]
    next_record_position: Optional[int]
    set_id: Optional[str]
    titles: Optional[Iterable[Title]]


@dataclass
class TitleDetail:
    """
Part of `GetTitleDetailsResponse`.

:var str bid:
:var str title_name:
:var str author:
:var str other_authors:
:var Optional[str] publisher:
:var str physical_desc:
:var Iterable[str] subjects:
:var str summary:
:var str notes:
:var str isbn:
:var Optional[str] issn:
:var Optional[str] n_title_name:
:var Optional[str] n_author:
:var Optional[str] n_publisher:

Example `TitleDetail`::

    TitleDetail(
        bid='203125808',
        title_name='Beren and Lúthien / by  J.R.R. Tolkien ; edited by Christopher Tolkien ; with illustrations by  Alan Lee.',
        author='Tolkien, J. R. R.',
        other_authors='Tolkien, J. R. R. (John Ronald Reuel), 1892-1973|Tolkien, Christopher|Lee, Alan',
        publisher=None,
        physical_desc='288 pages (pages numbered 8-288) :chiefly color illustrations ;21 cm',
        subjects=(
            'Middle Earth (Imaginary place) Fiction',
            'Elves Fiction',
            'Fantasy fiction'
        ),
        summary="The epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover.",
        notes="First published by Harper Collins Publishers 2017.Includes abstractsThe epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover.",
        isbn='1328915336 (paperback)',
        issn=None,
        n_title_name=None,
        n_author=None,
        n_publisher=None
    )

    """
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
    """
Returned by `Client.get_title_details`.

:var str status:
:var str message:
:var Optional[str] error_message:
:var Optional[TitleDetail] title_detail:

Example `GetTitleDetailsResponse`::

    GetTitleDetailsResponse(
        status='OK',
        message='Operation completed successfully',
        error_message=None,
        title_detail=TitleDetail(
            bid='203125808',
            title_name='Beren and Lúthien / by  J.R.R. Tolkien ; edited by Christopher Tolkien ; with illustrations by  Alan Lee.',
            author='Tolkien, J. R. R.',
            other_authors='Tolkien, J. R. R. (John Ronald Reuel), 1892-1973|Tolkien, Christopher|Lee, Alan',
            publisher=None,
            physical_desc='288 pages (pages numbered 8-288) :chiefly color illustrations ;21 cm',
            subjects=(
                'Middle Earth (Imaginary place) Fiction',
                'Elves Fiction',
                'Fantasy fiction'
            ),
            summary="The epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover.",
            notes="First published by Harper Collins Publishers 2017.Includes abstractsThe epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover.",
            isbn='1328915336 (paperback)',
            issn=None,
            n_title_name=None,
            n_author=None,
            n_publisher=None
        )
    )

    """
    status: str
    message: str
    error_message: Optional[str]
    title_detail: Optional[TitleDetail]


@dataclass
class Item:
    """
Part of `GetAvailabilityInfoResponse`.

:var str item_no:
:var str branch_id:
:var str branch_name:
:var str location_code:
:var str location_desc:
:var str call_number:
:var str status_code:
:var str status_desc:
:var Optional[str] media_code:
:var str media_desc:
:var str status_date:
:var Optional[str] due_date:
:var Optional[str] cluster_name:
:var Optional[str] category_name:
:var Optional[str] collection_code:
:var Optional[str] collection_min_age_limit:

Example `Item`::

    Item(
        item_no='B33315118C',
        branch_id='BBPL',
        branch_name='Bukit Batok Public Library',
        location_code='____',
        location_desc='Adult Lending',
        call_number='English      TOL -[FN]',
        status_code='C',
        status_desc='On Loan',
        media_code=None,
        media_desc='Book',
        status_date='08/11/2018',
        due_date='08/11/2018',
        cluster_name=None,
        category_name=None,
        collection_code=None,
        collection_min_age_limit=None
    )

    """
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
    """
Returned by `Client.get_availability_info`.

:var str status:
:var str message:
:var Optional[str] error_message:
:var Optional[int] next_record_position:
:var Optional[str] set_id:
:var Optional[Iterable[Item]] items:

Example `GetAvailabilityInfoResponse`::

    GetAvailabilityInfoResponse(
        status='OK',
        message='Operation completed successfully',
        error_message=None,
        next_record_position=2,
        set_id='3709',
        items=tuple([
            Item(
                item_no='B33315114J',
                branch_id='AMKPL',
                branch_name='Ang Mo Kio Public Library',
                location_code='____',
                location_desc='Adult Lending',
                call_number='English      TOL -[FN]',
                status_code='S',
                status_desc='Not On Loan',
                media_code=None,
                media_desc='Book',
                status_date='06/09/2018',
                due_date=None,
                cluster_name=None,
                category_name=None,
                collection_code=None,
                collection_min_age_limit=None
            ),
            Item(
                item_no='B33315118C',
                branch_id='BBPL',
                branch_name='Bukit Batok Public Library',
                location_code='____',
                location_desc='Adult Lending',
                call_number='English      TOL -[FN]',
                status_code='C',
                status_desc='On Loan',
                media_code=None,
                media_desc='Book',
                status_date='08/11/2018',
                due_date='08/11/2018',
                cluster_name=None,
                category_name=None,
                collection_code=None,
                collection_min_age_limit=None
            )
        ])
    )

    """
    status: str
    message: str
    error_message: Optional[str]
    next_record_position: Optional[int]
    set_id: Optional[str]
    items: Optional[Iterable[Item]]
