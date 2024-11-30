import sqlite3
from faker import Faker
from faker.providers import person, color, date_time, lorem, company
from random import randint as rd
from datetime import datetime

#conn = sqlite3.connect('C:/Users/Lenovo/DataGripProjects/gavno/identifier.sqlite')
conn = sqlite3.connect("C:/Users/Lenovo/Documents/GitHub/SYSC_site/db.sqlite3")
c = conn.cursor()


def Products():
    Faker.seed(141)
    f = Faker()
    f.add_provider(company)
    f.add_provider(lorem)

    for _ in range(10000):
        c.execute(
            "INSERT INTO Products (model, info) "
            "VALUES ('{0}', '{1}')".format( f.company(), f.text() ) )
    conn.commit()
    print("Products generated")


def Properties():
    Faker.seed(842)
    f = Faker()
    f.add_provider(color)

    for _ in range(100000):
        c.execute(
            "INSERT INTO Properties (prod_id, material, color_hex, price, stock_quantity, discount, size, avr_rating) "
            "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(
                rd(1, 10000),
                ["leather", "leatherette", "cloth", "rubber"][rd(0,3)],
                f.hex_color(),
                rd(1000, 20000) + rd(0,99) / 100.,
                rd(0,200),
                rd(0,100) / 100.,
                rd(10,50),
                rd(0,500) / 100.
            ))
    conn.commit()
    print("Properties generated")

def Users():
    Faker.seed(547)
    f = Faker()
    f.add_provider(person)

    for _ in range(200000):
        c.execute(
            "INSERT INTO Users (first_name, second_name, password, email, role) "
            "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(
                f.first_name(), f.last_name(), f.password(), f.email(), ["user", "moder"][rd(0,1)]
            ))
    conn.commit()
    print("Users generated")


def Popular():
    Faker.seed(442)
    f = Faker()

    for _ in range(200):
        c.execute(
            "INSERT INTO Popular (fav_id) "
            "VALUES ('{0}')".format(rd(1,10000)))
    conn.commit()
    print("Popular generated")


def Purchase():
    Faker.seed(100)
    f = Faker()
    f.add_provider(date_time)

    for _ in range(1000000):
        c.execute(
            "INSERT INTO Purchase (user_id, product_id, purchase_date, status) "
            "VALUES ('{0}', '{1}', '{2}', '{3}')".format(
                rd(1, 200000),
                rd(1, 10000),
                f.date_object(),
                ["Rejected", "In transit", "Delivered", "In stock"][rd(0,3)]
            ))
    conn.commit()
    print("Purchase generated")


def Reviews():
    Faker.seed(100)
    f = Faker()
    f.add_provider(lorem)

    for _ in range(2000000):
        c.execute(
            "INSERT INTO Reviews (product_id, user_id, rating, comment) "
            "VALUES ('{0}', '{1}', '{2}', '{3}')".format(
                rd(1, 10000),
                rd(1, 200000),
                rd(0,500) / 100.,
                f.text()
            ))
    conn.commit()
    print("Reviews generated")

def news_news():
    Faker.seed(100)
    f = Faker()
    f.add_provider(lorem)

    for i in range(500):
        c.execute(
            "INSERT INTO news_news (title, text, pub_date) "
            "VALUES ('{0}', '{1}', '{2}')".format(
                'a',
                '<p>a' + str(i) + '</p>',
                datetime.now().date(),
            ))
    conn.commit()


def news_event():
    Faker.seed(100)
    f = Faker()
    f.add_provider(lorem)

    for i in range(5000):
        c.execute(
            "INSERT INTO news_event (title, text, begin_date, end_date, pub_date) "
            "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(
                'a',
                '<p>a' + str(i) + '</p>',
                datetime.now().date(),
                datetime.now().date(),
                datetime.now().date(),
            ))
    conn.commit()


def info_grant():
    Faker.seed(100)
    f = Faker()
    f.add_provider(lorem)

    for i in range(5000):
        c.execute(
            "INSERT INTO info_grant (name, description, end_doc_date, end_result_date, criteria, link) "
            "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5})".format(
                'a',
                '<p>a' + str(i) + '</p>',
                datetime.now().date(),
                datetime.now().date(),
                'a',
                'gdgdgdg',
            ))
    conn.commit()


def info_institute():
    Faker.seed(100)
    f = Faker()
    f.add_provider(lorem)

    for i in range(5000):
        c.execute(
            "INSERT INTO info_institute (description, link, chairman, employees_count, scientist_count, smu_link, name) "
            "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(
                'a',
                'https://www.desmos.com/?lang=ru',
                'SUSCHTSCH',
                rd(1, 100),
                rd(1, 100),
                'www.desmos.com',
                'a' + str(i),
            ))
    conn.commit()


# Products()
# Properties()
# Users()
# Popular()
# Purchase()
# Reviews()
info_institute()

conn.close()