from sqlalchemy import text


def test_add_student(db_session):
    db_session.execute(
        text("INSERT INTO students (name) VALUES (:name)"),
        {"name": "Test Add Student"},
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT name FROM students WHERE name = :name"),
        {"name": "Test Add Student"},
    ).scalar_one_or_none()

    assert result == "Test Add Student"


def test_update_student(db_session):
    db_session.execute(
        text("INSERT INTO students (name) VALUES (:name)"),
        {"name": "Test Update Before"},
    )
    db_session.commit()

    db_session.execute(
        text("UPDATE students SET name = :new WHERE name = :old"),
        {"new": "Test Update After", "old": "Test Update Before"},
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT name FROM students WHERE name = :name"),
        {"name": "Test Update After"},
    ).scalar_one_or_none()

    assert result == "Test Update After"


def test_delete_student(db_session):
    db_session.execute(
        text("INSERT INTO students (name) VALUES (:name)"),
        {"name": "Test Delete Student"},
    )
    db_session.commit()

    db_session.execute(
        text("DELETE FROM students WHERE name = :name"),
        {"name": "Test Delete Student"},
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT name FROM students WHERE name = :name"),
        {"name": "Test Delete Student"},
    ).scalar_one_or_none()

    assert result is None
