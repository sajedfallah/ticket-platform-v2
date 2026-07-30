from contextlib import contextmanager


@contextmanager
def transaction_scope(session):
    """Provide commit/rollback handling for database operations."""
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
