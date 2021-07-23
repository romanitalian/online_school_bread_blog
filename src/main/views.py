import csv
from time import time

from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from faker import Faker
from django.views.generic import View
from django_filters.views import FilterView
from rest_framework.pagination import PageNumberPagination

from api.generics import PostSerializer
from main.forms import PostForm, SubscriberForm
from main.ftrs import PostFilter
from main.models import Author, Subscriber, Post, Book, ContactUs, Rate
from main.notify_service import notify
from main.post_service import post_all, post_find
from main.subscribe_service import subscribe
from main.tasks import smth_slow_async, subscribe_notify, parse_privatbank
from time import sleep


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {"title": "О нас"})


def api_post_show(request, post_id):
    pst = post_find(post_id)
    # pst.delete()
    return JsonResponse(model_to_dict(pst), safe=False, json_dumps_params={'ensure_ascii': False})


def author_subscribers_all(request):
    all = Subscriber.objects.all()
    # all.delete()
    return render(request, 'main/subscribers.html', {"title": "Все подписки", "subscribers": all})


def post_create(request):
    err_custom = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_all')
        else:
            err_custom = "Error on save Post"
    else:
        form = PostForm()
    context = {
        'form': form,
        'err_my': err_custom
    }
    return render(request, 'main/post_create.html', context=context)


def post_show(request, post_id):
    pst = post_find(post_id)
    return render(request, 'main/post_show.html', {"title": pst.title, "pst": pst})


def post_update(request, post_id):
    err = ""
    pst = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('posts_all'))
            return redirect('posts_all')
        else:
            err = "Error on update Post"
    else:
        form = PostForm(instance=pst)
    context = {
        'form': form,
        'err': err
    }
    return render(request, 'main/post_update.html', context=context)


def json_posts(request):
    posts_cont = post_all().values('title', 'description', 'content')
    return JsonResponse(list(posts_cont), safe=False, json_dumps_params={'ensure_ascii': False})


def authors_new(request):
    faker = Faker()
    # Author.objects.all().delete()
    Author(name=faker.name(), email=faker.email()).save()
    # all = Author.objects.all().values('name', 'email')
    # return JsonResponse(list(all), safe=False)
    # return HttpResponseRedirect(reverse('authors_all'))
    return redirect('authors_all')


def api_authors_new(request):
    faker = Faker()
    # Author.objects.all().delete()
    Author(name=faker.name(), email=faker.email()).save()
    all = Author.objects.all().values('name', 'email')
    return JsonResponse(list(all), safe=False)


def api_authors_all(request):
    all = Author.objects.all().values('id', 'name', 'email')
    return JsonResponse(list(all), safe=False)


def authors_all(request):
    # authors = Author.objects.all()
    authors = Author.objects.all().prefetch_related('books')
    context = {
        'title': 'Авторы',
        'authors': authors,
    }
    return render(request, 'main/authors.html', context)


def books_all(request):
    # books = Book.objects.all()
    # books = Book.objects.all().select_related('author')
    # books = Book.objects.all().only('id', 'title', 'author__name').select_related('author')
    # books = Book.objects.all().defer('author__email', 'author__age').select_related('author')
    books = Book.objects.all().only('id', 'title', 'author__name').select_related(
        'author')  # author.full_name in books.html
    context = {
        'title': 'Книги',
        'books': books,
    }
    return render(request, 'main/books.html', context)


def api_subscribers_all(request):
    all = Subscriber.objects.all().values('email_to', 'author_id')
    return JsonResponse(list(all), safe=False)


def api_author_subscribe(request):
    author_id = request.GET["author_id"]
    email_to = request.GET["email_to"]

    get_object_or_404(Author, pk=author_id)

    subscribe_process(author_id, email_to)

    data = {"author_id": author_id}
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def author_subscribe(request):
    err = ''
    is_subscribe_success = False
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                # return redirect('main/posts_subscribe.html')
                # return HttpResponseRedirect('/api/subscribers/all')
                # return HttpResponseRedirect(reverse('author_subscribers_all'))
                is_subscribe_success = True
            else:
                err = form.errors
        except ValidationError:
            err = 'Уже подписан'
    else:
        # form = SubscriberForm(initial=model_to_dict(Subscriber(email_to="asdfads", author_id=Author.objects.get(pk=15))))
        # form = SubscriberForm(instance=Subscriber())
        form = SubscriberForm()

    if is_subscribe_success:
        print('----- subscribe_notify')
        print(request.POST.get('email_to'))

        email_to = request.POST.get('email_to')
        author_id = request.POST.get('author_id')
        author = Author.objects.get(id=author_id)

        subscribe_notify.delay(email_to, author.name)
        # subscribe_notify.apply_async(args=(email_to, ), countdown=20)
        # subscribe_notify.apply_async(kwargs={'email_to', email_to}, countdown=20)

        return redirect('author_subscribers_all')

    context = {
        'form': form,
        'err': err,
        'title': 'Подписаться на Автора'
    }
    # subscribe_process(author_id, email_to)

    return render(request, 'main/author_subscribe.html', context=context)


def slow(request):
    st = time()
    print('-------------- START')
    smth_slow_async.delay(10)
    time_exec = time() - st
    print('-------------- FINISH. Time exec: {}'.format(time_exec))
    return JsonResponse(dict([('time_exec', time_exec)]))


def subscribe_process(author_id, email_to):
    subscribe(author_id, email_to)
    notify(email_to)


from django.views.generic import ListView, CreateView


class BooksListView(ListView):
    queryset = Book.objects.all()


def posts_all(request):
    return render(request, 'main/posts_all.html', {"title": "Все посты", "psts": post_all()})


class PostsListView(FilterView):
    queryset = Post.objects.all()
    paginate_by = 3
    filterset_class = PostFilter

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['get_params'] = '&'.join(
            f'{key}={val}'
            for key, val in self.request.GET.items()
            if key != 'page'
        )
        context['cnt'] = context['object_list'].count()
        context['title'] = "Все посты"
        return context


class ContactUsView(CreateView):
    success_url = reverse_lazy('home_page')
    model = ContactUs
    fields = ('email', 'subject', 'message')


def display_attr(obj, atrr: str):
    get_display = f'get_{atrr}_display'
    if hasattr(obj, get_display):
        return getattr(obj, get_display)()

    return getattr(obj, atrr)


class PostCSV(View):
    headers = ['title', 'description', 'mood']
    filename = 'posts_all_list.csv'
    sleep(15)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': f'attachment; filename="{self.filename}"'},
        )

        writer = csv.writer(response)

        writer.writerow(self.headers)
        for post in Post.objects.all().iterator():
            writer.writerow([display_attr(post, header) for header in self.headers])

        return response


from rest_framework import generics, serializers, viewsets

# class RateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rate
#         fields = ('id', 'currency', 'source', 'buy', 'sale', 'created', 'get_source_display')

# def validate(self, attrs):
#     print(f"------------ 2222 attrs: {attrs}")
#     return attrs
#
# def validate_source(self, attr):
#     print(f"------------ 111 attr: {attr}")
#     return attr


# class RateListAPIView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Rate.objects.all().order_by('-id')
#     serializer_class = RateSerializer
#
#     # TODO about route name
#     # def get_queryset(self):
#     #     pass
#
#
# class RateAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all().order_by('-id')
#     serializer_class = RateSerializer

# class RateAPIViewSet(viewsets.ModelViewSet):
#     queryset = Rate.objects.all().order_by('-id')
#     serializer_class = RateSerializer
