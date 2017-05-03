from django.shortcuts import render
from django.utils import timezone
from .models import Post
import requests
import json

#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})


def post_list(request):
    start_date='2017-04-24'
    end_date='2017-04-25'
    api_key='lB7TeFRAKQqCCWzYEyq2zYI3St4G27om5Ta3sR0M'
    params={'start_date':start_date, 'end_date': end_date, 'api_key':api_key}
    response = requests.get('https://api.nasa.gov/neo/rest/v1/feed', params=params)

    data = response.json()
    posts=[]
    asteroide=[]


    for j in data['near_earth_objects']:
        for i in range(len(data['near_earth_objects'][j])):
            asteroide=[]
            asteroide.append(j)
            asteroide.append(data['near_earth_objects'][j][i]['name'])
            asteroide.append(data['near_earth_objects'][j][i]['estimated_diameter']['kilometers']['estimated_diameter_max'])
            asteroide.append(data['near_earth_objects'][j][i]['estimated_diameter']['kilometers']['estimated_diameter_min'])
            asteroide.append(data['near_earth_objects'][j][i]['nasa_jpl_url'])
            asteroide.append(data['near_earth_objects'][j][i]['is_potentially_hazardous_asteroid'])
            posts.append([asteroide])


#        for j in range (0:2):


#        postsname[j].append()
#        postsname[j].append(data['near_earth_objects']['2017-04-24'][i]['estimated_diameter']['kilometers']['estimated_diameter_max'])
        #print ('Diametro máximo:', data['near_earth_objects']['2017-04-24'][i]['estimated_diameter']['kilometers']['estimated_diameter_max'], 'KM')
        #print ('Diametro mínimo:', data['near_earth_objects']['2017-04-24'][i]['estimated_diameter']['kilometers']['estimated_diameter_min'], 'KM')
        #print ('URL de datos:', data['near_earth_objects']['2017-04-24'][i]['nasa_jpl_url'])
        #print ('Potencialmente peligroso?:', data['near_earth_objects']['2017-04-24'][i]['is_potentially_hazardous_asteroid'])

    return render(request, 'blog/post_list.html',{'posts':posts})
