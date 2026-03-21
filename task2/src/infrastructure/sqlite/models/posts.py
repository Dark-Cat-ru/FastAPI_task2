from infrastructure.sqlite.database import Base
from infrastructure.sqlite.models.users import User
from infrastructure.sqlite.models.locations import Location
from infrastructure.sqlite.models.categories import Category

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

class Post(Base):
    __tablename__ = 'posts'

    title: Mapped[str] = mapped_column(
        nullable=False,
        max_length=20,
        min_length=3,
    )
    text: Mapped[str] = mapped_column(
        min_length=5,
        nullable=False,
    )
    id: Mapped[int] = mapped_column(unique=True, nullable=False)
    pub_date: Mapped[datetime] = mapped_column()
    author: Mapped[User] = mapped_column(nullable=False)
    location: Mapped[Location] = mapped_column()
    category: Mapped[Category] = mapped_column(nullable=False)