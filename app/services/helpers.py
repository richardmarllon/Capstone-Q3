from flask import current_app


def add_in_db(data) -> None:
    session = get_current_session()
    session.add(data)
    session.commit()


def add_all_in_db(data) -> None:
    session = get_current_session()
    session.add_all(data)
    session.commit()


def delete_in_db(data) -> None:
    session = get_current_session()
    session.delete(data)
    session.commit()


def commit_current_session() -> None:
    session = current_app.db.session
    session.commit()


def get_current_session():
    return current_app.db.session()
