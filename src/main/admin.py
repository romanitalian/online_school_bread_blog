from django.contrib import admin

from account.models import Ava, User
from main.models import Author, Post, Subscriber, Book, Rate


class AvaAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    # raw_id_fields = ['user',]


class AvaInline(admin.TabularInline):
    model = Ava
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = (AvaInline,)
    list_display = (
        'email',
        'username',
        'is_staff',
        'is_superuser',
        'is_active',
    )


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'currency',
        'source',
        'buy',
        'sale',
        'created',
    )
    list_filter = (
        'currency',
        'source',
        # 'buy',
        # 'sale',
        'created',
    )
    search_fields = (
        'currency',
        'source',
        'buy',
        'created',
    )

    # actions = None
    # readonly_fields = ['source']

    def get_readonly_fields(self, request, obj=None):
        if request.user.has_perm('main.rate_edit_all____2'):
            return 'source', 'currency'
        return super().get_readonly_fields(request, obj)

    # def has_delete_permission(self, request, obj=None):
    #     return request.user.is_superuser

class BookAdmin(admin.ModelAdmin):
    list_select_related = ['author']
    search_fields = (
        'title',
    )

admin.site.register(Ava, AvaAdmin)
admin.site.register(User, UserAdmin)

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Subscriber)
admin.site.register(Book, BookAdmin)
admin.site.register(Rate, RateAdmin)
