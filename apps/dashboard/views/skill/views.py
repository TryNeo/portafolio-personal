from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_skills import *
from apps.dashboard.forms.form_skill import *
from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin


class SkillView(TemplateView):
    template_name = 'Skill/skill.html'

class SkillListView(JsonMixin,ListView):
    template_name = 'Skill/skill_json.html'
    model = Skill
    context_object_name = 'skill_info'
    success_url = 'dash:skill'



class SkillCreateView(CreateMixin,CreateView):
    model = Skill
    form_class = SkillForm
    context_object_name = 'obj'
    template_name = 'Skill/skill_form.html'
    success_url = 'dash:skill'

        
class SkillUpdateView(UpdateMixin,UpdateView):
    model = Skill
    form_class = SkillForm
    context_object_name = 'obj'
    template_name = 'Skill/skill_form.html'
    success_url = 'dash:skill'

    

class SkillDeleteView(DeleteMixin,DeleteView):
    model = Skill
    context_object_name = 'obj'
    template_name = 'Skill/skill_delete.html'
    success_url = 'dash:skill'
