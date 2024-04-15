$(document).ready(function() {
    // Variáveis
    var EmpresaUrl = 'https://allian.pythonanywhere.com/empresas/lista/';
    var MembroUrl = 'https://allian.pythonanywhere.com/membros/lista/';
    var TarefaUrl = 'https://allian.pythonanywhere.com/tarefas/lista/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var dataBtn     = $('#data-btn');
    var dataForm    = $('#data-form');
    var filter      = $('#filter');
    var filtroAniversario = $('#filtro_aniversario');
    var confirmBtn = $('#confirmBtn');
    var btnRecusa = $('#btnRecusa');
    var form = $('#createForm');
    var openModalBtn = $('#openModalBtn');
    var voltarBtn = $('#voltarBtn');
    var nomeField = $('#div_id_nome');
    var dataAniversarioField = $('#div_id_data_aniversario');
    var nomeComputadorField = $('#div_id_nome_computador');
    var numeroAnyDeskField = $('#div_id_numero_anydesk');
    var idNome = $('#id_nome');
    var idSistema = $('#id_id_sistema');
    var campoAtividade = $('#id_atividade');
    var idNomeComputador = $('#id_nome_computador');
    var admin = $('#div_id_administrador');
    var campoObs = $('#id_obs');
    var numSistemaBtn = $('numSistema-btn')
    var numSistemaForm = $('numSistema-form');
    var numSistema     = $('numSistema');

    // notificações

    var notificationCount = 0; // Contagem inicial de notificações

    // Função para formatar a data no formato 'dia/mês/ano'
    function formatDate(date) {
        var dia = date.getDate() + 1;
        var mes = date.getMonth() + 1; // Mês começa do zero, então adiciona 1
        var ano = date.getFullYear();

        // Adiciona um zero à esquerda se o dia ou mês for menor que 10
        var diaFormatado = dia < 10 ? '0' + dia : dia;
        var mesFormatado = mes < 10 ? '0' + mes : mes;

        return diaFormatado + '/' + mesFormatado + '/' + ano;
    }


    // Função para atualizar a lista de notificações com dados de empresas e membros
    function atualizarListaNotificacoes(dataEmpresas, dataMembros) {
        var listaGroup = $('.list-group');
        listaGroup.empty(); // Limpa a lista antes de adicionar novos itens

        // Adiciona notificações de empresas com certificados vencendo em até 7 dias
        if (dataEmpresas && dataEmpresas.notificacoes) {
            dataEmpresas.notificacoes.forEach(function(notificacao) {
                var listItem = $('<a href="#" class="list-group-item list-group-item-action active"></a>');
                listItem.append('<h5 class="mb-1"><i class="fa-solid fa-certificate"></i> ' + notificacao.nome + '</h5>');
                var dataFormatada = formatDate(new Date(notificacao.data_certificado));
                listItem.append('<p class="mb-1">Certif. vencendo(ido) em ' + dataFormatada + '</p>');
                listItem.append('<small>Clique para saber mais.</small>');

                // Adiciona evento de clique para mostrar o modal
                listItem.click(function() {
                    exibirModal('Empresa:  ' + notificacao.nome,
                    'Certificado digital da empresa está vencido(endo) em ' + dataFormatada +
                    '. Informe ao responsável da empresa sobre a data, a fim de renovar com a contabilidade ' +
                    'ou com a equipe de suporte do sistema!');
                });

                listaGroup.append(listItem);
            });
        }

        // Adiciona notificações de membros com aniversário nos próximos 7 dias
        if (dataMembros && dataMembros.notificacoes_aniversarios) {
            dataMembros.notificacoes_aniversarios.forEach(function(notificacao) {
                var listItem = $('<a href="#" class="list-group-item list-group-item-action active"></a>');
                listItem.append('<h5 class="mb-1"><i class="fa-solid fa-cake-candles"></i> ' + notificacao.nome + '</h5>');
                var dataAniversario = new Date(notificacao.data);
                listItem.append('<p class="mb-1">Aniversariando em ' + formatDate(dataAniversario) + '</p>');
                listItem.append('<small>Clique para saber mais.</small>');

                // Adiciona evento de clique para mostrar o modal
                listItem.click(function() {
                    exibirModal('Cliente: ' + notificacao.nome,
                    'Olá, este cliente estará aniversariando em ' + formatDate(dataAniversario) +
                    '. Não se esqueça de gerar o Flyer de aniversariante, enviar para o cliente ' +
                    'e postar nos status!');
                });

                listaGroup.append(listItem);
            });
        }

        // Exibe a lista apenas se houver notificações para mostrar
        if (listaGroup.children().length > 0) {
            // Lista de notificações não será exibida automaticamente aqui
        } else {
            listaGroup.hide();
        }
    }

    function exibirModal(titulo, descricao) {
        var modal = $('#staticBackdrop1');

        // Atualiza o título e descrição do modal
        modal.find('.modal-title').text(titulo);
        modal.find('.modal-body').text(descricao);

        // Mostra o modal
        modal.modal('show');
    }

    function marcarComoLida() {
        // Aqui você pode adicionar a lógica para remover a notificação da lista ou realizar outras ações necessárias
        var modal = $('#staticBackdrop1');
        modal.modal('hide'); // Fecha o modal após clicar em "Marcar como Lida"
    }


    // Função para atualizar a contagem de notificações e o estilo do ícone
    function atualizarContagemNotificacoes(dataEmpresas, dataMembros) {
        var totalNotificacoes = 0;

        // Conta as notificações de empresas
        if (dataEmpresas && dataEmpresas.notificacoes) {
            totalNotificacoes += dataEmpresas.notificacoes.length;
        }

        // Conta as notificações de membros
        if (dataMembros && dataMembros.notificacoes_aniversarios) {
            totalNotificacoes += dataMembros.notificacoes_aniversarios.length;
        }

        // Atualiza a contagem de notificações
        notificationCount = totalNotificacoes;

        // Exibe a contagem de notificações não lidas
        var notificationCountElement = $('#notification-count');
        notificationCountElement.text(notificationCount);

        if (notificationCount > 0) {
            notificationCountElement.show();
            // Adiciona uma classe de destaque no ícone de sino
            $('.notification-icon, .notification-count').addClass('has-notifications');
            // Animação de pulso
            $('.notification-icon, .notification-count').addClass('animated infinite pulse');
        } else {
            notificationCountElement.hide();
            // Remove a classe de destaque no ícone de sino
            $('.notification-icon').removeClass('has-notifications');
            // Remove a animação de pulso
            $('.notification-icon').removeClass('animated infinite pulse');
        }
    }

    // Função para carregar dados de empresas e membros
    function carregarDados() {
        // Requisição AJAX para obter dados de empresas
        $.ajax({
            url: '/empresas/lista_ajax/', // Endpoint para empresas
            type: 'GET',
            dataType: 'json',
            success: function(dataEmpresas) {
                // Requisição AJAX para obter dados de membros
                $.ajax({
                    url: '/membros/lista_ajax/', // Endpoint para membros
                    type: 'GET',
                    dataType: 'json',
                    success: function(dataMembros) {
                        // Atualiza a lista de notificações na interface com dados combinados
                        atualizarListaNotificacoes(dataEmpresas, dataMembros);
                        // Atualiza a contagem de notificações
                        atualizarContagemNotificacoes(dataEmpresas, dataMembros);

                        // Evento de clique no documento para fechar a lista ao clicar fora dela
                        $(document).click(function(event) {
                            var listaGroup = $('.list-group');
                            var notificationIcon = $('.notification-icon');

                            // Verifica se o clique não ocorreu dentro da lista, no ícone de sino
                            // ou nos botões de fechar do modal ou de cancelar
                            if (!listaGroup.is(event.target) && listaGroup.has(event.target).length === 0 &&
                                !notificationIcon.is(event.target) && notificationIcon.has(event.target).length === 0 &&
                                !$(event.target).hasClass('btn-close') && !$(event.target).hasClass('btn-secondary')) {
                                listaGroup.hide(); // Oculta a lista
                            }
                        });
                    },
                    error: function(xhr, status, error) {
                        console.error('Erro ao carregar membros:', error);
                    }
                });
            },
            error: function(xhr, status, error) {
                console.error('Erro ao carregar empresas:', error);
            }
        });

        // Evento de clique no ícone de sino para exibir/ocultar a lista de notificações
        $('.notification-icon').click(function(event) {
            var listaGroup = $('.list-group');
            if (notificationCount > 0) {
                listaGroup.toggle(); // Alternar a visibilidade da lista
            } else {
                listaGroup.hide(); // Ocultar a lista se não houver notificações
            }

            // Impede que o evento de clique propague para o documento
            event.stopPropagation();
        });
    }

    // Chamada inicial para carregar dados ao carregar a página
    $(document).ready(function() {
        carregarDados();
    });



    // DatePicker

    $( function() {
      $("#id_data_certificado").datepicker({
        changeMonth: true,
        changeYear: true,
        dateFormat: "dd/mm/yy",
        monthNamesShort: [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ],
        dayNamesMin: [ "Do", "2ª", "3ª", "4ª", "5ª", "6ª", "Sá" ]
      });
      $("#data, #id_data_aniversario").datepicker({
        changeMonth: true,
        changeYear: true,
        dateFormat: "dd-mm-yy",
        monthNamesShort: [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ],
        dayNamesMin: [ "Do", "2ª", "3ª", "4ª", "5ª", "6ª", "Sá" ]
      });
    });


    // Função de foco

    idNome.focus();

    idSistema.focus();

    campoAtividade.focus();
    idNomeComputador.focus();

    // Funções de deletar

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Você confirma a EXCLUSÃO?');

        if(result) {
            window.location.href = delLink;
        }
    });

    // Campos de filtros

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $('#numSistema-btn').on('click', function() {
        $('#numSistema-form').submit();
    });

    $(filter).change(function() {
        var filter = $(this).val();
        window.location.href = TarefaUrl + '?filter=' + filter;
    });

    $(filtroAniversario).change(function() {
        var filter = $(this).val();
        window.location.href = MembroUrl + '?filter=' + filter;
    });

    // Função de carregamento do modal

    $('#loadingModal').modal({
        keyboard: false, // Disable closing with Esc
        backdrop: 'static' // Disable closing when clicking outside
    });

    // Função que envolve o select2

    // Função para normalizar o texto removendo a acentuação
    function normalize(text) {
      return text.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    }

    $('#id_nome_cliente').select2({
      placeholder: 'Selecione um cliente',
      minimumInputLength: 1,
      language: {
        inputTooShort: function() {
          return 'Por favor, insira 1 ou mais caracteres';
        },
        noResults: function() {
          return 'Nenhum resultado encontrado';
        },
        searching: function() {
          return 'Procurando...';
        }
      },
      ajax: {
        url: '/membros/lista_ajax/',
        dataType: 'json',
        delay: 250,
        processResults: function(data, params) {
          var query = normalize(params.term).toLowerCase();
          var filteredData = $.grep(data.membros, function(membro) {
            return normalize(membro.nome).toLowerCase().indexOf(query) > -1 || membro.id.toString().indexOf(query) > -1;
          });
          return {
            results: filteredData.map(function(membro) {
              return {
                id: membro.id,
                text: '<div><strong>' + membro.nome + '</strong></div>'
              };
            })
          };
        },
        cache: true
      },
      escapeMarkup: function(markup) {
        return markup;
      }
    });

    $('#id_empresa_cliente').select2({
      placeholder: 'Selecione uma empresa',
      minimumInputLength: 1,
      language: {
        inputTooShort: function() {
          return 'Por favor, insira 1 ou mais caracteres';
        },
        noResults: function() {
          return 'Nenhum resultado encontrado';
        },
        searching: function() {
          return 'Procurando...';
        }
      },
      ajax: {
        url: '/empresas/lista_ajax/',
        dataType: 'json',
        delay: 250,
        processResults: function(data, params) {
          var query = normalize(params.term).toLowerCase();
          var filteredData = $.grep(data.empresas, function(empresa) {
            return normalize(empresa.nome).toLowerCase().indexOf(query) > -1 || empresa.id.toString().indexOf(query) > -1 || empresa.id_sistema.toString().indexOf(query) > -1;
          });
          return {
            results: filteredData.map(function(empresa) {
              return {
                id: empresa.id,
                text: '<div><strong>' + empresa.nome + '</strong></div>'
              };
            })
          };
        },
        cache: true
      },
      escapeMarkup: function(markup) {
        return markup;
      }
    });

    // Funções referentes aos formulários de cadastro e edição

    $(confirmBtn).on('click', function() {
       form.submit();
    });

    $('#staticBackdrop').on('keydown', function(e) {
      // Verifica o código da tecla pressionada (ignora maiúsculas/minúsculas)
      var keyCode = e.which || e.keyCode;
      if (keyCode === 83 || keyCode === 78) {
        // Simular um clique no botão correspondente
        if (keyCode === 83) { // 's'
          confirmBtn.click();
        } else if (keyCode === 78) { // 'n'
          btnRecusa.click();
        }
      }
    });


    $(openModalBtn).on('focus', function() {
       isCriarBtnFocused = true;
    });

    $(openModalBtn).on('blur', function() {
       isCriarBtnFocused = false;
    });

    $(voltarBtn).on('focus', function() {
       isVoltarBtnFocused = true;
    });

    $(voltarBtn).on('blur', function() {
       isVoltarBtnFocused = false;
    });

    $('#createForm').on('keydown', function(e) {
      if (e.key === 'Enter') {
        if (isCriarBtnFocused || isVoltarBtnFocused) {
          // Abrir o modal se o botão "Criar" estiver focado
          $('#staticBackdrop').modal('show');
        } else {
          e.returnValue=false;
          e.cancel = true;
          // Prevenir o envio do formulário
          e.stopPropagation();
        }
      }
    });

    $(idSistema).on('keydown', function(e) {
       if (e.key === 'Enter') {
          e.preventDefault();
       }
    });

    $(admin).on('keydown', function(e) {
       if (e.key === 'Enter') {
          e.preventDefault();
       }
    });

    $(nomeField).on('keydown', function(e) {
       if (e.key === 'Enter') {
          e.preventDefault();
       }
    });

    $(campoObs).on('keydown', function(e) {
       if (e.key === 'Enter') {
          e.preventDefault();
       }
    });

    $(dataAniversarioField).on('keydown', function(e) {
       if (e.key === 'Enter') {
          e.preventDefault();
       }
    });

    $(nomeComputadorField).on('keydown', function(e) {
       if (e.key === 'Enter') {
          e.preventDefault();
       }
    });

    $(numeroAnyDeskField).on('keydown', function(e) {
       if (e.key === 'Enter') {
          e.preventDefault();
       }
    });

    // Animação alert e progress bar

    var $alert = $('.alert');
    var $progressBar = $('.progress-bar');
    var tempoExibicao = 5000;
    var diminuirProgresso = function () {
        var inicio = new Date().getTime();
        var intervalo = 100; // Intervalo de atualização da barra de progresso (100ms).
        var animacao = function () {
            var agora = new Date().getTime();
            var decorrido = agora - inicio;
            var progresso = 100 - (decorrido / tempoExibicao) * 100;
            $progressBar.width(progresso + '%');
            if (progresso > -10) {
                requestAnimationFrame(animacao);
            } else {
                $alert.hide();
            }
        };
        animacao();
    };
    diminuirProgresso();

    var tempoExibicaoModal = 3000;
    var fecharModal = function () {
        $('#loadingModal').modal('hide');
    };
    setTimeout(fecharModal, tempoExibicaoModal);

    // Define a data atual no campo de entrada de data

    function obterDataAtual() {
        const dataAtual = new Date();
        const ano = dataAtual.getFullYear();
        let mes = (dataAtual.getMonth() + 1).toString().padStart(2, '0'); // Adiciona zero à esquerda, se necessário
        let dia = dataAtual.getDate().toString().padStart(2, '0'); // Adiciona zero à esquerda, se necessário

        return `${dia}-${mes}-${ano}`;
    }

    $('#id_data_aniversario, #data').val(obterDataAtual());

    const campoData = $('#id_data_aniversario');
    const campoDataAniversario = $('#id_id_data_aniversario');

    campoData.on('input', function () {
        campoDataAniversario.val(campoData.val());
    });

    // Função para formatar a data de "DD-MM-YYYY" para "YYYY-MM-DD"
    function formatarDataParaBackend(dataInput) {
      const partes = dataInput.split('-');
      return `${partes[2]}-${partes[1]}-${partes[0]}`;
    }

    $(dataBtn).on('click', function() {
      const dataInput = $('#data').val();
      const dataFormatada = formatarDataParaBackend(dataInput);
      $('#data').val(dataFormatada);
      dataForm.submit();
    });


    const dataPesquisaInput = $("#data_pesquisa");

    // Obtenha a data atual no formato correto para o campo de entrada de data
    const today = new Date().toISOString().slice(0, 10);

    // Defina o valor do campo de entrada para a data atual
    dataPesquisaInput.val(today);
});