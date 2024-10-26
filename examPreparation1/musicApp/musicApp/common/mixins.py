class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()

    def add_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder


class ReadonlyMixin:
    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()

    def make_fields_readonly(self):
        for field_name, field in self.fields.items():
            if self.readonly_fields == '__all__' or field_name in self.readonly_fields:
                field.widget.attrs['readonly'] = True
