class ReadonlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()

    def make_fields_readonly(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True