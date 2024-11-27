from sqlalchemy.orm import Mapped, mapped_column, declared_attr, DeclarativeBase


class Base(DeclarativeBase):
    __abstaract__ = True
    ENDING_WORD = ["s", "ss", "x", "z", "ch", "sh"]

    @declared_attr.directive
    def __tablename__(cls) -> str:
        class_name = cls.__name__.lower()
        if any([class_name.endswith(end) for end in cls.ENDING_WORD]):
            return f"{class_name}es"
        elif class_name.endswith('y'):
            return f"{class_name[:-1]}ies"
        return f"{class_name}s"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)