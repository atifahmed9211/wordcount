from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def count(request):
    fullText=request.GET['fullText']
    wordsList=fullText.split()
    wordsDictionary={}
    for word in wordsList:
        if word in wordsDictionary:
            wordsDictionary[word]+=1
        else:
            wordsDictionary[word]=1
    sortedWords=sorted(wordsDictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fullText':fullText,'totalWords':len(wordsList),'sortedWords':sortedWords})
def about(request):
    return render(request,'about.html')
