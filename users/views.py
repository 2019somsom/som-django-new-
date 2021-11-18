# users/views.py

from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.views.generic import FormView
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from .decorators import login_message_required, admin_required, logout_message_required

@method_decorator(logout_message_required, name='dispatch')
class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/users/main/'

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)
        
        if user is not None:
            self.request.session['user_id'] = user_id
            login(self.request, user)

        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('/')

# 메인화면(로그인 후)
@login_message_required
def main_view(request):
    # notice_list = Notice.objects.order_by('-id')[:5]
    # calendar_property = [x.event_id for x in Calender.objects.all() if x.d_day == False]
    # calendar_list = Calender.objects.exclude(event_id__in=calendar_property).order_by('start_date')[:5]
    # free_list = Free.objects.filter(category='정보').order_by('-id')[:5]
    # anonymous_list = sorted(Anonymous.objects.all(), key=lambda t: t.like_count, reverse=True)[:5]

    context = {
        # 'notice_list' : notice_list,
        # 'calendar_list' : calendar_list,
        # 'free_list' : free_list,
        # 'anonymous_list' : anonymous_list,
    }
    return render(request, 'users/main.html', context)