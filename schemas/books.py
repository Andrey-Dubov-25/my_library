from pydantic import BaseModel, ConfigDict, Field

import constants


class BookBaseSchema(BaseModel):
    """Базовая модель для книги."""
    title: str = Field(
        ...,
        min_length=constants.TITLE_MIN_LENGTH,
        max_length=constants.TITLE_MAX_LENGTH,
        title='Название книги',
        description='Полное название книги'
    )
    author: str = Field(
        ...,
        min_length=constants.AUTHOR_MIN_LENGTH,
        max_length=constants.AUTHOR_MAX_LENGTH,
        title='Автор книги'
    )
    year: int = Field(
        ...,
        ge=constants.YEAR_MIN,
        le=constants.YEAR_MAX,
        title='Год написания'
    )
    pages: int = Field(..., gt=constants.PAGES_MIN, title='Количество страниц')
    is_read: bool = Field(default=False, title='Прочитана или нет')


class BookAddSchema(BookBaseSchema):
    """Модель для создания книги."""
    pass


class BookSchema(BookBaseSchema):
    """Модель для получения книги."""
    id: int

    model_config = ConfigDict(from_attributes=True)
