# AI-Queries
A repo that contains the code used for Web Semantic Project. 

## How the code works
The code's objective is to generate prompts through the use of Meta's open-source Llama3 model for 9 different set of questions refering to a database of Employees, Departments, Salaries and such. For each of the questions, it will generate two prompts: one SQL prompt, and one SPARQL prompt.

### Files
`resources` -> Folder containing the SQL_DDL and the ontology serialized in .ttl format.

`resources\employee.ttl` -> .ttl file with the ontology describing the relational database.

`resources\sql_ddl.txt` a .txt file with the DDL of the relational database.
