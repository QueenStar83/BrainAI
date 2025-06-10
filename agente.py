import os
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_experimental.tools.python.tool import PythonREPLTool
from dotenv import load_dotenv
load_dotenv()


def criar_agente(caminho_csv: str):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    print("API KEY:", openai_api_key)
    if not openai_api_key:
        raise ValueError("A variável de ambiente OPENAI_API_KEY não está definida.")

    # Carrega o CSV
    df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8', on_bad_lines='skip')

    # Contexto global com DataFrame df
    global_context = {"df": df}

    ferramenta_execucao = PythonREPLTool(locals=global_context)

    ferramentas = [
        Tool(
            name="Execução Python com pandas",
            func=ferramenta_execucao.run,
            description="Use esta ferramenta para responder perguntas com base no DataFrame `df`, que contém as notas fiscais."
        )
    ]

    llm = ChatOpenAI(
        temperature=0.3,
        model="gpt-3.5-turbo",
        openai_api_key=openai_api_key
    )

    prefixo = """Você é um agente inteligente especializado em análise de notas fiscais.

Seu objetivo é responder exclusivamente em **Português do Brasil**, de forma clara, educada e acessível, mesmo que a pergunta seja feita em outro idioma.

Você analisa o DataFrame chamado `df`, que contém as Notas Fiscais emitidas em Janeiro de 2024.

Você pode usar pandas e Python para calcular, filtrar ou resumir os dados conforme necessário.
Seja cordial e amigável em suas respostas, evitando jargões técnicos.

⚠️ NUNCA responda em inglês. NUNCA diga que é um modelo de linguagem. Caso perguntem "o que você é", diga:

"Sou um agente inteligente de análise de Notas Fiscais, treinado para responder perguntas com base nos dados disponíveis no sistema."

Caso não saiba a resposta, responda de forma amigável em português dizendo que não encontrou a informação solicitada nos dados disponíveis.
"""

    agente = initialize_agent(
        tools=ferramentas,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        agent_kwargs={"prefix": prefixo},
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=50,
        max_execution_time=500
    )

    return agente
