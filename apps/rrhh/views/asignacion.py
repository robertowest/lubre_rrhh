from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from . import models, forms


# ---------------------------------------------------------------------------------------
#
#  +---------------+   +---------------+
#  |    Activo     |   | Mantenimiento |
#  |       o       |   +---------------+
#  |   Documento   |
#  +---------------+
#
#  Los activos son elementos asignados a un empleado. Puede ser documentación
#  propia del empleado como el carnet de manejo o elementos entregados por la
#  empresa como un teléfono celular.
#
#  El mantenimiento es el tipo de seguimiento que se le hará a la documentación
#  o elemento asignado.
#
# ---------------------------------------------------------------------------------------

@login_required
def asignacion(request, empl_id):
    context = {'empleado': models.Empleado.objects.get(persona_id=empl_id),
               'activos': models.Activo.objects.filter(responsable_id=empl_id),
               'mantenimientos': None}
    return render(request, 'asignacion/index.html', context)

def activo(request, empl_id, activo_id):
    context = {'empleado': models.Empleado.objects.get(persona_id=empl_id),
               'activos': models.Activo.objects.filter(responsable_id=empl_id),
               'mantenimientos': models.Mantenimiento.objects.filter(activo_id=activo_id),
               'activo': models.Activo.objects.get(id=activo_id)}
    return render(request, 'asignacion/index.html', context)


# ---------------------------------------------------------------------------------------
# acciones realizadas en pantalla mediante AJAX
# ---------------------------------------------------------------------------------------

@login_required
def mantenimiento_ajax(request):
    pk = request.GET.get('id', None)
    context = {'mantenimientos': models.Mantenimiento.objects.filter(activo_id=pk),
               'referencia': pk}
    return render(request, 'asignacion/mantenimientos.html', context)


# ---------------------------------------------------------------------------------------
# altas y modificaciones de activos y mantenimientos
# ---------------------------------------------------------------------------------------

class ActivoCreateView(LoginRequiredMixin, BSModalCreateView):
    form_class = forms.ActivoForm
    template_name = 'asignacion/forms/activo.html'

    def get_success_url(self):
        return reverse_lazy('rrhh:asignacion', kwargs={'empl_id': self.kwargs['empl_id']})


class ActivoUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = models.Activo
    form_class = forms.ActivoForm
    template_name = 'asignacion/forms/activo.html'
    success_message = 'El activo fue correctamente actualizado.'

    def get_success_url(self):
        return reverse_lazy('rrhh:asignacion', kwargs={'empl_id': self.kwargs['empl_id']})


class MantenimientoCreateView(LoginRequiredMixin, BSModalCreateView):
    model = models.Mantenimiento
    form_class = forms.MantenimientoForm
    template_name = 'asignacion/forms/mantenimiento.html'
    # success_url = reverse_lazy('rrhh:home')

    def get_success_url(self):
        return reverse_lazy('rrhh:activo', kwargs={'empl_id': self.kwargs['empl_id'],
                                                   'activo_id': self.kwargs['activo_id']})


class MantenimientoUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = models.Mantenimiento
    form_class = forms.MantenimientoForm
    template_name = 'asignacion/forms/mantenimiento.html'
    success_message = 'El mantenimiento fue correctamente actualizado.'

    def get_success_url(self):
        return reverse_lazy('rrhh:activo', kwargs={'empl_id': self.kwargs['empl_id'],
                                                   'activo_id': self.kwargs['activo_id']})


class MantenimientoReadView(BSModalReadView):
    model = models.Mantenimiento
    template_name = 'rrhh/mantenimiento_read.html'


class MantenimientoCheckView(LoginRequiredMixin, UpdateView):
    model = models.Mantenimiento
    # template_name = 'comunes/generic_form.html'
    template_name = 'rrhh/mantenimiento_check.html'

    form_class = forms.MantenimientoFormCheck
    success_url = reverse_lazy('rrhh:home')

    # def get_queryset(self):
    #     return models.Mantenimiento.objects.filter(id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('rrhh:home')

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super().form_valid(form)
