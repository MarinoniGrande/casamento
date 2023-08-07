var tabela_lista_medicamentos = $("#tabela_lista_medicamentos").dxDataGrid({
    dataSource: data_table_medicamentos,
    filterRow: optionsDefaultTables.filterRow,
    onFileSaving: optionsDefaultTables.onFileSaving,
    headerFilter: optionsDefaultTables.headerFilter,
    filterBuilderPopup: optionsDefaultTables.filterBuilderPopup,
    scrolling: optionsDefaultTables.scrolling,
    onEditorPreparing: function(e){
        searchPanelCustomize(e);
        //resetGroupToolbar(e);
        //btnFilterAdvanced(e);
        //btnClearFilter(e);
        addBtnExport(e);
        //addBtnChooser(e);
        btnAfterEnd(e);
    },
    onContentReady: optionsDefaultTables.onContentReady,
    rowAlternationEnabled: optionsDefaultTables.rowAlternationEnabled,
    searchPanel: optionsDefaultTables.searchPanel,
    columnAutoWidth: optionsDefaultTables.columnAutoWidth,
    showColumnLines: optionsDefaultTables.showColumnLines,
    showRowLines: optionsDefaultTables.showRowLines,
    columns: [
        {
            dataField: "pk",
            caption: "ID",
            dataType: "number",
            visible: false,
            headerCellTemplate: function (container, options) {
                // função filterRow(container, options, headerDefault);
                // 1 parâmetro, container: elemento HTML referente a este header
                // 2 parâmetro, options: todas as opções referente a esta instancia do datagrid
                // 3 parâmetro, headerDefault: recebe um booleano, caso você esteja inserindo um html diferente do que existe no ~caption: "NomeDaColuna"~ coloque o parâmetro false, indicando que o header não é default, caso contrário a função irá inserir o caption como nome da coluna por padrão, este parâmetro pode ser opcional.
                filterRow(container, options);
            },
            cellTemplate: function (container, e) {
                replaceCell(container, e, "", "");
            }
        },
        {
            dataField: "medicamento",
            caption: "Medicamento",
            dataType: "string",
            headerCellTemplate: function (container, options) {
                // função filterRow(container, options, headerDefault);
                // 1 parâmetro, container: elemento HTML referente a este header
                // 2 parâmetro, options: todas as opções referente a esta instancia do datagrid
                // 3 parâmetro, headerDefault: recebe um booleano, caso você esteja inserindo um html diferente do que existe no ~caption: "NomeDaColuna"~ coloque o parâmetro false, indicando que o header não é default, caso contrário a função irá inserir o caption como nome da coluna por padrão, este parâmetro pode ser opcional.
                filterRow(container, options);
            },
            cellTemplate: function (container, e) {
                replaceCell(container, e, "", "");

                if(!e.data.medicamento){
                    container.html('')
                }
            }
        },
        {
            dataField: "indicacao",
            caption: "Indicação",
            dataType: "string",
            headerCellTemplate: function (container, options) {
                // função filterRow(container, options, headerDefault);
                // 1 parâmetro, container: elemento HTML referente a este header
                // 2 parâmetro, options: todas as opções referente a esta instancia do datagrid
                // 3 parâmetro, headerDefault: recebe um booleano, caso você esteja inserindo um html diferente do que existe no ~caption: "NomeDaColuna"~ coloque o parâmetro false, indicando que o header não é default, caso contrário a função irá inserir o caption como nome da coluna por padrão, este parâmetro pode ser opcional.
                filterRow(container, options);
            },
            cellTemplate: function (container, e) {
                replaceCell(container, e, "", "");
                
                if(!e.data.indicacao){
                    container.html('')
                }
            }
        },
        {
            dataField: "pagamento",
            caption: "Pagamento",
            dataType: "string",
            headerCellTemplate: function (container, options) {
                // função filterRow(container, options, headerDefault);
                // 1 parâmetro, container: elemento HTML referente a este header
                // 2 parâmetro, options: todas as opções referente a esta instancia do datagrid
                // 3 parâmetro, headerDefault: recebe um booleano, caso você esteja inserindo um html diferente do que existe no ~caption: "NomeDaColuna"~ coloque o parâmetro false, indicando que o header não é default, caso contrário a função irá inserir o caption como nome da coluna por padrão, este parâmetro pode ser opcional.
                filterRow(container, options);
            },
            cellTemplate: function (container, e) {
                replaceCell(container, e, "", "");

                if(!e.data.pagamento){
                    container.html('')
                }
            }
        },
    ]
}).dxDataGrid("instance");