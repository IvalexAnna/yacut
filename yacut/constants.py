from string import ascii_letters, digits

MIN_LEN = 1
MAX_LEN_ORIGINAL = 256
MAX_LEN_SHORT = 16

STR_FOR_GEN_URL = ascii_letters + digits
PATTERN_FOR_CHECK_URL = r"^[A-Za-z0-9]{1,16}$"
REGEX_CUSTOM_ID = r"^[A-Za-z0-9]+$"

ERROR_NO_BODY = "Отсутствует тело запроса"
ERROR_ID_NOT_FOUND = "Указанный id не найден"
ERROR_URL_REQUIRED = '"url" является обязательным полем!'
ERROR_INVALID_CUSTOM_ID = "Указано недопустимое имя для короткой ссылки"
ERROR_CUSTOM_ID_EXISTS = "Предложенный вариант короткой ссылки уже существует."
MSG_REQUIRED = "Обязательное поле"
MSG_INVALID_URL = "Некорректная ссылка"
MSG_INVALID_CUSTOM_ID = (
    "Используются недопустимые символы (разрешены " "только A-Z, a-z, 0-9)."
)
