from django.shortcuts import render
from .models import PostQuestion, PostAnswer
# Create your views here.
def PostListView(request):
    obj = PostQuestion.objects.all()
    return render(request, 'postlist.html', {'obj':obj})

def PostDetailView(request,pk):
    obj = PostQuestion.objects.get(pk=pk)
    answers = PostAnswer.objects.filter(question=obj)
    return render(request, 'postdetail.html', {'obj':obj, 'ans':answers})
