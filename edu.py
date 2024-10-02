books_id = [50, 34, -1, -1, 2, 23, -1]
new_books_id = []

for i in range(10):
    id = int(input('Введите айди книги: '))
    books_id.append(id)

for i in books_id:
    if i != -1:
        new_books_id.append(i)
        
print(new_books_id)