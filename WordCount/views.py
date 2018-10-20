from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	sorted_dict = {}
	for word in wordlist:
		if word in sorted_dict:
			sorted_dict[word] += 1
		else:
			sorted_dict[word] = 1

	sorted_dict = sorted(sorted_dict.items(), key=lambda kv: kv[1], reverse=True)
	return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'sorted_dict': sorted_dict})

def about(request):
	return render(request, 'about.html')
