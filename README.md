# 🤖 Agente Inteligente para Notas Fiscais - Jan/2024

Este é um projeto de um agente inteligente de perguntas e respostas desenvolvido com Python, Streamlit e LangChain. Ele responde, em linguagem natural, perguntas sobre um arquivo CSV contendo notas fiscais emitidas em Janeiro de 2024.

---

## 🔍 O que ele faz?

Com base no conteúdo do arquivo `202401_NFs_Cabecalho.csv`, o agente:

- Analisa os dados usando **Python** e **pandas**;
- Interage por meio de **perguntas em linguagem natural**;
- Usa um **modelo de linguagem (LLM)** via **OpenAI** (ex: `gpt-3.5-turbo`);
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
.venv\Scripts\activate         # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
```

> ⚠️ **Nunca compartilhe sua chave pública.** O uso de `.env` garante mais segurança.

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
├── .env                 # (adicionado pelo usuário, não subir no GitHub)
├── README.md
└── images/
    └── logo.jpg
```

---

## 🧠 Modelo Utilizado

Este projeto agora usa o modelo oficial da **OpenAI**: `gpt-3.5-turbo`.  
Você pode alterá-lo para `gpt-4` ou outro, ajustando o arquivo `agente.py`.

---

## 📌 Observações

- O agente sempre responde em **português do Brasil**;
- Se não encontrar a informação, ele informa isso de forma educada;
- O agente utiliza **LangChain + PythonREPLTool** para interpretar comandos e consultar o DataFrame carregado.

---

## 👨‍🏫 Desenvolvido por

Projeto acadêmico desenvolvido por **Dallan Borgheresi** para o curso da I2A2 (Tarefa 2).

---

🧠 Com tecnologia: Python + LangChain + OpenAI + Streamlit
