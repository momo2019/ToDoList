import json
import time
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from ToDoList.models import Articles
from ToDoList.models import Lags
from ToDoList.models import ArticlesHasLags

class lag:
  # 获取所有标签
  def get_lags(request):
    if request.method=='GET':
      lags_list = list( Lags.objects.all().values() )
    return JsonResponse({'data':lags_list, 'msg': 'get success'}, safe=False)
  
  # 创建新标签
  @csrf_exempt
  def create_lag(request):
    if request.method == 'POST':
      data = json.loads(request.body)
      name = data['name']
      color = data['color']
      Lags.objects.create(name=name,color=color)
    lags_list = list( Lags.objects.all().values() )
    return JsonResponse({'data':lags_list, 'msg': 'create success'}, safe=False)

class article:
  # 获取日历上的日期的事件标签集合
  def get_calendar(request):
    if request.method == 'GET':
      first_unix = request.GET.get('first_unix')[:-5]
      unix_list = []
      response = {}
      for i in range(0,42):
        temp_unix = str(int(first_unix) + (i * 864)) + '00000'
        unix_list.append(temp_unix)
        response[temp_unix] = []
      articles = Articles.objects.filter(unix__in=unix_list)
      for article in articles:
        temp_article = []
        temp_unix = article.unix
        art_has_lags = ArticlesHasLags.objects.filter(id_art=article.id_art)
        for item in art_has_lags:
          temp_lag = {}
          temp_lag['id'] = item.id_lag.id_lag
          temp_lag['name'] = item.id_lag.name
          temp_lag['color'] = item.id_lag.color
          temp_article.append(temp_lag)
        response[temp_unix].append(temp_article)
    return JsonResponse({'msg': 'ok', 'data': response}, safe=False)
  
  # 获取日期的事件集合
  def get_article(request):
    if request.method == 'GET':
      unix = request.GET.get('unix')
      response = []
      articles = Articles.objects.filter(unix=unix)
      for article in articles:
        temp_article = {}
        temp_article['id'] = article.id_art
        temp_article['title'] = article.title
        temp_article['content'] = article.content
        temp_article['lags'] = []
        art_has_lags = ArticlesHasLags.objects.filter(id_art=article.id_art)
        for item in art_has_lags:
          temp_lag = {}
          temp_lag['name'] = item.id_lag.name
          temp_lag['color'] = item.id_lag.color
          temp_article['lags'].append(temp_lag)
        response.append(temp_article)
    return JsonResponse({'msg': 'ok', 'data': response}, safe=False)

  # 创建新事件
  @csrf_exempt
  def create_article(request):
    if request.method == 'POST':
      data = json.loads(request.body)
      title = data['title']
      content = data['content']
      lags = data['lags']
      unix = data['unix']
      rel_art = Articles.objects.create(title=title,content=content,unix=unix)
      addlist = []
      for i in lags:
        rel_lag = Lags.objects.get(id_lag=i)
        addlist.append(ArticlesHasLags(id_art=rel_art,id_lag=rel_lag))
      ArticlesHasLags.objects.bulk_create(addlist)
    return JsonResponse({'msg': 'create success'}, safe=False)

  # 删除事件
  @csrf_exempt
  def del_article(request):
    if request.method == 'POST':
      data = json.loads(request.body)
      id_art = data['id']
      ArticlesHasLags.objects.filter(id_art=id_art).delete()
      Articles.objects.filter(id_art=id_art).delete()
    return JsonResponse({'msg': 'delete success'}, safe=False)