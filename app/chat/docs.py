from chat.serializers import ChatRoomsSerializer
from drf_spectacular.utils import extend_schema

docs_for_chat_CRUD = extend_schema(
    description="CRUD по чатам ",
    summary='CRUD для чатов (создать удалить чат и тд)',
    responses={200: ChatRoomsSerializer(many=True)},
    tags=["Пользовательские чаты"]
)


entry_chat_schema = extend_schema(
            description="Поле для ввода данных для входа в определенный чат",
            summary=' перейти по урл (вставить в адресную строку) и ввести название чата в этом поле',
            responses={200: 'OK'},
            tags=["Пользовательские чаты"]
)

chat_schema = extend_schema(
            description="Сам чат",
            summary='окно чата',
            responses={200: 'OK'},
            tags=["Пользовательские чаты"]
)