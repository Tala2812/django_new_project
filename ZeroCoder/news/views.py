from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import NewsPostForm

def home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
    error = ""
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            # Сохраняем форму, но пока не записываем в базу данных
            news_post = form.save(commit=False)
            # Назначаем автора из данных формы
            news_post.author = form.cleaned_data['author']
            # Теперь сохраняем объект в базе данных
            news_post.save()
            return redirect('news_home')
        else:
            error = "Данные были заполнены некорректно"
    else:
        form = NewsPostForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})