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
        ordenacao = self.request.GET.get('ordenacao')
        produtos = BO.item.item.Item().get_all_itens(ordenacao=ordenacao)
        context = {
            'selecionado': ordenacao if ordenacao is not None else 'vlr_preco_cota',
            'produtos': produtos
        }
        return render(self.request, template_name=template_name, context=context)

    def post(self, *args, **kwargs):
        item_id = self.request.POST.get('item_id')

        qtd_clicks = BO.item.item.Item().adicionar_click(item_id=item_id)
        return JsonResponse({'status': True, 'qtd_clicks': qtd_clicks}, safe=False)

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
            nome=nome[:200] if nome is not None else '',
            email=email[:200] if email is not None else '',
            telefone=telefone[:200] if telefone is not None else '',
            data= data,
            observacao=observacao,
        )

        nova_confirmacao.save()

        from email.message import EmailMessage
        import smtplib

        sender = "nmgrande@hotmail.com"
        message = f"""
             Nome: {nome}
             E-mail: {email}
             Telefone: {telefone}
             Data: {data}
             Observação: {observacao if observacao not in ['None', None, ''] else '--'}
             
        """

        try:
            email = EmailMessage()
            recipient = "nicolas.grande@inteliger.com.br"
            email["From"] = sender
            email["To"] = recipient
            email["Subject"] = f"""Nova confirmação de presença!"""
            email.set_content(message)

            smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
            smtp.starttls()
            smtp.login(sender, "Nicol@smg99!!")

            smtp.sendmail(sender, recipient, email.as_string())
            smtp.quit()
        except:
            pass
        try:
            email = EmailMessage()
            recipient = "lucas.hertel@outlook.com"
            email["From"] = sender
            email["To"] = recipient
            email["Subject"] = f"""Nova confirmação de presença!"""
            email.set_content(message)

            smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
            smtp.starttls()
            smtp.login(sender, "Nicol@smg99!!")



            smtp.sendmail(sender, recipient, email.as_string())
            smtp.quit()
        except:
            pass
        try:
            email = EmailMessage()
            recipient = "stephaniemueller@gmail.com"
            email["From"] = sender
            email["To"] = recipient
            email["Subject"] = f"""Nova confirmação de presença!"""
            email.set_content(message)

            smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
            smtp.starttls()
            smtp.login(sender, "Nicol@smg99!!")

            smtp.sendmail(sender, recipient, email.as_string())
            smtp.quit()
        except:
            pass

        context = {
            'status': True
        }
        return JsonResponse(context, safe=False)


class ProdutosConfirmarView(View):
    def get(self, *args, **kwargs):
        template_name = 'core/confirmacao.html'
        lista = BO.item.item.Item().buscar_compras()
        context = {
            'lista': lista
        }
        return render(self.request, template_name=template_name, context=context)

    def post(self, *args, **kwargs):
        item_id = self.request.POST.get('item_id')
        nome = self.request.POST.get('nome_cadastro')
        status = BO.item.item.Item().confirmar_compra(item_id=item_id, nome=nome)
        return JsonResponse({'status': status}, safe=False)