from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = "notes/note_listview.html"


class HomeNoteView(TemplateView):
    template_name = "notes/note_home.html"


class NoteCreateView(CreateView):
    model = Note
    fields = ['sender', 'recipient', 'msj', 'img']
    template_name = "notes/create_note.html"
    success_url = reverse_lazy('notes:home_notes')

