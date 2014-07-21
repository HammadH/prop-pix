from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from emails.models import Leads

class IndexView(TemplateView):
	template_name = 'index.html'

	def post(self, request, *args, **kwargs):
		email = request.POST.get('email')
		try:
			new_lead = Leads.objects.create(email=email)
		except:
			pass
		return HttpResponseRedirect('/') 


home = IndexView.as_view()
