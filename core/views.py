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
        import core.models
        lista = list(core.models.Confirmacao.objects.values('nome', 'email', 'telefone', 'observacao', 'data').order_by('id'))

        template_name = 'core/rsvp.html'

        context = {
            'lista': lista
        }
        return render(self.request, template_name=template_name, context=context)

    def post(self, *args, **kwargs):
        nome = self.request.POST.get('nome_cadastro')
        email = self.request.POST.get('email_cadastro')
        telefone = self.request.POST.get('telefone_cadastro')
        observacao = self.request.POST.get('observacao_cadastro')
        import core.models
        data = (timezone.now() + timezone.timedelta(hours=-3)).strftime('%d/%m/%Y %H:%M:%S')
        nova_confirmacao = core.models.Confirmacao(
            nome=nome,
            email=email,
            telefone=telefone,
            data= data,
            observacao=observacao,
        )

        nova_confirmacao.save()

        from email.message import EmailMessage
        import smtplib

        sender = "nmgrande@hotmail.com"
        recipient = "nicolas.grande@inteliger.com.br"
        message = f"""
             Nome: {nome}
             E-mail: {email}
             Telefone: {telefone}
             Data: {data}
             Observação: {observacao}
             
        """

        email = EmailMessage()
        email["From"] = sender
        email["To"] = recipient
        email["Subject"] = f"""Nova confirmação de presença!"""
        email.set_content(message)

        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, "Nicol@smg99!!")
        smtp.sendmail(sender, recipient, email.as_string())
        smtp.quit()

        context = {
            'status': True
        }
        return JsonResponse(context, safe=False)