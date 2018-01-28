from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Choice, Profile

@login_required
def index(request):
	food = request.POST.get('sunday')
	user_v = None
	get_choices = Choice.objects.values('choices', 'vote', 'users')
	get_profile = Profile.objects.values('user', 'has_voted')
	
	new_profile = list(get_profile)

	new_choices = list(get_choices)

	for p in new_profile:
		user_p      = p['user']
		has_voted_p = p['has_voted']
		
		if user_p == request.user.id and has_voted_p == False:
			if food:
				model_con = Profile.objects.get(user=request.user.id)
				model_con.has_voted = True
				model_con.save()

				for q in new_choices:
					choice   = q['choices']
					vote_v   = q['vote']

					if food:
						if food == choice:
							vote_v += 1
							model_conn = Choice.objects.get(choices=choice)
							model_conn.vote = vote_v
							model_conn.users.add(request.user)
							model_conn.save()

				return render(request, 'thanks.html', {})

		if user_p == request.user.id and has_voted_p == True:
			order_items = Choice.objects.order_by('-vote')

			return render(request, 'already_done.html', {'order_items': order_items})



	return render(request, 'index.html', {})



