from drf_spectacular.utils import extend_schema

user_create_schema = extend_schema(
    summary="Создание пользователя",
    description="Эндпоинт для создания нового пользователя.",
    tags=["Действия с пользователями"]
)

user_login_schema = extend_schema(
    summary="Залогинить пользователя",
    description="Эндпоинт для авторизации пользователя.",
    tags=["Действия с пользователями"]
)

user_logout_schema = extend_schema(
    summary="Разлогинить пользователя",
    description="Эндпоинт для разлогирования пользователя.",
    tags=["Действия с пользователями"]
)

user_stub_schema = extend_schema(
    summary="just stub заглушка для удобства",
    tags=["Действия с пользователями"]
)
