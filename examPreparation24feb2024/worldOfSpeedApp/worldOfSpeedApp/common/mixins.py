from worldOfSpeedApp.common.helpers import get_profile


class AddProfileToContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()

        return context
