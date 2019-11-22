from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from ghibil_studio_api.settings import CACHE_TTL
from utils.ghibli_api import GhibliApi as api


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class MoviesHomeView(TemplateView):
    template_name = 'movies_home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update(movies=api.get_film_list_with_cast())
        return self.render_to_response(context)
