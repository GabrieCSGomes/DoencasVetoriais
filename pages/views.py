from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView
from pages.forms import DistritosAdmForm, FichaForm, EnderecoForm, InformacoesForm, EquipeForm
from pages.models import DistritosAdm, Endereco, Equipe, FichaVisita, Info

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

'''class FichaDetailView(DetailView):
    model = FichaVisita
    template_name = 'ficha_detail.html'

class FichaListView(View):
    model = FichaVisita
    template_name = 'ficha_list.html'''

class FichaRegistroView(View):
    def get(self, request):
        context = {'ficha_form': FichaForm(), 'distrito_form': DistritosAdmForm(), 'endereco_form': EnderecoForm(), 'informacoes_form': InformacoesForm(), 'equipe_form': EquipeForm()}
        return render(request, 'ficha.html', context)

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
                
                return HttpResponseRedirect('/')
            else:
                context = {'ficha_form': ficha_form, 'distrito_form': distrito_form, 'endereco_form': endereco_form, 'informacoes_form': informacoes_form, 'equipe_form': equipe_form}
        else:
            context = {'ficha_form': FichaForm(), 'distrito_form': DistritosAdmForm(), 'endereco_form': EnderecoForm(), 'informacoes_form': InformacoesForm(), 'equipe_form': EquipeForm()}

        return render(request, 'ficha.html', context)
