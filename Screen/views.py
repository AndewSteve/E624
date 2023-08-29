from django.shortcuts import render
from .forms import SearchForm
# Create your views here.

def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # 在这里执行搜索操作，获取搜索结果
            # 将搜索结果传递给模板
            return render(request, 'search_results.html', {'query': query})
    else:
        form = SearchForm()
    return render(request, 'search_screen.html', {'form': form})