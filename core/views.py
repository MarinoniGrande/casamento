from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import View
import BO.item.item


class HomeView(View):
    def get(self, *args, **kwargs):
        template_name = 'core/home.html'
        context = {
        }
        return render(self.request, template_name=template_name, context=context)

    def post(self, *args, **kwargs):
        return JsonResponse({}, safe=False)


class ProdutosView(View):
    def get(self, *args, **kwargs):
        template_name = 'core/produtos.html'

        produtos = BO.item.item.Item().get_all_itens()
        context = {
            'produtos': produtos
        }
        return render(self.request, template_name=template_name, context=context)

    def post(self, *args, **kwargs):
        colunas = {
            "colunas": {
                "categoria": {
                    "nome": "Categoria",
                    "ordem": 2,
                    "tipo": None,
                    "valores": {
                        "PRESERVATIVO": 69,
                        "LUBRIFICANTE ÍNTIMO": 26
                    }
                }
            }
        }
        return JsonResponse(colunas, safe=False)

class RSVPView(View):
    def get(self, *args, **kwargs):
        nome = self.request.POST.get('nome')
        email = self.request.POST.get('email')
        telefone = self.request.POST.get('telefone')
        observacao = self.request.POST.get('observacao')
        import core.models
        nova_confirmacao = core.models.Confirmacao(
            nome=nome,
            email=email,
            telefone=telefone,
            data= timezone.now(),
            observacao=observacao,
        )
        nova_confirmacao.save()
        context = {
            'status': True
        }
        return JsonResponse(context, safe=False)