from django.contrib import admin

# Register your models here.

from .models import About, Introduction
admin.site.register([About, Introduction])

from .models import Skill, Skill_Set, Skill_Desc
admin.site.register([Skill, Skill_Set, Skill_Desc])

from .models import Certification
admin.site.register(Certification)

from .models import Employment, EmploymentPosition
admin.site.register([Employment, EmploymentPosition])

from .models import Education
admin.site.register(Education)

from .models import Testimonial
admin.site.register(Testimonial)

from .models import Advert
admin.site.register(Advert)

from .models import Quote
admin.site.register(Quote)