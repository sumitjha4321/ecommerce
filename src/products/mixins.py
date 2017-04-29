from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings


class StaffRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(
                request,
                'You do not have the permission required to perform the '
                'requested operation.')
            return redirect(settings.LOGIN_URL)
        return super(StaffRequiredMixin, self).dispatch(request,
            *args, **kwargs)

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(
		self, request, *args, **kwargs)
