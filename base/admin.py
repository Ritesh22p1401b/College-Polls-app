from django.contrib import admin
from .models import *


admin.site.register(Candidate)
admin.site.register(Voters)
admin.site.register(Position)
admin.site.register(ControlVote)
