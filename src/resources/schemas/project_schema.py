
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


