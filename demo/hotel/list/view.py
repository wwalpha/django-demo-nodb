from django.shortcuts import render
from django.views.generic import ListView

from .form import ExListForm
from demo.constants.Master import MEAL_CHOICE, SERVICE_CHOICE, RANK_CHOICE
from Django.settings import session, Hotel


class ExListView(ListView):
  form = ExListForm()
  context_object_name = 'hotelList'
  paginate_by = 5

  def get(self, request, *args, **kwargs):
    super().get(self, request, *args, **kwargs)

    context = self.get_context_data()
    context['form'] = self.form
    context['Const'] = {
        'SERVICE_CHOICE': SERVICE_CHOICE,
        'MEAL_CHOICE': MEAL_CHOICE,
        'RANK_CHOICE': RANK_CHOICE,
    }

    return self.render_to_response(context)

  def post(self, request, *args, **kwargs):
    super().get(self, request, *args, **kwargs)
    context = self.get_context_data()
    context['form'] = ExListForm(request.POST)

    return self.render_to_response(context)

  def get_queryset(self):
    # if self.request.method == 'GET':
    #   return session.query(Hotel).all()

    # form = ExListForm(self.request.POST).data.dict()
    # query = session.query(Hotel)

    # if form.get('name'):
    #   query = query.filter(Hotel.name == form.get('name'))
    # if form.get('address'):
    #   query = query.filter(Hotel.address == form.get('address'))
    # if form.get('stars'):
    #   query = query.filter(Hotel.stars == form.get('stars'))
    # if form.get('meal'):
    #   query = query.filter(Hotel.meal == form.get('meal'))
    # if form.get('service'):
    #   query = query.filter(Hotel.service == form.get('service'))

    # query.order_by(Hotel.id)
    return []
    # return query.all()
