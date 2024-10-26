from worldOfSpeedApp.common.helpers import get_profile


class AddProfileToContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()

        return context


class ReadonlyMixin:
    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()

    def make_fields_readonly(self):

        for field_name, field in self.fields.items():
            if self.readonly_fields == '__all__' or field_name in self.readonly_fields:
                field.widget.attrs['readonly'] = True
