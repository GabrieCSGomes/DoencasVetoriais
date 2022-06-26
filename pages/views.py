from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView, DeleteView
from pages.forms import DistritosAdmForm, FichaForm, EnderecoForm, InformacoesForm, EquipeForm
from pages.models import DistritosAdm, Endereco, Equipe, FichaVisita, Info

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class FichaDetailView(DetailView): #Detalhes de uma ficha
    model = FichaVisita
    template_name = 'crud/ficha_read.html'

class FichaListView(ListView): # Lista todas as fichas
    model = FichaVisita
    template_name = 'ficha_list.html'

class FichaCreateView(CreateView): #Criar uma nova ficha
    def get(self, request):
        context = {'ficha_form': FichaForm(), 'distrito_form': DistritosAdmForm(), 'endereco_form': EnderecoForm(), 'informacoes_form': InformacoesForm(), 'equipe_form': EquipeForm()}
        return render(request, 'crud/ficha_create.html', context)

    def post(self, request):
        if request.method == 'POST':
            ficha_form = FichaForm(request.POST)
            distrito_form = DistritosAdmForm(request.POST)
            endereco_form = EnderecoForm(request.POST)
            informacoes_form = InformacoesForm(request.POST)
            equipe_form = EquipeForm(request.POST)

            if ficha_form.is_valid() and distrito_form.is_valid() and endereco_form.is_valid() and informacoes_form.is_valid() and equipe_form.is_valid():
                #Cria instancias de ficha e informacoes sem salvar no banco
                new_ficha = ficha_form.save(commit=False)
                new_informacoes = informacoes_form.save(commit=False)

                #Salva as instancias de distrito, endereco e equipe, para as pk's
                new_distrito = distrito_form.save()
                new_endereco = endereco_form.save()
                new_equipe = equipe_form.save()

                #Salva as pk's de distrito e endereco no objeto de ficha
                new_ficha.distrito = DistritosAdm.objects.get(id=new_distrito.id)
                new_ficha.endereco = Endereco.objects.get(id=new_endereco.id)

                #Salva as pk's de equipe no objeto de informacoes e salva
                new_informacoes.equipe = Equipe.objects.get(id=new_equipe.id)
                new_informacoes.save()

                #Salva as pk de informacoes no objeto de ficha e salva
                new_ficha.infos = Info.objects.get(id=new_informacoes.id)
                new_ficha.save()
                
                messages.success(request, 'Ficha cadastrada com sucesso!')

                return HttpResponseRedirect(reverse('ficha_read', kwargs={'pk': new_ficha.id}))
            else:
                context = {'ficha_form': ficha_form, 'distrito_form': distrito_form, 'endereco_form': endereco_form, 'informacoes_form': informacoes_form, 'equipe_form': equipe_form}
        else:
            context = {'ficha_form': FichaForm(), 'distrito_form': DistritosAdmForm(), 'endereco_form': EnderecoForm(), 'informacoes_form': InformacoesForm(), 'equipe_form': EquipeForm()}

        return render(request, 'ficha.html', context)

class FichaUpdateView(UpdateView): # Editar uma ficha e objetos relacionados
    model = FichaVisita
    template_name = 'crud/ficha_update.html'
    
    def post(self, request, pk):
        ficha = FichaVisita.objects.get(id=pk)
        
        if request.method == 'POST':
            ficha_form = FichaForm(request.POST, instance=ficha)
            distrito_form = DistritosAdmForm(request.POST, instance=ficha.distrito)
            endereco_form = EnderecoForm(request.POST, instance=ficha.endereco)
            informacoes_form = InformacoesForm(request.POST, instance=ficha.infos)
            equipe_form = EquipeForm(request.POST, instance=ficha.infos.equipe)
        if ficha_form.is_valid() and distrito_form.is_valid() and endereco_form.is_valid() and informacoes_form.is_valid() and equipe_form.is_valid():
            ficha_form.save()
            distrito_form.save()
            endereco_form.save()
            informacoes_form.save()
            equipe_form.save()
            messages.success(self.request, 'Ficha atualizada com sucesso!')
            return HttpResponseRedirect(reverse('ficha_read', kwargs={'pk': ficha.id}))
        else:
            messages.error(self.request, 'Erro ao atualizar ficha!')
            return HttpResponseRedirect(reverse('ficha_update', kwargs={'pk': ficha.id}))
            
    def get_context_data(self, **kwargs):
        context = {
            'ficha_form': FichaForm(instance=self.object),
            'distrito_form': DistritosAdmForm(instance=self.object.distrito),
            'endereco_form': EnderecoForm(instance=self.object.endereco),
            'informacoes_form': InformacoesForm(instance=self.object.infos),
            'equipe_form': EquipeForm(instance=self.object.infos.equipe)}
        return context

class FichaDeleteView(DeleteView): # Deletar uma ficha e objetos associados
    model = FichaVisita
    template_name = 'crud/ficha_delete.html'

    def delete(self, request, pk):
        ficha = FichaVisita.objects.get(id=pk)
        if ficha.distrito:
            ficha.distrito.delete()
        if ficha.endereco:
            ficha.endereco.delete()
        if ficha.infos:
            ficha.infos.delete()
            ficha.infos.equipe.delete()
        ficha.delete()

        messages.success(self.request, 'Ficha deletada com sucesso!')
        return HttpResponseRedirect(reverse('ficha_list'))

    def get_success_url(self):
        return reverse('ficha_list')