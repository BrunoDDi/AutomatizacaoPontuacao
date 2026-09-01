# Automação de Validação de Pedidos

Script em Python para automatizar a validação de elegibilidade de pedidos (Parceiro / Mídia / Campanha), eliminando um processo que antes era feito manualmente, um pedido por vez.

## 🎯 Problema

O processo de validação exigia, para cada pedido:
1. Acessar o sistema e consultar o número do pedido manualmente
2. Verificar se os dados de Parceiro, Mídia e Campanha estavam corretos
3. Anotar o resultado (Elegível / Não elegível)
4. Repetir o processo em outro sistema para registrar a informação

Feito pedido a pedido, isso consumia tempo e era repetitivo — o cenário ideal para automação.

## 💡 Solução

O script combina duas abordagens:

- **Selenium**: acessa o sistema web, consulta cada número de pedido e captura o resultado da validação (Elegível / Não elegível)
- **pandas**: lê uma planilha de entrada com múltiplos números de pedido, roda a consulta em lote para cada um, e gera uma planilha de saída consolidada com os resultados
- **PyAutoGUI**: usado na etapa final para inserir os dados validados em uma aplicação desktop (não-web) da empresa

## 🛠️ Tecnologias

- Python
- Selenium
- pandas
- PyAutoGUI

## ⚙️ Como funciona (fluxo)

```
Planilha de entrada (números de pedido)
        ↓
   Selenium consulta cada pedido no sistema
        ↓
   Compara Parceiro / Mídia / Campanha
        ↓
   Resultado: Elegível ou Não elegível
        ↓
Planilha de saída consolidada
```

## 📌 Status

Projeto em desenvolvimento. Próximos passos:
- [ ] Consolidar o loop de consulta em lote via pandas
- [ ] Tratar casos de divergência com uma rotina específica
- [ ] Automatizar a etapa final de inserção de dados via PyAutoGUI

## ⚠️ Nota

Este repositório é uma versão didática do projeto, com dados fictícios de exemplo. Informações internas, credenciais e dados reais de pedidos/clientes não são incluídos por questões de confidencialidade.
