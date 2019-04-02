from .types import (GetAvailabilityInfoResponse, GetTitleDetailsResponse, Item,
                    SearchResponse, Title, TitleDetail)


def search_response_factory(response):
    try:
        titles = []
        for title in response['Titles']['Title']:
            titles.append(Title(
                bid=title['BID'],
                isbn=title['ISBN'],
                title_name=title['TitleName'],
                author=title['Author'],
                publish_year=title['PublishYear'],
                media_code=title['MediaCode'],
                media_desc=title['MediaDesc']
            ))
    except TypeError:
        titles = None
    return SearchResponse(
        status=response['Status'],
        message=response['Message'],
        error_message=response['ErrorMessage'],
        total_records=response['TotalRecords'],
        next_record_position=response['NextRecordPosition'],
        set_id=response['SetId'],
        titles=titles and tuple(titles)
    )


def get_title_details_response_factory(response):
    try:
        title_detail = TitleDetail(
            bid=response['TitleDetail']['BID'],
            title_name=response['TitleDetail']['TitleName'],
            author=response['TitleDetail']['Author'],
            other_authors=response['TitleDetail']['OtherAuthors'],
            publisher=response['TitleDetail']['Publisher'],
            physical_desc=response['TitleDetail']['PhysicalDesc'],
            subjects=tuple(response['TitleDetail']['Subjects']['Subject']),
            summary=response['TitleDetail']['Summary'],
            notes=response['TitleDetail']['Notes'],
            isbn=response['TitleDetail']['ISBN'],
            issn=response['TitleDetail']['ISSN'],
            n_title_name=response['TitleDetail']['NTitleName'],
            n_author=response['TitleDetail']['NAuthor'],
            n_publisher=response['TitleDetail']['NPublisher'],
        )
    except TypeError:
        title_detail = None
    return GetTitleDetailsResponse(
        status=response['Status'],
        message=response['Message'],
        error_message=response['ErrorMessage'],
        title_detail=title_detail
    )


def get_availability_info_response_factory(response):
    try:
        items = []
        for item in response['Items']['Item']:
            items.append(Item(
                item_no=item['ItemNo'],
                branch_id=item['BranchID'],
                branch_name=item['BranchName'],
                location_code=item['LocationCode'],
                location_desc=item['LocationDesc'],
                call_number=item['CallNumber'],
                status_code=item['StatusCode'],
                status_desc=item['StatusDesc'],
                media_code=item['MediaCode'],
                media_desc=item['MediaDesc'],
                status_date=item['StatusDate'],
                due_date=item['DueDate'],
                cluster_name=item['ClusterName'],
                category_name=item['CategoryName'],
                collection_code=item['CollectionCode'],
                collection_min_age_limit=item['CollectionMinAgeLimit'],
            ))
    except TypeError:
        items = None
    return GetAvailabilityInfoResponse(
        status=response['Status'],
        message=response['Message'],
        error_message=response['ErrorMessage'],
        next_record_position=response['NextRecordPosition'],
        set_id=response['SetId'],
        items=items and tuple(items),
    )
