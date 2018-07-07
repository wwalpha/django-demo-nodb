from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse
from django.http import HttpResponseRedirect

from .form import ExEditForm
from Django.settings import session, Hotel


class ExEditView(FormView):
  mode = 'create'
  form_class = ExEditForm
  success_url = 'list'

  def get(self, request, *args, **kwargs):
    # パス等からデータ取得
    context = self.get_context_data(**kwargs)

    # 登録以外の場合、データ検索
    if self.mode != 'create':
      # パスのホテルIDをセッションに保存する
      request.session['hotel_id'] = context['hotel_id']

      hotel = session.query(Hotel).filter(Hotel.id == context['hotel_id']).first()
      # 検索結果画面に反映
      context['form'] = ExEditForm(initial=hotel.__dict__)

    context.update({
        'mode': self.mode,
    })

    return self.render_to_response(context)

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    formData = context['form'].data.dict()

    if self.mode == 'delete':
      self.delete()

    if self.mode == 'create':
      self.insert(formData)

    if self.mode == 'update':
      self.update(formData)

    return HttpResponseRedirect(reverse('list'))

  def insert(self, form):
    # 登録
    hotel = Hotel(
        name=form.get('name'),
        address=form.get('address'),
        meal=form.get('meal'),
        stars=form.get('stars'),
        service=form.get('service')
    )

    session.add(hotel)
    session.flush()

  def update(self, form):
    # 更新
    hotel_id = self.request.session['hotel_id']
    hotel = session.query(Hotel).filter(Hotel.id == hotel_id).first()

    hotel.name = form.get('name')
    hotel.address = form.get('address')
    hotel.meal = form.get('meal')
    hotel.stars = form.get('stars')
    hotel.service = form.get('service')

    session.commit()

  def delete(self):
    # 削除
    hotel_id = self.request.session['hotel_id']
    hotel = session.query(Hotel).filter(Hotel.id == hotel_id).first()

    session.delete(hotel)
    session.commit()

  def get_success_url(self):
    return reverse('cat:detail_cat', args=(self.kwargs['pk'],))

  def form_invalid(self, form, **kwargs):
    context = self.get_context_data(**kwargs)
    context['form'] = form
    # here you can add things like:
    context[show_results] = False
    return self.render_to_response(context)

  def form_valid(self, form, **kwargs):
    context = self.get_context_data(**kwargs)
    context['form'] = form
    # here you can add things like:
    context[show_results] = True
    return self.render_to_response(context)
