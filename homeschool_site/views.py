from django.shortcuts import HttpResponse, HttpResponseRedirect, render_to_response, render, Http404
from django.core.urlresolvers import reverse

from homeschool_site.models import Form, RSVP, Contact, Event, News, AboutUs
from homeschool_site.forms import HomeSchoolUserCreationForm, RSVPForm


def index(request):
    news = News.objects.all().order_by('-time_of_news')[:10]
    about_us = None
    try:
        about_us = AboutUs.objects.get(active=True)
    except AboutUs.DoesNotExist:
        pass
    return render_to_response('homeschool_site/index.html', {
        'request': request,
        'news': news,
        'about_us': about_us,
    })


def register(request):
    if request.method == 'POST':
        form = HomeSchoolUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = HomeSchoolUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


def download_form(request, form_id):
    form = Form.objects.get(id=form_id)
    filename = form.file.name.split('/')[-1]
    response = HttpResponse(form.file, content_type='application/msword')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response


def new_notes(request):
    RSVPs = RSVP.objects.all().order_by('-time_rsvpd')[:10]

    return render(request, "homeschool_site/new_notes.html", {
        'RSVPs': RSVPs,
    })


def contact_us(request):
    contact = None
    try:
        contact = Contact.objects.get(active=True)
    except Contact.DoesNotExist:
        pass
    return render(request, "homeschool_site/contact_us.html", {
        'contact': contact,
    })


def forms(request):
    forms_list = Form.objects.all()
    return render(request, "homeschool_site/forms.html", {
        'forms': forms_list,
    })


def events(request):
    events_list = Event.objects.all()
    return render(request, "homeschool_site/events.html", {
        'events': events_list,
    })


def rsvp_confirm(request):
    return render(request, "homeschool_site/rsvp_confirm.html", )


def event(request, event_id):
    try:
        the_event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        raise Http404("There is no event with that ID")
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            RSVP.objects.create(
                user=request.user,
                response=cleaned_data['response'],
                note=cleaned_data['rsvp_note'],
                event=the_event,
                num_guests=cleaned_data['num_guests']
            )
            return HttpResponseRedirect(reverse('rsvp_confirm'))
    else:
        return render(request, "homeschool_site/event.html", {
            'event': the_event,
        })
