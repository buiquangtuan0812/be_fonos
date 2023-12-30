import json

file_path = 'db_library_books.json'

with open(file_path, 'r', encoding = 'utf-8') as f:
    data = json.load(f)
new_data = []
file_writer = 'insert.json'

for book in data:
    new_book = {}
    new_book['name'] = book['name']
    new_book['author'] = book['author']
    new_book['type'] = book['type']
    new_book['numberPage'] = book['numberPage']
    new_book['imgDes'] = book['imgDes']
    new_book['description'] = book['description']
    new_book['publisher'] = book['publishCompany']
    new_data.append(new_book)

with open(file_writer, 'w', encoding= 'utf-8') as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)