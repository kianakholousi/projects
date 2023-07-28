

# search Engine


## Description

This project is a search engine data structure that has various functions including:
- Adding a document: gets a Wikipedia page URL and adds the first two paragraphs of the page to the document collection.
- Document search: gets a keyword and shows the list of articles containing it.
- Deleting a document: deletes a document by providing its URL.
- search version 2: searches for a term and gets the number of documents containing that term.
- Similarity: gets the IDs of two documents to calculate their similarity based on common words.
- Dominant word: finds the dominant words of a document by providing its ID.
- Popular word: finds the phrase that appears most frequently in all documents.

## Installation

To use this project,  need to have Python installed. Additionally,  need to install the following libraries:

- requests
- BeautifulSoup

 can install these libraries using pip:

```
pip install requests
pip install beautifulsoup4
```

## Usage

To use the search Engine, follow these steps:

1. Create an instance of the `searchEngine` class:

```python
se = searchEngine()
```

2. Add documents to the search engine using the `add_document` method. Pass the URL of the document as an argument:

```python
se.add_document('https://en.wikipedia.org/wiki/Koala')
```

3. search for documents containing specific keywords using the `search_document` method. Pass the keyword as an argument:

```python
se.search_document('animal')
```

4. Calculate the number of documents that contain a specific keyword using the `search2` method. Pass the keyword as an argument:

```python
se.search2('animal')
```

5. Calculate the similarity between two documents using the `similar` method. Pass the document IDs as arguments:

```python
se.similar('Koala', 'Tiger')
```

6. Find the most used word in a document using the `most_used_word` method. Pass the document ID as an argument:

```python
se.most_used_word('Koala')
```

7. Find the most popular word across all documents using the `most_popular_word` method:

```python
se.most_popular_word()
```

8. Remove a document from the search engine using the `remove_document` method. Pass the URL of the document as an argument:

```python
se.remove_document('https://en.wikipedia.org/wiki/Koala')
```

## Contributing

Contributions to this project are welcome. If  find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
