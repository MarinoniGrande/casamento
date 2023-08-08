import core.models


class Item:
    def __init__(self):
        pass

    def get_all_itens(self, ordenacao='nome'):
        if ordenacao is None:
            ordenacao = 'nome'

        lista = list(core.models.Produto.objects.values('id', 'nome', 'imagem', 'preco_cota', 'qtd_clicks',
                                                       'qtd_cotas_maxima', 'preco_total', 'vlr_preco_total', 'vlr_preco_cota',
                                                       'categoria').order_by(ordenacao))
        return lista


    def adicionar_click(self, item_id=None):
        item = core.models.Produto.objects.all().filter(id=item_id).first()
        if item is None:
            return 0
        else:
            if item.qtd_clicks is None:
                item.qtd_clicks = 0
            item.qtd_clicks += 1
            item.save()

            return item.qtd_clicks