[![Build Status](https://travis-ci.com/yi-jiayu/nlbsg.svg?branch=master)](https://travis-ci.com/yi-jiayu/nlbsg)
[![codecov](https://codecov.io/gh/yi-jiayu/nlbsg/branch/master/graph/badge.svg)](https://codecov.io/gh/yi-jiayu/nlbsg)
[![Documentation Status](https://readthedocs.org/projects/nlbsg/badge/?version=latest)](https://nlbsg.readthedocs.io/en/latest/?badge=latest)

# nlbsg
Python SDK for the [NLB Open Web Services](http://www.nlb.gov.sg/labs/technical-documentation/)

Currently supports the [Catalogue Service](http://www.nlb.gov.sg/labs/technical-documentation/#catalogue-service).

## Example usage

Creating a client:

```python
from nlbsg import Client

WSDL = 'https://openweb-stg.nlb.gov.sg/OWS/CatalogueService.svc?singleWsdl'
API_KEY = 'secret_api_key'

client = Client(WSDL, API_KEY)
```

Searching the catalogue:

```python
>>> from nlbsg import MediaCode
>>> results = client.search('lord of the rings', author='tolkien', media_code=MediaCode.BOOKS, limit=3)
>>> for title in results['Titles']:
...     print(f'Title: {title["TitleName"]}\nISBN: {title["ISBN"]}\nPublished: {title["PublishYear"]}\n')
...
Title: Beren and Lúthien / by  J.R.R. Tolkien ; edited by Christopher Tolkien ; with illustrations by  Alan Lee.
ISBN: 1328915336 (paperback)
Published: 2018

Title: Beren and l℗♭©ʻthien [electronic resource]. J. R. R Tolkien.
ISBN: 9780008214210 (electronic bk)
Published: 2017

Title: The fall of arthur [electronic resource]. J. R. R Tolkien.
ISBN: 9780007489954 (electronic bk)
Published: 2013
```

Getting title details:

```python
>>> details = client.get_title_details(isbn='1328915336')
>>> details['TitleDetail']['Summary']
"The epic tale of Beren and Lúthien became an essential element in the evolution of The Silmarillion, the myths and legends of J.R.R. Tolkien's First Age of the World. Always key to the story is the fate that shadowed their love: Beren was a mortal man, Lúthien an immortal Elf. Her father, a great Elvish lord, imposed on Beren an impossible task before he might wed Lúthien: to rob the greatest of all evil beings, Melkor, of a Silmaril.Painstakingly restored from Tolkien's manuscripts and presented for the first time as a continuous and standalone story, Beren and Lúthien reunites fans of The Hobbit and The Lord of the Rings with Elves and Men, along with the rich landscape and creatures unique to Tolkien's Middle-earth. Christopher Tolkien tells the story in his father's own words by giving its original form as well as prose and verse passages from later texts that illustrate the narrative as it changed. -- from back cover."
```

Getting title availability:

```python
>>> availability = client.get_availability_info(isbn='1328915336')
>>> for item in availability['Items']:
...     print(f'Branch: {item["BranchName"]}\nStatus: {item["StatusDesc"]}\n')
...
Branch: Ang Mo Kio Public Library
Status: Not On Loan

Branch: Bukit Batok Public Library
Status: On Loan

Branch: Bedok Public Library
Status: On Loan

Branch: Bishan Public Library
Status: Not On Loan

Branch: Bukit Panjang Public Library
Status: Not On Loan

Branch: Choa Chu Kang Public Library
Status: On Loan

Branch: Central Public Library
Status: Not On Loan

Branch: Clementi Public Library
Status: On Loan

Branch: Cheng San Public Library
Status: On Loan

Branch: Geylang East Public Library
Status: Not On Loan
```
