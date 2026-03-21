from infrastructure.sqlite.database import Base

from sqlalchemy.orm import Mapped, mapped_column

class Category(Base):
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        max_length=256
    )
    description: Mapped[str] = mapped_column(
        nullable=False,
        min_length=5,
    )
    slug: Mapped[int] = mapped_column(
        min_length=1,
        nullable=False,
        unique=True
    )