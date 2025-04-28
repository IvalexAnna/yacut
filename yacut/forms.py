from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from yacut import constants


class URLForm(FlaskForm):
    """Форма для создания короткой ссылки."""

    original_link = URLField(
        "Длинная ссылка",
        validators=[
            Length(constants.MIN_LEN, constants.MAX_LEN_ORIGINAL),
            DataRequired(message=constants.MSG_REQUIRED),
            URL(require_tld=True, message=constants.MSG_INVALID_URL),
        ],
    )
    custom_id = URLField(
        "Ваш вариант короткой ссылки",
        validators=[
            Length(constants.MIN_LEN, constants.MAX_LEN_SHORT),
            Optional(),
            Regexp(
                regex=constants.REGEX_CUSTOM_ID,
                message=(constants.MSG_INVALID_CUSTOM_ID),
            ),
        ],
    )
    submit = SubmitField("Создать")
