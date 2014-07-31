#from django.views.generic import TemplateView
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView

from braces.views import LoginRequiredMixin

from albums.models import Artist

#from albums.forms import ArtistForm


#class AboutView(TemplateView):
#    template_name = "base.html"

#class ArtistCreate(CreateView):
#    model = Artist
#    fields = ['name']

class ArtistActionMixin(object):


    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        msg = "Artist {0}!".format(self.action)
        messages.info(self.request, msg)
        return super(ArtistActionMixin, self).form_valid(form)
        
class ArtistCreateView(LoginRequiredMixin, ArtistActionMixin, CreateView):
    model = Artist
    action = "created"

class ArtistUpdateView(LoginRequiredMixin, ArtistActionMixin, UpdateView):
    model = Artist
    action = "updated"

class ArtistDetailView(DetailView):
    model = Artist

