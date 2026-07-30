from contextlib import contextmanager


class DatabaseSessionManager:
    """Database session abstraction for production persistence."""

    def __init__(self, session_factory=None):
        self.session_factory = session_factory

    @contextmanager
    def session(self):
        session = self.session_factory() if self.session_factory else None
        try:
            yield session
            if session:
                session.commit()
        except Exception:
            if session:
                session.rollback()
            raise
        finally:
            if session:
                session.close()


session_manager = DatabaseSessionManager()
