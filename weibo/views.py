from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger

labels = {
    'trump': '特朗普',
    'biden': '拜登',
    'us_election': '美国大选',
    'republican': '共和党',
    'Representatives': '众议院',
    'senate': '参议院',
    'pence': '彭斯',
    'Harris': '贺锦丽',
    'Democratic': '民主党',
    'congress': '美国国会',
}


# Create your views here.
def showWeibo(request):
    label = request.POST.get('label')
    cluster = request.POST.get('cluster')
    if label==None or label not in labels:
        label='trump'
    try:
        cluster=int(cluster)
    except:
        cluster=1
    if cluster<1 or cluster>5: cluster=1

    labelword=LabelWord.objects.filter(label=label)
    clusterword=ClusterWord.objects.filter(cluster=cluster)

    return render(request, 'weibo.html', {
        'weiboroot': True,
        'labels': [(k, labels[k]) for k in labels],
        'label':label,
        'labelcn':labels[label],
        'labelword': labelword,
        'cluster':str(cluster),
        'clusterword':clusterword,
    })

def showWeiboSentiment(request):
    daySentiment=DaySentiment.objects.all()
    monthSentiment=MonthSentiment.objects.all()
    return render(request, "weibo-sentiment.html", {
        'weibosentiment': True,
        'daysentiment':daySentiment,
        'monthsentiment':monthSentiment,
    })

def showWeiboOriginal(request):
    weibo = Weibo.objects.all()
    paginator = Paginator(weibo, 50)
    page = request.GET.get('page')
    data_list = []
    if page:
        data_list = paginator.page(page).object_list
    else:
        data_list = paginator.page(1).object_list
    try:
        page_object = paginator.page(page)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)
    return render(request, "weibo-original.html", {
        'weibooriginal': True,
        'page_object':page_object,
        'data_list':data_list
    })