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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['infos'] = Info.objects.all().filter(ficha=self.kwargs['pk']).order_by('-data', '-hora')
        return context

class FichaListView(ListView): # Lista todas as fichas
    model = FichaVisita
    template_name = 'ficha_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_infos = Info.objects.all().order_by('-data', '-hora')
        
        #Verificar a última informação de cada ficha
        all_ficha_id , last_info_by_ficha= [], []
        for info in all_infos: 
            if info.ficha.id not in all_ficha_id:
                all_ficha_id.append(info.ficha.id)
                last_info_by_ficha.append(info)
        
        context['infos'] = last_info_by_ficha
        return context

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

                #Salva as pk's de equipe no objeto de informacoes
                new_informacoes.equipe = Equipe.objects.get(id=new_equipe.id)

                #Salva a ficha, a pk da ficha no objeto de informações e salva
                new_ficha.save()
                new_informacoes.ficha = FichaVisita.objects.get(id=new_ficha.id)
                new_informacoes.save()
                
                messages.success(request, 'Ficha cadastrada com sucesso!')

                return HttpResponseRedirect(reverse('ficha_read', kwargs={'pk': new_ficha.id}))
            else:
                context = {'ficha_form': ficha_form, 'distrito_form': distrito_form, 'endereco_form': endereco_form, 'informacoes_form': informacoes_form, 'equipe_form': equipe_form}
        else:
            context = {'ficha_form': FichaForm(), 'distrito_form': DistritosAdmForm(), 'endereco_form': EnderecoForm(), 'informacoes_form': InformacoesForm(), 'equipe_form': EquipeForm()}

        return render(request, 'crud/ficha_create.html', context)

class FichaUpdateView(UpdateView): # Editar uma ficha e objetos relacionados
    model = FichaVisita
    template_name = 'crud/ficha_update.html'
    
    def post(self, request, pk):
        ficha = FichaVisita.objects.get(id=pk)
        
        if request.method == 'POST':
            ficha_form = FichaForm(request.POST, instance=ficha)
            distrito_form = DistritosAdmForm(request.POST, instance=ficha.distrito)
            endereco_form = EnderecoForm(request.POST, instance=ficha.endereco)
            if ficha_form.is_valid() and distrito_form.is_valid() and endereco_form.is_valid():
                ficha_form.save()
                distrito_form.save()
                endereco_form.save()
                messages.success(self.request, 'Ficha atualizada com sucesso!')
                return HttpResponseRedirect(reverse('ficha_read', kwargs={'pk': ficha.id}))
            else:
                context = {'ficha_form': ficha_form, 'distrito_form': distrito_form, 'endereco_form': endereco_form}

        return render(request, 'crud/ficha_update.html', context)
            
    def get_context_data(self):
        context = {
            'ficha_form': FichaForm(instance=self.object),
            'distrito_form': DistritosAdmForm(instance=self.object.distrito),
            'endereco_form': EnderecoForm(instance=self.object.endereco),
            'ficha_id': self.object.id}
        return context

class FichaDeleteView(DeleteView): # Deletar uma ficha e objetos associados
    model = FichaVisita
    template_name = 'crud/ficha_delete.html'

    def delete(self, request, pk):
        ficha = FichaVisita.objects.get(id=pk)
        infos = Info.objects.all().filter(ficha=pk)
        
        if ficha.distrito:
            ficha.distrito.delete()
            pass
        if ficha.endereco:
            ficha.endereco.delete()
        if infos:
            for info in infos:
                info.equipe.delete()
        ficha.delete()

        messages.success(self.request, 'Ficha deletada com sucesso!')
        return HttpResponseRedirect(reverse('ficha_list'))

    def get_success_url(self):
        return reverse('ficha_list')

class InfoCreateView(CreateView): #Criar informações de uma ficha
    model = Info
    template_name = 'infos/info_create.html'

    def get(self, request, pk=None):
        context = {'equipe_form': EquipeForm(), 'informacoes_form': InformacoesForm(), 'ficha_id': pk}
        return render(request, 'infos/info_create.html', context)
        
    def post(self, request, pk):
        ficha = FichaVisita.objects.get(id=pk)

        if request.method == 'POST':
            equipe_form = EquipeForm(request.POST)
            informacoes_form = InformacoesForm(request.POST)
            if equipe_form.is_valid() and informacoes_form.is_valid():
                equipe = equipe_form.save()
                informacoes = informacoes_form.save(commit=False)
                informacoes.equipe = equipe
                informacoes.ficha = ficha
                informacoes.save()
                messages.success(self.request, 'Informação criada com sucesso!')
                return HttpResponseRedirect(reverse('ficha_read', kwargs={'pk': pk}))
            else:
                context = {'equipe_form': equipe_form, 'informacoes_form': informacoes_form, 'ficha_id': pk}
        
        return render(request, 'infos/info_create.html', context)

class InfoUpdateView(UpdateView): #Editar informações de uma ficha
    model = Info
    template_name = 'infos/info_update.html'

    def post(self, request, pk, idf):
        info = Info.objects.get(id=pk)

        if request.method == 'POST':
            equipe_form = EquipeForm(request.POST, instance=info.equipe)
            informacoes_form = InformacoesForm(request.POST, instance=info)
            if equipe_form.is_valid() and informacoes_form.is_valid():
                equipe_form.save()
                informacoes_form.save()
                messages.success(self.request, 'Informação atualizada com sucesso!')
                return HttpResponseRedirect(reverse('ficha_read', kwargs={'pk': idf}))
            else:
                context = {'equipe_form': equipe_form, 'informacoes_form': informacoes_form, 'ficha_id': idf, 'info_id': pk}
        
        return render(request, 'infos/info_update.html', context)
    
    def get_context_data(self, **kwargs):
        context = {
            'equipe_form': EquipeForm(instance=self.object.equipe),
            'informacoes_form': InformacoesForm(instance=self.object),
            'ficha_id': self.object.ficha.id,
            'info_id': self.object.id,}
        return context

class InfoDeleteView(DeleteView): #Deletar informações de uma ficha
    model = Info
    template_name = 'infos/info_delete.html'

    def delete(self, request, pk, idf):
        info = Info.objects.get(id=pk)
        info.equipe.delete()
        messages.success(self.request, 'Informação deletada com sucesso!')
        return HttpResponseRedirect(reverse('ficha_read', kwargs={'pk': idf}))

    def get_success_url(self):
        return HttpResponseRedirect(reverse('ficha_read', kwargs={'pk': self.object.ficha.id}))