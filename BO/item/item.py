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


    def get_colunas(self, ):
        return {}