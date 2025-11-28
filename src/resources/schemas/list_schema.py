SCHEMA_LIST_PAYLOAD_INPUT = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "position": {
      "type": "number"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "position",
    "name"
  ]
}

SCHEMA_CREATE_LIST_OUTPUT = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "item": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "createdAt": {
          "type": "string"
        },
        "updatedAt": {},
        "type": {
          "type": "string"
        },
        "position": {
          "type": "number"
        },
        "name": {
          "type": "string"
        },
        "color": {},
        "boardId": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "createdAt",
        "updatedAt",
        "type",
        "position",
        "name",
        "color",
        "boardId"
      ]
    }
  },
  "required": [
    "item"
  ]
}

SCHEMA_ITEM_LIST = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
        "updatedAt": {"type": ["string", "null"]},  # permite null
        "type": {"type": "string"},
        "position": {"type": "number"},
        "name": {"type": "string"},
        "color": {"type": ["string", "null"]},
        "boardId": {"type": "string"}
    },
    "required": ["id", "createdAt", "type", "position", "name", "boardId"]
}


SCHEMA_INCLUDED_LIST = {
    "type": "object",
    "properties": {
        "cards": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "createdAt": {"type": "string"},
                    "updatedAt": {"type": ["string", "null"]},
                    "type": {"type": "string"},
                    "position": {"type": "number"},
                    "name": {"type": "string"},
                    "description": {"type": ["string", "null"]},
                    "dueDate": {"type": ["string", "null"]},
                    "stopwatch": {
                         "type": ["object", "null"],
                        "properties": {
                            "total": {"type": "number"},
                            "startedAt": {"type": "string"}
                        },
                        "required": ["total", "startedAt"]
                    },
                    "commentsTotal": {"type": "number"},
                    "listChangedAt": {"type": ["string", "null"]},
                    "boardId": {"type": "string"},
                    "listId": {"type": "string"},
                    "creatorUserId": {"type": "string"},
                    "prevListId": {"type": ["string", "null"]},
                    "coverAttachmentId": {"type": ["string", "null"]},
                    "isSubscribed": {"type": "boolean"}
                },
                "required": ["id", "createdAt", "type", "name", "boardId"]
            }
        },
        "users": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "createdAt": {"type": "string"},
                    "updatedAt": {"type": ["string", "null"]},
                    "email": {"type": "string"},
                    "role": {"type": "string"},
                    "name": {"type": "string"},
                    "username": {"type": "string"},
                    "phone": {"type": ["string", "null"]},
                    "organization": {"type": ["string", "null"]},
                    "language": {"type": ["string", "null"]},
                    "avatar": {"type": ["string", "null"]},
                    "isSsoUser": {"type": "boolean"},
                    "isDeactivated": {"type": "boolean"},
                    "isDefaultAdmin": {"type": "boolean"}
                },
                "required": ["id", "email", "role", "name", "username"]
            }
        },
        # otras listas vacías
        "cardMemberships": {"type": "array"},
        "cardLabels": {"type": "array"},
        "taskLists": {"type": "array"},
        "tasks": {"type": "array"},
        "customFieldGroups": {"type": "array"},
        "customFields": {"type": "array"},
        "customFieldValues": {"type": "array"},
        "attachments": {"type": "array"}
    },
    "required": ["cards", "users"]
}