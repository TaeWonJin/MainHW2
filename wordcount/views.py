from django.shortcuts import render
import operator
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text = request.GET['fulltext']
    stext = request.GET['secondtext']
    words = text.split()
    swords= stext.split()
    word_dictionary = {}
    sword_dictionary = {}
      
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1

    for word in swords:
        if word in sword_dictionary:
            #increase
            sword_dictionary[word]+=1
        else:
            #add to dictionary
            sword_dictionary[word]=1

    multi_dictionary = {**word_dictionary, ** sword_dictionary}
    A = multi_dictionary.keys()
    B = word_dictionary.keys()
    C = sword_dictionary.keys()
    list_multi=list(set(A))
    list_first=list(set(B))
    list_second=list(set(C))
    Bb=[]
    AB = set(list_second)
    Bb = [x for x in list_multi if x not in AB]
    K = set(Bb)
    ab = [x for x in list_first if x not in K]
  
    
    sorted_value = sorted(word_dictionary.items(), key=operator.itemgetter(1),reverse=True)
    ssorted_value = sorted(sword_dictionary.items(), key=operator.itemgetter(1),reverse=True)
    multi_value = sorted(ab)


    return render(request, 'result.html',{'full':text,'total':len(words),'dictionary':sorted_value,'sfull':stext,'stotal':len(swords),'sdictionary':ssorted_value,'gub':len(ab),'multilist':multi_value})
    #.items() : 쌍으로 저장 <단어 : 몇번>