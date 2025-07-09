import os
import requests
from pathlib import Path

# Paths
base_dir = Path(__file__).parent
resources = base_dir / "resources"
output_dir = base_dir / "resulting_queries"
output_dir.mkdir(exist_ok=True)

# Load input files
sql_ddl = (resources / "sql_ddl.txt").read_text(encoding="utf-8")
ttl_ontology = (resources / "employee.ttl").read_text(encoding="utf-8")

# LLaMA Model Config (Ollama)
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

perguntas = ["Quais são os nomes de todos os departamentos?",
             "Qual é o maior e o menor salário?",
             "Liste todos os empregados contratados antes de 1986.",
             "Qual é o intervalo salarial entre os gerentes?",
             "Quantos cargos diferentes temos?",
             "Quantos empregados são homens? Quantos são mulheres?",
             "Liste, por departamento, os cargos e a média salarial dos empregados por cargos.",
             "Liste, por empregados, os seus departamentos trabalhados e seus respectivos salários na época.",
             "Liste os gerentes de departamento contratados antes de 1991 e seus salários atuais."]

def generate_query_SQL(question, context, query_type):
    prompt = f"""
Dada uma base de dados descrita pelo DDL a seguir: {query_type.upper()} query que responda à pergunta abaixo.

{context}

Escreva uma {query_type.upper()} query que responda à pergunta abaixo. Responda apenas com a query, sem nenhuma explicação, tal que seja possível rodar a query palavra-por-palavra da sua resposta.

"{question}"

""".strip()

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        raise Exception(f"Erro ao consultar LLaMA: {response.text}")
    
    
def generate_query_SPARQL(question, context, query_type):
    prompt = f"""
Dada uma base de dados descrita pelo DDL a seguir: {query_type.upper()} query que responda à pergunta abaixo.

{context}

Escreva uma {query_type.upper()} query que responda à pergunta abaixo. Responda apenas com a query, sem nenhuma explicação, tal que seja possível rodar a query palavra-por-palavra da sua resposta.

"{question}"
""".strip()

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        raise Exception(f"Erro ao consultar LLaMA: {response.text}")

def genQuery():
    for i, pergunta in enumerate(perguntas, 1):
        sql_query = generate_query_SQL(pergunta, sql_ddl, "SQL")
        sparql_query = generate_query_SPARQL(pergunta, ttl_ontology, "SPARQL")

        (output_dir / f"q{i:02d}_sql.txt").write_text(sql_query, encoding="utf-8")
        (output_dir / f"q{i:02d}_sparql.txt").write_text(sparql_query, encoding="utf-8")

    print("Queries geradas com sucesso em:", output_dir)

if __name__ == "__main__":
    genQuery()