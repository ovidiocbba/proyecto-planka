
SCHEMA_INPUT_CREATE_PROJECT = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "name",
    "description"
  ]
}



SCHEMA_OUTPUT_CREATE_PROJECT = {
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
        "name": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "backgroundType": {},
        "backgroundGradient": {},
        "isHidden": {
          "type": "boolean"
        },
        "ownerProjectManagerId": {},
        "backgroundImageId": {}
      },
      "required": [
        "id",
        "createdAt",
        "updatedAt",
        "name",
        "description",
        "backgroundType",
        "backgroundGradient",
        "isHidden",
        "ownerProjectManagerId",
        "backgroundImageId"
      ]
    },
    "included": {
      "type": "object",
      "properties": {
        "projectManagers": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "createdAt": {
                "type": "string"
              },
              "updatedAt": {},
              "projectId": {
                "type": "string"
              },
              "userId": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "createdAt",
              "updatedAt",
              "projectId",
              "userId"
            ]
          }
        }
      },
      "required": [
        "projectManagers"
      ]
    }
  },
  "required": [
    "item",
    "included"
  ]
}



SCHEMA_PROJECT = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "createdAt": {"type": ["string", "null"]},
        "updatedAt": {"type": ["string", "null"]},
        "name": {"type": "string"},
        "description": {"type": ["string", "null"]},
        "backgroundType": {"type": ["string", "null"]},
        "backgroundGradient": {"type": ["string", "null"]},
        "isHidden": {"type": "boolean"},
        "ownerProjectManagerId": {"type": ["string", "null"]},
        "backgroundImageId": {"type": ["string", "null"]},
        "isFavorite": {"type": "boolean"}
    },
    "required": ["id", "name", "isHidden", "isFavorite"]
}

SCHEMA_OUTPUT_GET_PROJECTS = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": SCHEMA_PROJECT
        },
        "included": {
            "type": "object",
            "properties": {
                "projectManagers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "projectId": {"type": "string"},
                            "userId": {"type": "string"}
                        },
                        "required": ["id", "projectId", "userId"]
                    }
                }
            },
            "required": ["projectManagers"]
        }
    },
    "required": ["items", "included"]
}


SCHEMA_BOARD_OUTPUT ={
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
        "position": {
          "type": "number"
        },
        "name": {
          "type": "string"
        },
        "defaultView": {
          "type": "string"
        },
        "defaultCardType": {
          "type": "string"
        },
        "limitCardTypesToDefaultOne": {
          "type": "boolean"
        },
        "alwaysDisplayCardCreator": {
          "type": "boolean"
        },
        "projectId": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "createdAt",
        "updatedAt",
        "position",
        "name",
        "defaultView",
        "defaultCardType",
        "limitCardTypesToDefaultOne",
        "alwaysDisplayCardCreator",
        "projectId"
      ]
    },
    "included": {
      "type": "object",
      "properties": {
        "boardMemberships": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "createdAt": {
                "type": "string"
              },
              "updatedAt": {},
              "role": {
                "type": "string"
              },
              "canComment": {},
              "projectId": {
                "type": "string"
              },
              "boardId": {
                "type": "string"
              },
              "userId": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "createdAt",
              "updatedAt",
              "role",
              "canComment",
              "projectId",
              "boardId",
              "userId"
            ]
          }
        }
      },
      "required": [
        "boardMemberships"
      ]
    }
  },
  "required": [
    "item",
    "included"
  ]
}

