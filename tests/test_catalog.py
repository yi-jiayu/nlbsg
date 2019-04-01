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
