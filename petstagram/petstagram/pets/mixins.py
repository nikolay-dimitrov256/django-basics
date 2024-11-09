class DisabledFieldsMixin:
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for field_name, field in self.fields.items():
            if self.disabled_fields == '__all__' or field_name in self.disabled_fields:
                field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'
