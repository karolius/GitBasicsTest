from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp


def home(request):
    title = "Register your side curls!"
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New sheklemaker"

        instance.save()
        context = {
            "title": "Thanks goyy!",
        }

    if request.user.is_authenticated() and request.user.is_staff:
        queryset = SignUp.objects.all().order_by('-donation')\
            .filter(doner_kebab__icontains="kosher")
        context = {
            "queryset": queryset,
        }

    return render(request, "home.html", context)


def contact(request):
    title = "Cuntact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        full_name = form.cleaned_data.get('full_name')

        subject = "Gib back our mone!"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'karolius127@gmail.com']
        contact_message = "%s: %s VIA %s" % (full_name, message, email)
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False,
        )

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)