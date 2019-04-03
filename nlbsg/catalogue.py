from typing import Union

from zeep import Client as Zeep

from ._factories import (get_availability_info_response_factory,
                         get_title_details_response_factory,
                         search_response_factory)
from .constants import Branch, Language, MediaCode, Sort
from .types import (GetAvailabilityInfoResponse, GetTitleDetailsResponse,
                    SearchResponse)

PRODUCTION_URL = 'https://openweb.nlb.gov.sg/OWS/CatalogueService.svc?singleWsdl'
STAGING_URL = 'https://openweb-stg.nlb.gov.sg/OWS/CatalogueService.svc?singleWsdl'


class Client:
    def __init__(self, wsdl: str, api_key: str) -> None:
        self._zeep = Zeep(wsdl)
        self.api_key = api_key

    @staticmethod
    def _search_request(api_key, keywords=None, author=None, subject=None, title=None,
                        branch=None, media_code=None, language=None,
                        sort=None, start=1, limit=10, set_id=None):
        search_items = []
        if keywords:
            search_items.append({
                'SearchField': 'Keywords',
                'SearchTerms': keywords,
            })
        if author:
            search_items.append({
                'SearchField': 'Author',
                'SearchTerms': author,
            })
        if subject:
            search_items.append({
                'SearchField': 'Subject',
                'SearchTerms': subject
            })
        if title:
            search_items.append({
                'SearchField': 'Title',
                'SearchTerms': title
            })
        if branch:
            search_items.append({
                'SearchField': 'BranchID',
                'SearchTerms': branch.value if isinstance(branch, Branch) else branch,
            })
        if media_code:
            search_items.append({
                'SearchField': 'MediaCode',
                'SearchTerms': media_code.value if isinstance(media_code, MediaCode) else media_code,
            })
        if language:
            search_items.append({
                'SearchField': 'Language',
                'SearchTerms': language.value if isinstance(language, Language) else language,
            })
        return {
            'APIKey': api_key,
            'SearchItems': {
                'SearchItem': search_items,
            },
            'Modifiers': {
                'SortSchema': sort.value if isinstance(sort, Sort) else sort,
                'StartRecordPosition': start,
                'MaximumRecords': limit,
                'SetId': set_id,
            }
        }

    def search(self, keywords: str = None, author: str = None, subject: str = None, title: str = None,
               branch: Union[str, Branch] = None, media_code: Union[str, MediaCode] = None,
               language: Union[str, Language] = None,
               sort: Union[str, Sort] = None, start: int = 1, limit: int = 10, set_id: str = None) -> SearchResponse:
        """
        Searches content according to search criteria.

        :param keywords:
        :param author:
        :param subject:
        :param title:
        :param branch: Include only results from a particular branch. See `constants.Branch` for possible values.
        :param media_code: Include only results of a particular media type. See `constants.MediaCode` for possible
                           values.
        :param language: Include only results in a particular language. See `constants.Language` for possible values.
        :param sort: By default, results are sorted by published year in descending order. Use ``PUBDATE`` to sort in
                     ascending order instead, or ``TITLE`` to sort by title in ascending order, ignoring articles like
                     "a", "an" or "the". These values can also be found in `constants.Sort`.
        :param start: Start pointer for returned records.
        :param limit: Maximum records to be returned. This is capped at 100 records even if a number greater than 100
                      is specified.
        :param set_id: For use in pagination. This can be used with ``start`` to return the index position of
                       the next record in the backend system
        :return:
        """
        search_request = self._search_request(self.api_key, keywords, author, subject, title,
                                              branch, media_code, language,
                                              sort, start, limit, set_id)
        response = self._zeep.service.Search(**search_request)
        return search_response_factory(response)

    def get_title_details(self, bid: str = None, isbn: str = None) -> GetTitleDetailsResponse:
        """
        Get detailed information about an item. Either ``bid`` or ``isbn`` should be provided.

        :param bid:
        :param isbn:
        :return:
        """
        response = self._zeep.service.GetTitleDetails(APIKey=self.api_key,
                                                      BID=bid,
                                                      ISBN=isbn)
        return get_title_details_response_factory(response)

    def get_availability_info(self, bid: str = None, isbn: str = None,
                              sort: Union[str, Sort] = None, start: int = 1, limit: int = 10,
                              set_id: str = None) -> GetAvailabilityInfoResponse:
        """
        Check whether an item is available for loan. Either ``bid`` or ``isbn`` should be provided.

        :param bid:
        :param isbn:
        :param sort: By default, results are sorted by published year in descending order. Use ``PUBDATE`` to sort in
                     ascending order instead, or ``TITLE`` to sort by title in ascending order, ignoring articles like
                     "a", "an" or "the". These values can also be found in `constants.Sort`.
        :param start: Start pointer for returned records.
        :param limit: Maximum records to be returned. This is capped at 100 records even if a number greater than 100
                      is specified.
        :param set_id: For use in pagination. This can be used with ``start`` to return the index position of
                       the next record in the backend system
        :return:
        """
        response = self._zeep.service.GetAvailabilityInfo(APIKey=self.api_key,
                                                          BID=bid,
                                                          ISBN=isbn,
                                                          Modifiers={
                                                              'SortSchema': sort.value if isinstance(sort,
                                                                                                     Sort) else sort,
                                                              'StartRecordPosition': start,
                                                              'MaximumRecords': limit,
                                                              'SetId': set_id,
                                                          })
        return get_availability_info_response_factory(response)
