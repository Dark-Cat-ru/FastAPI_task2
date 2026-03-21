from infrastructure.sqlite.database import Base

from sqlalchemy.orm import Mapped, mapped_column

class Location(Base):
    __tablename__ = 'locations'

    name: Mapped[str] = mapped_column(
        min_length=3,
        max_length=20,
        nullable=False,
    )