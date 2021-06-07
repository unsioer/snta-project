from django.shortcuts import render
from .models import HubeiProvinceCases, HubeiCityCases

areas = [
    '武汉', '襄阳', '咸宁', '神农架林区', '恩施州', '荆州', '鄂州', '黄石', '天门', '潜江', '随州',
    '十堰', '仙桃', '荆门', '宜昌', '孝感', '黄冈'
]
sources = [
    '武汉', '襄阳', '咸宁', '神农架林区', '监狱系统', '恩施州', '荆州', '鄂州', '黄石', '天门', '潜江',
    '随州', '待明确地区', '十堰', '仙桃', '荆门', '宜昌', '孝感', '黄冈'
]

# Create your views here.
def showDXY(request):
    hubeiCases = HubeiProvinceCases.objects.all()
    return render(
        request, 'dxy.html', {
            'dxyroot':
            True,
            'province_confirmCount': [[
                str(c.year) + '-' + str(c.month) + '-' + str(c.day),
                c.confirmCount
            ] for c in hubeiCases][::-1],
            'province_curedCount': [[
                str(c.year) + '-' + str(c.month) + '-' + str(c.day),
                c.curedCount
            ] for c in hubeiCases][::-1],
            'province_deadCount': [[
                str(c.year) + '-' + str(c.month) + '-' + str(c.day),
                c.deadCount
            ] for c in hubeiCases][::-1],
            'data':
            hubeiCases
        })


def showDXYCities(request):
    city = request.POST.get('city')
    piedate = request.POST.get('piedate')
    if city not in areas:
        city = '武汉'

    cityCases = HubeiCityCases.objects.filter(cityName=city)

    year = month = day = 0
    try:
        l = piedate.split('-')
        year = int(l[0])
        month = int(l[1])
        day = int(l[2])
    except:
        year = 2020
        month = 1
        day = 30
        piedate = '2020-01-30'
    piedatecases = HubeiCityCases.objects.filter(year=year,
                                                 month=month,
                                                 day=day)
    print(piedatecases)


    available_dates = HubeiCityCases.objects.values('year', 'month',
                                                    'day').distinct()
    available_dates = [
        str(d['year']) + '-' + '%02d' % d['month'] + '-' + '%02d' % d['day']
        for d in available_dates
    ]

    return render(
        request, 'dxy-cities.html', {
            'dxycities': True,
            'available_dates': available_dates,
            'curpiedate': piedate,
            'piedatecases': piedatecases,
            'available_cities': areas,
            'city': city,
            'city_confirmCount': [[
                str(c.year) + '-' + str(c.month) + '-' + str(c.day),
                c.confirmCount
            ] for c in cityCases][::-1],
            'city_curedCount': [[
                str(c.year) + '-' + str(c.month) + '-' + str(c.day),
                c.curedCount
            ] for c in cityCases][::-1],
            'city_deadCount': [[
                str(c.year) + '-' + str(c.month) + '-' + str(c.day),
                c.deadCount
            ] for c in cityCases][::-1],
        })


def showDXYClass(request):
    

    areas_ = ['湖北全省']
    areas_.extend(sources)
    return render(
        request, 'dxy-class.html', {
            'dxypca': True,
            'areas': [{
                'id': areas_.index(a),
                'name': a
            } for a in areas_]
        })
