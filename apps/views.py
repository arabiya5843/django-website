from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.models import User

class UserListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users'

    paginate_by = 2


class UserCreateView(CreateView):
    model = User
    fields = "__all__"
    template_name = 'users_add.html'
    success_url = reverse_lazy('users_list')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users_update.html'
    fields = "__all__"
    success_url = reverse_lazy("users_list")


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users_delete.html'
    success_url = reverse_lazy('users_list')

