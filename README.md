# Automa_Check_Pagamento

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium" />
  <img src="https://img.shields.io/badge/Excel-.xlsx-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" alt="Excel" />
  <img src="https://img.shields.io/badge/Automation-Status%20Check-FF6B6B?style=for-the-badge" alt="Automation" />
</p>

Automatização de verificação de pagamento fazendo leitura de arquivo `.xlsx` e usando Selenium para verificar status via web.

---

## Visão Geral

O projeto `Automa_Check_Pagamento` foi desenvolvido para automatizar a checagem de pagamentos a partir de uma planilha Excel (`.xlsx`), acessando uma interface web via Selenium para confirmar o status de cada registro de forma rápida e eficiente.

A ideia central é reduzir a necessidade de validação manual, evitar erros operacionais e acelerar processos repetitivos de conferência de pagamentos.

Este tipo de automação é especialmente útil em cenários onde:
- há grande volume de registros;
- os dados são enviados em planilhas;
- a confirmação do status do pagamento precisa ser feita em um sistema web;
- a operação é repetitiva e pode ser automatizada.

---

## Funcionalidades

- leitura automática de arquivos `.xlsx`;
- processamento de registros em lote;
- acesso automatizado a páginas web com Selenium;
- verificação do status de pagamento;
- registro de resultados por item;
- possibilidade de exportação ou organização dos dados processados;
- execução de tarefas repetitivas sem intervenção manual;
- base para automações mais robustas e escaláveis.

---

## Stack Tecnológica

| Tecnologia | Uso |
| --- | --- |
| Python | Lógica principal da automação |
| Selenium | Automação de navegação e verificação no navegador |
| Pandas | Leitura e manipulação de arquivos Excel |
| OpenPyXL / Excel reader | Leitura de arquivos `.xlsx` |
| WebDriver | Acesso ao navegador para automação |

---

## Requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.9+
- pip
- Google Chrome ou outro navegador compatível
- ChromeDriver correspondente à sua versão do navegador
- Git

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/KleyJkGameDev/Automa_Check_Pagamento.git
cd Automa_Check_Pagamento
