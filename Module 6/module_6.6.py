# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 6.6 - Formative Test
# 6. Develop a program that defines a dictionary of book titles and their corresponding authors, then prints each book title and author.

books = {
    'Python Crash Course': 'Eric Matthes',
    'Clean Code': 'Robert C. Martin',
    'Deep Learning': 'Ian Goodfellow'
}

print('Books and Authors:')
for title, author in books.items():
    print(f'Title: {title}, Author: {author}')