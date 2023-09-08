from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class ContactPageView(TemplateView):
    template_name = "core/pages/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        return context


class ServicesPageView(TemplateView):
    template_name = "core/pages/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Services'
        return context


class ContactSuccessView(TemplateView):
    template_name = "core/pages/contact_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Success'
        return context


class AboutPageView(TemplateView):
    template_name = "core/pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        return context


""" 
class ContactPageView(FormView, RedirectView):
    template_name = "core/pages/contact.html"
    form_class = ContactForm
    success_url = 'contact_success'

    def get(self, request):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        # Guardar el mensaje en la base de datos
        form.save()

        # Enviar el mensaje por correo electrónico
        username = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        subject = 'Nuevo mensaje de contacto de {}'.format(username)
        message = 'De: {}\n\n{}'.format(email, message)
        from_email = 'ssds@gmail.com'
        recipient_list = ['correo_destino@gmail.com']

        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)

        return redirect('contact_success')
 """
