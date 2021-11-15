import json
from django.db.models import JSONField
from django.forms.fields import InvalidJSONInput


class ReadableJSONFormField(JSONField):
    def prepare_value(self, value):
        if isinstance(value, InvalidJSONInput):
            return value
        return json.dumps(value, ensure_ascii=False, indent=4)