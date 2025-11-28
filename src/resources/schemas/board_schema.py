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