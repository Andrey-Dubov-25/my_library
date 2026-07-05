from pydantic import BaseModel, ConfigDict, Field


class BookBaseSchema(BaseModel):
    """Базовая модель для книги."""
    title: str = Field(
        ...,
        min_length=2,
        max_length=100,
        title='Название книги',
        description='Полное название книги'
    )
    author: str = Field(
        ..., min_length=2, max_length=100, title='Автор книги'
    )
    year: int = Field(..., title='Год написания')
    pages: int = Field(..., gt=10, title='Количество страниц')
    is_read: bool = Field(default=False, title='Прочитана или нет')


class BookAddSchema(BookBaseSchema):
    """Модель для создания книги."""
    pass


class BookSchema(BookBaseSchema):
    """Модель для получения книги."""
    id: int

    model_config = ConfigDict(from_attributes=True)
