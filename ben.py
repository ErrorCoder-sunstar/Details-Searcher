import wikipedia as wiki

query = input("Search your query: ")

try:
    result = wiki.summary(query, sentences=2)
    print(result)
except wiki.exceptions.DisambiguationError as e:
    print("Multiple results found. Try one of these:")
    print(e.options[:5])
except wiki.exceptions.PageError:
    print("No matching Wikipedia page found.")
