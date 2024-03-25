from drf_spectacular.utils import extend_schema

user_list_docs = extend_schema(
    summary="Получение списка всех пользователей по емейлам с их номерами телефонов",
    description="API для получения списка всех пользователей с их номерами телефонов.",
    tags=["Действия с пользователями"]
)
organization_create_docs_get = extend_schema(
    summary="just stub заглушка для удобства",
    tags=["Организации"]
)
organization_create_docs_post = extend_schema(
    summary="Создание новой организации",
    description="API для создания новой организации.",
    tags=["Организации"]
)

event_create_docs_post = extend_schema(
    summary="Создание нового мероприятия",
    description="API для создания нового мероприятия. При создании мероприятия необходимо использовать sleep 60 секунд и данный запрос не должен быть блокирующим. ",
    tags=["Мероприятия"]
)

event_detail_docs = extend_schema(
    summary="Получение детальной информации о мероприятии",
    description="API для получения детальной информации о мероприятии с информацией о всех участвующих пользователях.",
    tags=["Мероприятия"]
)

event_list_docs = extend_schema(
    summary="Получение списка всех мероприятий с возможностью фильтрации, сортировки и поиска",
    description="API для получения списка всех мероприятий с возможностью фильтрации, сортировки и поиска.",
    tags=["Мероприятия"]
)
