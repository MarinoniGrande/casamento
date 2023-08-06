from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
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
