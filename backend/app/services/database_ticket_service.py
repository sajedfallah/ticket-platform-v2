from sqlalchemy.orm import Session

from app.models.ticket import Ticket


class DatabaseTicketService:
    """Persistence layer for ticket operations backed by SQLAlchemy."""

    def create_ticket(
        self,
        db: Session,
        *,
        ticket_code: str,
        qr_code: str,
        order_id: int,
        payment_id: str,
        transaction_id: str,
    ) -> Ticket:
        ticket = Ticket(
            ticket_code=ticket_code,
            qr_code=qr_code,
            order_id=order_id,
            payment_id=payment_id,
            transaction_id=transaction_id,
            status="active",
        )
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

    def find_by_code(self, db: Session, ticket_code: str) -> Ticket | None:
        return (
            db.query(Ticket)
            .filter(Ticket.ticket_code == ticket_code)
            .first()
        )


 database_ticket_service = DatabaseTicketService()
