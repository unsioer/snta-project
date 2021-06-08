from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger

# Create your views here.
labels=['biden','trump','us election']

def showTwitter(request):
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

    return render(request, 'twitter.html', {
        'twitterroot': True,
        'labels': labels,
        'label':label,
        'labelword': labelword,
        'cluster':str(cluster),
        'clusterword':clusterword,
    })


def showTwitterSentiment(request):
    daySentiment=DaySentiment.objects.all()
    monthSentiment=MonthSentiment.objects.all()
    return render(request, "twitter-sentiment.html", {
        'twittersentiment': True,
        'daysentiment':daySentiment,
        'monthsentiment':monthSentiment,
    })


def showTwitterOriginal(request):
    tweet = Tweet.objects.all()
    paginator = Paginator(tweet, 50)
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
    return render(request, "twitter-original.html", {
        'twitteroriginal': True,
        'page_object':page_object,
        'data_list':data_list
    })