class DisableFieldsMixin:
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.disabled_fields == '__all__' or field_name in self.disabled_fields:
                field.disabled = True
