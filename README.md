# Foundation-API

This is an API around the Foundation Series of Isaac Asimov. It will provide data about the different books such as their
chapters, the characters and quotes within the books. 

## API implemented so far


| Endpoint | Response |
| --- | --- |
| /api/books/ | Get all books |
| /api/books/{id}/ | Get specific book |
| /api/chapters/ | Get all chapters | 
| /api/chapters/{id}/ | Get specific chapter |
| /api/books/{books.id}/chapters/ | Get all chapters of specific book |
| /api/characters/ | Get all characters |
| /api/characters/{id}/ | Get specific character |
| /api/books/{books.id}/characters/ | Get all characters of specific book |
| /api/quotes/ | Get all quotes |
| /api/quotes/{id}/ | Get specific quote |
| /api/books/{books.id}/quotes/ | Get quotes from specific book |
| /api/characters/{characters.id}/quotes/ | Get quotes from specific character | 

