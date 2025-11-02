

PAYLOAD_PROJECT_CREATE = {
    "type": "private",
    "name": "Nuevo Proyecto",
    "description": "A project for developing new features..."
}

PAYLOAD_PROJECT_CREATE_NAME_EMPTY = {
    "type": "private",
    "name": "",
}

PAYLOAD_PROJECT_CREATE_NAME_NUMBER = {
    "type": "private",
    "name": 1234,
}

PAYLOAD_PROJECT_CREATE_TYPE_EMPTY = {
    "type": "private",
    "name": "",
}

PAYLOAD_PROJECT_CREATE_TYPE_SHARED = {
    "type": "shared",
    "name": "Mi Proyecto"
}


PAYLOAD_PROJECT_CREATE_TYPE_PRIVATE = {
    "type": "private",
    "name": "Mi Proyecto"
}

PAYLOAD_PROJECT_CREATE_TYPE_INVALID = {
    "type": "asd",
    "name": "Mi Proyecto"
}



PAYLOAD_BOARD_CREATE = {
    "position": 8,
    "name": "Proyecto Oficial"
}

PAYLOAD_BOARD_EMPTY_NAME={
    "position": 8,
    "name": ""
}

PAYLOAD_BOARD_NAME_VALUE_NUMBER={
    "position": 8,
    "name": 1234
}

PAYLOAD_BOARD_EMPTY_POSITION={
    "position": "",
    "name": "Proyecto Oficial"
}

PAYLOAD_BOARD_POSITION_NEGATIVE={
    "position": -8,
    "name": "Proyecto Oficial"
}

PAYLOAD_BOARD_POSITION_INVALID_TYPE={
    "position": "123",
    "name": "Proyecto Oficial"
}

PAYLOAD_BOARD_POSITION_LARGE={
    "position": 123456789456155554456465456465465456465456432435346456547567585786786786786786786753454634645754745,
    "name": "Proyecto Oficial"
}

PAYLOAD_BOARD_EMPTY ={
    "position": "",
    "name": ""
}

PAYLOAD_CREATE_LIST = {
    "type": "active",
    "position": 6553,
    "name": "IN PROGRESS"
}

PAYLOAD_CREATE_LIST_TYPE_ACTIVE = {
    "type": "active",
    "position": 6553,
    "name": "IN PROGRESS"
}

PAYLOAD_CREATE_LIST_TYPE_CLOSED = {
    "type": "closed",
    "position": "6553",
    "name": "En progreso"
}


PAYLOAD_CREATE_LIST_EMPTY_TYPE = {
    "type": "",
    "position": 6553,
    "name": "En progreso"
}

PAYLOAD_CREATE_LIST_INVALID_TYPE = {
    "type": "asd",
    "position": 6553,
    "name": "En progreso"
}



PAYLOAD_CREATE_LIST_EMPTY_POSITION = {
    "type": "active",
    "position": "",
    "name": "En progreso"
}

PAYLOAD_CREATE_LIST_INVALID_POSITION = {
    "type": "active",
    "position": "123",
    "name": "En progreso"
}

PAYLOAD_CREATE_LIST_POSITION_VALUE_NEGATIVE = {
    "type": "active",
    "position": -123,
    "name": "En progreso"
}

PAYLOAD_CREATE_LIST_POSITION_VALUE_EXCEEDS = {
    "type": "active",
    "position": 6546546546546546546546546546546546546546546546546546546546546546546546546465465465465465465465,
    "name": "En progreso"
}

PAYLOAD_CREATE_LIST_EMPTY_NAME = {
    "type": "active",
    "position": "6593",
    "name": ""
}

PAYLOAD_CREATE_LIST_INVALID_NAME = {
    "type": "active",
    "position": "6593",
    "name": 123
}

PAYLOAD_CREATE_CARD = {
    "type": "project",
    "position": 65536,
    "name": "Tercera Tarjeta",
    "description": "Mi description tercera",
    "dueDate": "2024-01-01T00:00:00.000Z",
    "isDueCompleted": False,
    "stopwatch": {
        "startedAt": "2024-01-01T00:00:00.000Z",
        "total": 3600
    }
}

PAYLOAD_CREATE_CARD_TYPE_PROJECT = {
  "type": "project",
  "position": 65536,
  "name": "Tercera Tarjeta"
}

PAYLOAD_CREATE_CARD_TYPE_STORY = {
  "type": "story",
  "position": 65536,
  "name": "Tercera Tarjeta"
}

PAYLOAD_CREATE_CARD_TYPE_EMPTY = {
  "type": "",
  "position": 65536,
  "name": "Tercera Tarjeta"
}

PAYLOAD_CREATE_CARD_TYPE_INVALID = {
  "type": "asd",
  "position": 65536,
  "name": "Tercera Tarjeta"
}




PAYLOAD_CREATE_CARD_POSITION_EMPTY = {
  "type": "project",
  "position": "",
  "name": "Tercera Tarjeta"
}

PAYLOAD_CREATE_CARD_POSITION_INVALID = {
  "type": "project",
  "position": "123",
  "name": "Tercera Tarjeta"
}

PAYLOAD_CREATE_CARD_POSITION_VALUE_NEGATIVE = {
  "type": "project",
  "position": -123,
  "name": "Tercera Tarjeta"
}

PAYLOAD_CREATE_CARD_POSITION_DIGITS_EXCEEDS = {
  "type": "project",
  "position": 45646546546546546546546546546546546546546546546546546546546565465465465465465465465465465456,
  "name": "Tercera Tarjeta"
}


PAYLOAD_CREATE_CARD_NAME_EMPTY = {
  "type": "project",
  "position": 65536,
  "name": ""
}
PAYLOAD_CREATE_CARD_NAME_INVALID = {
  "type": "project",
  "position": 65536,
  "name": 123
}
