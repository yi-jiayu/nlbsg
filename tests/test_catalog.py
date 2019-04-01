from nlbsg.catalog import Client
from nlbsg.constants import Branch, Language, MediaCode, Sort


class TestClient:
    def test_search_request(self):
        actual = Client._search_request('api_key', 'decimal system', 'dewey', media_code='BK')
        expected = {
            'APIKey': 'api_key',
            'SearchItems': {
                'SearchItem': [
                    {
                        'SearchField': 'Keywords',
                        'SearchTerms': 'decimal system'
                    },
                    {
                        'SearchField': 'Author',
                        'SearchTerms': 'dewey'
                    },
                    {
                        'SearchField': 'MediaCode',
                        'SearchTerms': 'BK'
                    },
                ]
            },
            'Modifiers': {
                'SortSchema': None,
                'StartRecordPosition': 1,
                'MaximumRecords': 10,
                'SetId': None,
            }
        }
        assert actual == expected

    def test_search_request_with_constants(self):
        actual = Client._search_request('api_key', 'decimal system', 'dewey',
                                        branch=Branch.ANG_MO_KIO_PUBLIC_LIBRARY,
                                        media_code=MediaCode.BOOKS,
                                        language=Language.CHINESE,
                                        sort=Sort.PUBDATE)
        expected = {
            'APIKey': 'api_key',
            'SearchItems': {
                'SearchItem': [
                    {
                        'SearchField': 'Keywords',
                        'SearchTerms': 'decimal system'
                    },
                    {
                        'SearchField': 'Author',
                        'SearchTerms': 'dewey'
                    },
                    {
                        'SearchField': 'BranchID',
                        'SearchTerms': 'AMKPL'
                    },
                    {
                        'SearchField': 'MediaCode',
                        'SearchTerms': 'BK'
                    },
                    {
                        'SearchField': 'Language',
                        'SearchTerms': 'Chinese'
                    }
                ]
            },
            'Modifiers': {
                'SortSchema': 'PUBDATE',
                'StartRecordPosition': 1,
                'MaximumRecords': 10,
                'SetId': None,
            }
        }
        assert actual == expected

    def test_search_result(self):
        result = {
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
                    },
                    {
                        'BID': '203665768',
                        'ISBN': '9780007489954 (electronic bk)',
                        'TitleName': 'The fall of arthur [electronic resource]. J. R. R Tolkien.',
                        'Author': 'Tolkien, J. R. R.',
                        'PublishYear': '2013',
                        'MediaCode': 'BK',
                        'MediaDesc': 'Books'
                    }
                ]
            }
        }
        actual = Client._search_result(result)
        expected = {
            'Status': 'OK',
            'Message': 'Operation completed successfully',
            'ErrorMessage': None,
            'TotalRecords': 52,
            'NextRecordPosition': 4,
            'SetId': 'PGE3676',
            'Titles': [
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
                },
                {
                    'BID': '203665768',
                    'ISBN': '9780007489954 (electronic bk)',
                    'TitleName': 'The fall of arthur [electronic resource]. J. R. R Tolkien.',
                    'Author': 'Tolkien, J. R. R.',
                    'PublishYear': '2013',
                    'MediaCode': 'BK',
                    'MediaDesc': 'Books'
                }
            ]
        }
        assert actual == expected

    def test_search_result_when_error(self):
        result = {
            'Status': 'ERROR',
            'Message': 'System error encountered. Please contact the administrator',
            'ErrorMessage': 'Wrong API authorization key.',
            'TotalRecords': None,
            'NextRecordPosition': None,
            'SetId': None,
            'Titles': None
        }
        actual = Client._search_result(result)
        expected = result
        assert actual == expected

    def test_details(self):
        details = {
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
        actual = Client._details(details)
        expected = {
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
                'Subjects': [
                    'Middle Earth (Imaginary place) Fiction',
                    'Elves Fiction',
                    'Fantasy fiction'
                ],
                'Summary': "The epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover.",
                'Notes': "First published by Harper Collins Publishers 2017.Includes abstractsThe epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover.",
                'ISBN': '1328915336 (paperback)',
                'ISSN': None,
                'NTitleName': None,
                'NAuthor': None,
                'NPublisher': None
            }
        }
        assert actual == expected

    def test_details_when_error(self):
        details = {
            'Status': 'ERROR',
            'Message': 'System error encountered. Please contact the administrator',
            'ErrorMessage': 'Wrong API authorization key.',
            'TitleDetail': None
        }
        actual = Client._details(details)
        expected = details
        assert actual == expected

    def test_availability(self):
        availability = {
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
                    }
                ]
            }
        }
        actual = Client._availability(availability)
        expected = {
            'Status': 'OK',
            'Message': 'Operation completed successfully',
            'ErrorMessage': None,
            'NextRecordPosition': 2,
            'SetId': '3709',
            'Items': [
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
                }
            ]
        }
        assert actual == expected

    def test_availability_when_error(self):
        availability = {
            'Status': 'ERROR',
            'Message': 'System error encountered. Please contact the administrator',
            'ErrorMessage': 'Wrong API authorization key.',
            'NextRecordPosition': None,
            'SetId': None,
            'Items': None
        }
        actual = Client._availability(availability)
        expected = availability
        assert actual == expected
