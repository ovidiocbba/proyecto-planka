import pytest
import jsonschema


class AssertionSchemas:

    @staticmethod
    def validate_output_schema(response , schema_output):
        try:
            jsonschema.validate(instance=response.json(), schema= schema_output)
        except jsonschema.exceptions.ValidationError as error:
            pytest.fail(f"JSON schema doesn't match: {error}")


    @staticmethod
    def validate_list_output_schema(list , schema_output):
        try:
            jsonschema.validate(instance=list, schema= schema_output)
        except jsonschema.exceptions.ValidationError as error:
            pytest.fail(f"JSON schema doesn't match: {error}")
    


    @staticmethod
    def validate_input_schema(payload_input , payload_output):
        try:
            jsonschema.validate(payload_input, schema= payload_output)
        except jsonschema.exceptions.ValidationError as error:
            pytest.fail(f"JSON schema doesn't match: {error}")


    