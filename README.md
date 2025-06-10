
# 🤖 Agente Inteligente para Notas Fiscais - Jan/2024

Este é um projeto de um agente inteligente de perguntas e respostas desenvolvido com Python, Streamlit e LangChain. Ele responde, em linguagem natural, perguntas sobre um arquivo CSV contendo notas fiscais emitidas em Janeiro de 2024.

---

## 🔍 O que ele faz?

Com base no conteúdo do arquivo `202401_NFs_Cabecalho.csv`, o agente:

- Analisa os dados usando **Python** e **pandas**;
- Interage por meio de **perguntas em linguagem natural**;
- Usa um **modelo de linguagem (LLM)** via [OpenRouter](https://openrouter.ai) (ex: `mistralai/mixtral-8x7b-instruct`);
- Apresenta os resultados de forma **clara, objetiva e em português do Brasil**.

---

## 📦 Requisitos

- Python **3.10+**
- pip (gerenciador de pacotes)

---

## ⚙️ Instalação Local

1. Clone o repositório:

```bash
git clone https://github.com/Dallan99/I2A2---Tarefa2---NF
cd I2A2---Tarefa2---NF
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate       # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Defina a variável de ambiente com sua chave da OpenRouter:

```bash
# Linux/macOS
export OPENROUTER_API_KEY="sua-chave-aqui"

# Windows (cmd)
set OPENROUTER_API_KEY="sua-chave-aqui"
```

> ⚠️ Não adicione sua chave ao código ou ao GitHub. Use variáveis de ambiente.

5. Execute o aplicativo Streamlit:

```bash
streamlit run app.py
```

---

## 💡 Exemplos de Perguntas

- Qual o valor total das notas fiscais?
- Quais estados mais emitiram notas?
- Quem são os principais destinatários?
- Quantas notas foram emitidas por CNPJ?

---

## 📁 Estrutura do Projeto

```
📦 I2A2---Tarefa2---NF/
├── app.py
├── agente.py
├── 202401_NFs_Cabecalho.csv
├── requirements.txt
├── README.md
└── images/
    └── logo.jpg
```

---

## 🧠 Modelo Utilizado

Este projeto usa um modelo gratuito da OpenRouter: `mistralai/mixtral-8x7b-instruct`.  
Você pode alterá-lo no arquivo `agente.py` conforme sua necessidade.

---

## 📌 Observações

- O agente sempre responderá em **português do Brasil**;
- Se não encontrar a informação, ele dirá de forma educada que não conseguiu localizar nos dados disponíveis.

---

## 👨‍🏫 Desenvolvido por

Projeto acadêmico desenvolvido por Dallan Borgheresi para o curso da I2A2 (Tarefa 2).

---

🧠 Com tecnologia: Python + LangChain + OpenRouter + Streamlit
