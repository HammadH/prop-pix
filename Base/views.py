import json

from django.views.generic import TemplateView
from django.http import HttpResponse

from emails.models import Leads

class IndexView(TemplateView):
	template_name = 'index.html'

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			email = request.POST.get('email')
			response_data = {}
			try:
				new_lead = Leads.objects.create(email=email)
				response_data['status'] = 'success'
				response_data['message'] = 'Thank you for your interest! We shall contact you very soon.'
			except:
				response_data['status'] = 'failed'
				response_data['message'] = "Oops! Your email didn't go through! Try again?"
				
			
			return  HttpResponse(json.dumps(response_data), content_type="application/json")


home = IndexView.as_view()
