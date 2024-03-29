from django.contrib import admin
from core.models import Student, Institute, Grade, AppUser, Blog, Author, Entry, Dog
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# # Register your models here.
@admin.register(Student)
class MembershipInline(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Institute)
class MembershipInline(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Grade)
class MembershGradeipInline(admin.ModelAdmin):
    list_display = ['id']

@admin.register(AppUser)
class UserAdminChild(ImportExportModelAdmin, UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',
                                         'email', 'phone','gender'
                                         )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('id', 'username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'pk')
    date_hierarchy = 'date_joined'
    ordering = ['-id']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['id']