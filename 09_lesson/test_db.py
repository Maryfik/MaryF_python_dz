from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:123@localhost:5432/NB"
db = create_engine(db_connection_string)


# Вывод списка
def test_db_conection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'subject'


# вывод списка уроков
def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['subject_id'] == 1
    assert row1['subject_title'] == "English"

    connection.close()


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("""INSERT INTO subject (\"subject_title\", \"subject_id\")
               VALUES (:new_name, :new_id)""")
    connection.execute(sql, {"new_name": "Medicina", "new_id": "16"})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("""UPDATE subject
       SET subject_title = :new_title
       WHERE subject_id = :subject_id""")
    connection.execute(sql, {"new_title": 'DB',
                             "subject_id": '16'})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
    connection.execute(sql, {"subject_id": '16'})

    transaction.commit()
    connection.close()