SCHEMA_BOARD_OUTPUT2 = {
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
        "position": {
          "type": "number"
        },
        "name": {
          "type": "string"
        },
        "defaultView": {
          "type": "string"
        },
        "defaultCardType": {
          "type": "string"
        },
        "limitCardTypesToDefaultOne": {
          "type": "boolean"
        },
        "alwaysDisplayCardCreator": {
          "type": "boolean"
        },
        "projectId": {
          "type": "string"
        },
        "isSubscribed": {
          "type": "boolean"
        }
      },
      "required": [
        "id",
        "createdAt",
        "updatedAt",
        "position",
        "name",
        "defaultView",
        "defaultCardType",
        "limitCardTypesToDefaultOne",
        "alwaysDisplayCardCreator",
        "projectId",
        "isSubscribed"
      ]
    },
    "included": {
      "type": "object",
      "properties": {
        "boardMemberships": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "createdAt": {
                "type": "string"
              },
              "updatedAt": {},
              "role": {
                "type": "string"
              },
              "canComment": {},
              "projectId": {
                "type": "string"
              },
              "boardId": {
                "type": "string"
              },
              "userId": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "createdAt",
              "updatedAt",
              "role",
              "canComment",
              "projectId",
              "boardId",
              "userId"
            ]
          }
        },
        "labels": {
          "type": "array",
          "items": {}
        },
        "lists": {
          "type": "array",
          "items": {
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
              "position": {},
              "name": {},
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
        "cards": {
          "type": "array",
          "items": {}
        },
        "cardMemberships": {
          "type": "array",
          "items": {}
        },
        "cardLabels": {
          "type": "array",
          "items": {}
        },
        "taskLists": {
          "type": "array",
          "items": {}
        },
        "tasks": {
          "type": "array",
          "items": {}
        },
        "customFieldGroups": {
          "type": "array",
          "items": {}
        },
        "customFields": {
          "type": "array",
          "items": {}
        },
        "customFieldValues": {
          "type": "array",
          "items": {}
        },
        "users": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "email": {
                "type": "string"
              },
              "role": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              
              "isSsoUser": {
                "type": "boolean"
              },
              "isDeactivated": {
                "type": "boolean"
              },
              
              "isDefaultAdmin": {
                "type": "boolean"
              }
            },
            "required": [
                "id",
                "email",
                "role",
                "name",
                "isSsoUser",
                "isDeactivated",
                "isDefaultAdmin"
            ]
          }
        },
        "projects": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "createdAt": {
                "type": "string"
              },
              "updatedAt": {},
              "name": {
                "type": "string"
              },
              "description": {},
              "backgroundType": {},
              "backgroundGradient": {},
              "isHidden": {
                "type": "boolean"
              },
              "ownerProjectManagerId": {},
              "backgroundImageId": {}
            },
            "required": [
              "id",
              "createdAt",
              "updatedAt",
              "name",
              "description",
              "backgroundType",
              "backgroundGradient",
              "isHidden",
              "ownerProjectManagerId",
              "backgroundImageId"
            ]
          }
        },
        "attachments": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "boardMemberships",
        "labels",
        "lists",
        "cards",
        "cardMemberships",
        "cardLabels",
        "taskLists",
        "tasks",
        "customFieldGroups",
        "customFields",
        "customFieldValues",
        "users",
        "projects",
        "attachments"
      ]
    }
  },
  "required": [
    "item",
    "included"
  ]
}

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
                        "type": "object",
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


SCHEMA_CARD_PAYLOAD_INPUT = {
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
    },
    "description": {
      "type": "string"
    },
    "dueDate": {
      "type": "string"
    },
    "isDueCompleted": {
      "type": "boolean"
    },
    "stopwatch": {
      "type": "object",
      "properties": {
        "startedAt": {
          "type": "string"
        },
        "total": {
          "type": "number"
        }
      },
      "required": [
        "startedAt",
        "total"
      ]
    }
  },
  "required": [
    "type",
    "position",
    "name",
    "description",
    "dueDate",
    "isDueCompleted",
    "stopwatch"
  ]
}


SCHEMA_CARD_WITH_STOPWATCH = {
    "type": "object",
    "properties": {
        "item": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "stopwatch": {
                    "type": "object",
                    "properties": {
                        "total": {"type": "number"},
                        "startedAt": {"type": "string"}
                    },
                    "required": ["total", "startedAt"]
                }
            },
            "required": ["id", "stopwatch"]
        }
    },
    "required": ["item"]
}


SCHEMA_CARD_WITHOUT_STOPWATCH = {
    "type": "object",
    "properties": {
        "item": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "stopwatch": {"type": ["null"]}
            },
            "required": ["id", "stopwatch"]
        }
    },
    "required": ["item"]
}
