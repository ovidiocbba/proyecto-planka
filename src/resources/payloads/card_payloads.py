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
  "position": "uno",
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
