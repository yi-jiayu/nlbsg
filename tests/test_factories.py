from nlbsg.types import SearchResponse, Title, GetTitleDetailsResponse, TitleDetail, Item, GetAvailabilityInfoResponse
from nlbsg._factories import search_response_factory, get_title_details_response_factory, \
    get_availability_info_response_factory


class TestSearchResponseFactory:
    def test_success(self):
        response = {
            'Status': 'OK',
            'Message': 'Operation completed successfully',
            'ErrorMessage': None,
            'TotalRecords': 52,
            'NextRecordPosition': 4,
            'SetId': 'PGE3676',
            'Titles': {
                'Title': [
                    {
                        'BID': '203125808',
                        'ISBN': '1328915336 (paperback)',
                        'TitleName': 'Beren and Lúthien / by  J.R.R. Tolkien ; edited by Christopher Tolkien ; with illustrations by  Alan Lee.',
                        'Author': 'Tolkien, J. R. R. (John Ronald Reuel), 1892-1973',
                        'PublishYear': '2018',
                        'MediaCode': 'BK',
                        'MediaDesc': 'Books'
                    },
                    {
                        'BID': '204576140',
                        'ISBN': '9780008214210 (electronic bk)',
                        'TitleName': 'Beren and l℗♭©ʻthien [electronic resource]. J. R. R Tolkien.',
                        'Author': 'Tolkien, J. R. R.',
                        'PublishYear': '2017',
                        'MediaCode': 'BK',
                        'MediaDesc': 'Books'
                    }
                ]
            }
        }
        actual = search_response_factory(response)
        expected = SearchResponse(
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
        assert actual == expected

    def test_error(self):
        response = {
            'Status': 'ERROR',
            'Message': 'System error encountered. Please contact the administrator',
            'ErrorMessage': 'Wrong API authorization key.',
            'TotalRecords': None,
            'NextRecordPosition': None,
            'SetId': None,
            'Titles': None
        }
        actual = search_response_factory(response)
        expected = SearchResponse(
            status='ERROR',
            message='System error encountered. Please contact the administrator',
            error_message='Wrong API authorization key.',
            total_records=None,
            next_record_position=None,
            set_id=None,
            titles=None
        )
        assert actual == expected


class TestGetTitleDetailsResponseFactory:
    def test_success(self):
        response = {
            'Status': 'OK',
            'Message': 'Operation completed successfully',
            'ErrorMessage': None,
            'TitleDetail': {
                'BID': '203125808',
                'TitleName': 'Beren and Lúthien / by  J.R.R. Tolkien ; edited by Christopher Tolkien ; with illustrations by  Alan Lee.',
                'Author': 'Tolkien, J. R. R.',
                'OtherAuthors': 'Tolkien, J. R. R. (John Ronald Reuel), 1892-1973|Tolkien, Christopher|Lee, Alan',
                'Publisher': None,
                'PhysicalDesc': '288 pages (pages numbered 8-288) :chiefly color illustrations ;21 cm',
                'Subjects': {
                    'Subject': [
                        'Middle Earth (Imaginary place) Fiction',
                        'Elves Fiction',
                        'Fantasy fiction'
                    ]
                },
                'Summary': "The epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover.",
                'Notes': "First published by Harper Collins Publishers 2017.Includes abstractsThe epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover.",
                'ISBN': '1328915336 (paperback)',
                'ISSN': None,
                'NTitleName': None,
                'NAuthor': None,
                'NPublisher': None
            }
        }
        actual = get_title_details_response_factory(response)
        expected = GetTitleDetailsResponse(
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
        assert actual == expected

    def test_error(self):
        response = {
            'Status': 'ERROR',
            'Message': 'System error encountered. Please contact the administrator',
            'ErrorMessage': 'Wrong API authorization key.',
            'TitleDetail': None
        }
        actual = get_title_details_response_factory(response)
        expected = GetTitleDetailsResponse(
            status='ERROR',
            message='System error encountered. Please contact the administrator',
            error_message='Wrong API authorization key.',
            title_detail=None
        )
        assert actual == expected


class TestGetAvailabilityInfoResponseFactory:
    def test_success(self):
        response = {
            'Status': 'OK',
            'Message': 'Operation completed successfully',
            'ErrorMessage': None,
            'NextRecordPosition': 2,
            'SetId': '3709',
            'Items': {
                'Item': [
                    {
                        'ItemNo': 'B33315114J',
                        'BranchID': 'AMKPL',
                        'BranchName': 'Ang Mo Kio Public Library',
                        'LocationCode': '____',
                        'LocationDesc': 'Adult Lending',
                        'CallNumber': 'English      TOL -[FN]',
                        'StatusCode': 'S',
                        'StatusDesc': 'Not On Loan',
                        'MediaCode': None,
                        'MediaDesc': 'Book',
                        'StatusDate': '06/09/2018',
                        'DueDate': None,
                        'ClusterName': None,
                        'CategoryName': None,
                        'CollectionCode': None,
                        'CollectionMinAgeLimit': None
                    },
                    {
                        'ItemNo': 'B33315118C',
                        'BranchID': 'BBPL',
                        'BranchName': 'Bukit Batok Public Library',
                        'LocationCode': '____',
                        'LocationDesc': 'Adult Lending',
                        'CallNumber': 'English      TOL -[FN]',
                        'StatusCode': 'C',
                        'StatusDesc': 'On Loan',
                        'MediaCode': None,
                        'MediaDesc': 'Book',
                        'StatusDate': '08/11/2018',
                        'DueDate': '08/11/2018',
                        'ClusterName': None,
                        'CategoryName': None,
                        'CollectionCode': None,
                        'CollectionMinAgeLimit': None
                    },
                ]
            }
        }
        actual = get_availability_info_response_factory(response)
        expected = GetAvailabilityInfoResponse(
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
            ]))
        assert actual == expected

    def test_error(self):
        response = {
            'Status': 'ERROR',
            'Message': 'System error encountered. Please contact the administrator',
            'ErrorMessage': 'Wrong API authorization key.',
            'NextRecordPosition': None,
            'SetId': None,
            'Items': None
        }
        actual = get_availability_info_response_factory(response)
        expected = GetAvailabilityInfoResponse(
            status='ERROR',
            message='System error encountered. Please contact the administrator',
            error_message='Wrong API authorization key.',
            next_record_position=None,
            set_id=None,
            items=None
        )
        assert actual == expected
