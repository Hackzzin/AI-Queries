# AI-Queries
A repo that contains the code used for Web Semantic Project. 

## How the code works
The code's objective is to generate prompts through the use of Meta's open-source Llama3 model for 9 different set of questions refering to a database of Employees, Departments, Salaries and such. For each of the questions, it will generate two prompts: one SQL prompt, and one SPARQL prompt.

### Files
`resources` -> Folder containing the SQL_DDL and the ontology serialized in .ttl format.

`resources\employee.ttl` -> .ttl file with the ontology describing the relational database.

`resources\sql_ddl.txt` a .txt file with the DDL of the relational database.

### How to run

This project uses [Ollama](https://ollama.com/) to run Meta's open-source **LLaMA 3** model locally, which is then accessed by a Python script to generate **SQL** and **SPARQL** queries based on 9 natural language questions.

Each question will generate two output files:
- One with a **SQL query** (based on the `sql_ddl.txt` file)
- One with a **SPARQL query** (based on the `employee.ttl` ontology)

---

#### 1. Requirements

- Python 3.8 or higher
- Internet connection (first-time model download)
- [Ollama installed](https://ollama.com/) (see below)

---

#### 2. Installing and Running Ollama

##### On Windows

1. Visit [https://ollama.com/download](https://ollama.com/download) and download the Windows installer.
2. Run the `.msi` file and follow the steps to complete installation.
3. **Restart your terminal** (CMD or PowerShell) to ensure the `ollama` command is recognized.
4. In the terminal, start the LLaMA 3 model:

   ```bash
   ollama run llama3

##### On Linux

1. Run
   
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
2. Restart the terminal.
3. Run
   ```bash
   ollama run llama3

#### 3. Running genQuery.py

Run 
   ```bash
   python genQuery.py
