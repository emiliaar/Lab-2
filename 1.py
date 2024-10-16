#!!!!!
#В файле books-en.csv ошибка В 6452 строке: Publisher стоит на неправильном месте
#она должна выглядеть так:
#735201994;"Peterman Rides Again: Adventures Continue with the Real \J. Peterman\"" Through Life &amp";John Peterman;2000;" the Catalog Business""";1;0
#!!!!!

import json 
import csv


DATASET_PATH = 'books-en.csv'
OUT_PATH = 'out.json'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [col.strip() for col in title]
    return title


def get_object(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    res = next(reader)
    return res


def filter_author(dataset, title, author):
    filtered = []
    
    for line in dataset:
        obj = get_object(line, title)
        author_value = obj['Book-Author']
        year = obj['Year-Of-Publication']
        limit = 2016 <= int(year) <=2018
        if author_value == author and limit:
            filtered.append(obj)

    dataset.seek(0)
    return filtered


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        title = get_title(dataset)

        task1=0
        for line in dataset:
            obj = get_object(line, title)
            name = obj['Book-Title']
            if len(name) > 30:
                task1 += 1
        print('Задание 1:', task1)

        dataset.seek(0)
        next(dataset)
        author = str(input('Введите имя автора: '))
        task2 = filter_author(dataset, title, author)
        print('Задание 2', task2)

        dataset.seek(0)
        next(dataset)
        with open(OUT_PATH, 'w') as out:
            num = 1
            for line in dataset:
                if num <= 20:
                    obj = get_object(line, title)
                    author = obj['Book-Author']
                    name = obj['Book-Title']
                    year = obj['Year-Of-Publication']
                    out.write(f'{num}. {author} - {name} - {year}\n')
                    num += 1
                else:
                    break
        with open(OUT_PATH, 'r') as file:
            task3 = file.read()
            print(task3)

        print('Допзадание 1')
        izdatelstva = set()
        dataset.seek(0)
        next(dataset)
        for line in dataset:
                obj = get_object(line, title)
                izdatelstva.add(obj['Publisher'])
        print(izdatelstva)

        print('Допзадание 2')
        books = {}
        dataset.seek(0)
        next(dataset)
        for line in dataset:
                obj = get_object(line, title)
                certain_book = obj['Book-Title']
                if certain_book not in books:
                    books.update({certain_book : 1})
                else: books[certain_book] += 1
        books = dict(sorted(books.items(), key=lambda item: item[1]))
        print(dict(list(books.items())[-20:]))