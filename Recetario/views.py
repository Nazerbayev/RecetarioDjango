from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from django.views import generic
from django.utils import timezone

from Recetario.forms import RecetaForm
from Recetario.models import Choice, Receta, Ingrediente
from .models import Question


class IndexView(generic.ListView):
    template_name = "recetario/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last 5 published questions"""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "recetario/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet
        :return:
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "recetario/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "recetario/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("recetario:results", args=(question_id,)))


def agregar(request, test=None):
    if test:
        receta = Receta.objects.get(pk=test)
    else:
        receta = Receta()

    ingrediente_formset = inlineformset_factory(Receta, Ingrediente, fields=("nombre",))

    if request.POST:
        receta_form = RecetaForm(request.POST or None, request.FILES or None, instance=receta)
        ingrediente_set = ingrediente_formset(request.POST, instance=receta)
        if receta_form.is_valid() and ingrediente_set.is_valid():
            receta_form.save()
            ingrediente_set.save()
        return HttpResponseRedirect(reverse("recetario:index"))
    else:
        receta_form = RecetaForm(instance=receta)
        ingrediente_set = ingrediente_formset(instance=receta)

    return render(request, "recetario/receta_add.html", {'form': receta_form, 'formset': ingrediente_set})
