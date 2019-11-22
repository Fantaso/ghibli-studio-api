from django.views.generic import TemplateView

from utils.ghibli_api import GhibliApi as api


class MoviesHomeView(TemplateView):
    template_name = 'movies_home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # add movie list to context
        context.update(movies=api.get_film_list_with_cast())

        return self.render_to_response(context)
