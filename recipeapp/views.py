from django.shortcuts import render, redirect
import requests
# Create your views here.
def index(request):
    url="https://dummyjson.com/recipes"
    response=requests.get(url)
    mydata=response.json()
    print(mydata['recipes'][0].keys())
    print(len(mydata['recipes']))
    # --------------------------------------
    # fetch tag
    response2=requests.get(f"{url}/tags")
    mydata2=response2.json()
    # response2=requests.get(url+"/tag/"+mealname)
    context={
        'recipedata':mydata['recipes'],
        'alltags':mydata2
    }
    return render(request,'index.html',context)


def recipedetails(request,rid):
    singledata=requests.get(f"https://dummyjson.com/recipes/{rid}").json()
    print(singledata['tags'][0])
    tagname=singledata['tags'][0]
    tagdata=requests.get(f"https://dummyjson.com/recipes/tag/{tagname}").json()
    context={
        'singledata':singledata,
        'tagdata':tagdata['recipes']
    }
    return render(request,'recipe.html',context)

def mealtype(request,mealname):
    mealdata=requests.get(f"https://dummyjson.com/recipes/meal-type/{mealname}").json()
    context = {
        'recipedata': mealdata['recipes'],
    }
    return render(request,'index.html',context)



def tagtype(request,tagname):
    tagdata=requests.get(f"https://dummyjson.com/recipes/tag/{tagname}").json()
    context = {
        'recipedata': tagdata['recipes'],
    }
    return render(request,'index.html',context)


def search(request):
    word=request.POST.get("query")
    searchdata=requests.get(f"https://dummyjson.com/recipes/search?q={word}").json()
    context = {
        'recipedata': searchdata['recipes'],
    }
    return render(request,'index.html',context)
