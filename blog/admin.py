''' Register Models on Admin '''
from django.contrib import admin
from .models import Post, Postcategory, Comment

# Register your models here.


class PostcategoryAdmin(admin.ModelAdmin):
    '''Register Post Categores; display the names below'''
    list_display = (
        'friendly_name',
        'name',
    )


class PostAdmin(admin.ModelAdmin):
    '''Register Posts'''
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    '''Register comment model '''
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        ''' Update Query set '''
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Postcategory, PostcategoryAdmin)
admin.site.register(Comment, CommentAdmin)
