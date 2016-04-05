from django.contrib import admin


from homeschool_site.models import Form, HomeSchoolUser, News, RSVP, Event, Contact, AboutUs


# Register your models here.
class HomeSchoolUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_approved')
    list_filter = ('is_staff', 'is_superuser', 'is_approved')


class FormAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_visible_by_unreg')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class RSVPAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'response', 'get_user_status', 'get_start_of_note')
    list_filter = ('response', 'event', )


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'contact_phone', 'active')


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('get_message', 'active')


admin.site.register(HomeSchoolUser, HomeSchoolUserAdmin)

admin.site.register(Form, FormAdmin)

admin.site.register(News, NewsAdmin)

admin.site.register(RSVP, RSVPAdmin)

admin.site.register(Event, EventAdmin)

admin.site.register(Contact, ContactAdmin)

admin.site.register(AboutUs, AboutUsAdmin)
