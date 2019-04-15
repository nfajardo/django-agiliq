from django.urls import path
from .views import HomeNoteView, NoteListView, NoteCreateView

app_name = 'notes'

urlpatterns = [
    path('', HomeNoteView.as_view(), name='home_notes'),
    path('list-notes/', NoteListView.as_view(), name='listview_notes'),
    path('create-note/', NoteCreateView.as_view(), name='create_note'),
]
