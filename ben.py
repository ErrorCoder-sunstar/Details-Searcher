import wikipedia as wiki
query=input("search your query: ")
print(query)
search = wiki.summary(query,sentences = 2)
print(search)