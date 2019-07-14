from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html',{'test':'Hareesha'})
#  https://www.historynet.com/gettysburg-address-text
def count(request):
    fulltextString=request.GET['fulltext']
    wordList=fulltextString.split()
    # print(fulltext)

    wordictonary = {}

    for word in wordList:
        if word in wordictonary:
            wordictonary[word]  += 1
        else:
            wordictonary[word]  = 1



    return render(request, 'count.html', {'fulltext':fulltextString,'countvalue':len(wordList), 'wordictonary':wordictonary.items() })

def about(request):
    return render(request, 'about.html')

def ourservices(request):
    return render(request, 'ourservices.html')
