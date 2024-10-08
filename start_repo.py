import os
import re

topics = {
    "1. Estruturas de Dados e Algoritmos": {
        "Estruturas de Dados": [
            "Arrays e Listas",
            "Pilhas e Filas",
            "Conjuntos e Dicionários (JavaScript: Set, Map; Python: set, dict)",
            "Árvores (Binárias, AVL, Trie)",
            "Grafos (BFS, DFS)",
            "Listas ligadas (simples e duplamente encadeadas)",
            "Heaps (Max-Heap, Min-Heap)",
            "Hashing e tabelas hash"
        ],
        "Algoritmos": [
            "Ordenação (Bubble, Merge, Quick, etc.)",
            "Pesquisa (Linear, Binária)",
            "Algoritmos de grafos (BFS, DFS, Dijkstra)",
            "Backtracking",
            "Programação dinâmica (ex.: problema da mochila)",
            "Algoritmos de busca em profundidade e largura"
        ]
    },
    "2. Manipulação de Strings e Arrays": {
        "Operações com Strings": [
            "Comparações",
            "Substrings e subsequências",
            "Manipulação de caracteres",
            "Problemas como anagramas, palíndromos, regex simples"
        ],
        "Operações com Arrays": [
            "Ordenação e busca",
            "Rotação de arrays",
            "Mapeamento, filtragem e redução",
            "Desduplicação e remoção de elementos"
        ]
    },
    "3. Programação Orientada a Objetos (POO)": {
        "Conceitos de POO": [
            "Classes e Objetos",
            "Herança e Polimorfismo",
            "Encapsulamento",
            "Abstração",
            "Métodos estáticos e de classe"
        ]
    },
    "4. Funções e Escopo": {
        "Funções": [
            "Definição e invocação",
            "Funções de ordem superior",
            "Closures (JavaScript: escopo léxico; Python: funções aninhadas)",
            "Currying e composição"
        ],
        "Escopo e Contexto": [
            "Escopo de variáveis (global, local)",
            "Hoisting (JavaScript)",
            "this e contexto (JavaScript)",
            "global e nonlocal (Python)"
        ]
    },
    "5. Tratamento de Erros e Exceções": {
        "Tratamento de Erros": [
            "Blocos try-except em Python",
            "Blocos try-catch em JavaScript",
            "Lidando com exceções customizadas"
        ]
    },
    "6. Assíncronismo e Concorrência": {
        "JavaScript": [
            "Callbacks",
            "Promises (.then, .catch)",
            "async/await",
            "Event Loop e ciclo de vida assíncrono"
        ],
        "Python": [
            "asyncio e await",
            "Threads e multiprocessing",
            "GIL (Global Interpreter Lock)"
        ]
    },
    "7. Estruturas de Controle de Fluxo": {
        "Controle de Fluxo": [
            "Condicionais (if, else, elif)",
            "Laços (for, while)",
            "Compreensões de lista (Python)",
            "Iteradores e geradores (yield em Python)"
        ]
    },
    "8. Manipulação de Arquivos e I/O": {
        "I/O e Arquivos": [
            "Leitura e escrita de arquivos",
            "Operações de I/O assíncronas",
            "Entrada e saída padrão"
        ]
    },
    "9. Técnicas de Otimização e Complexidade": {
        "Otimização e Complexidade": [
            "Análise de complexidade de tempo e espaço (Notação Big O)",
            "Otimização de algoritmos",
            "Estratégias para melhorar a eficiência"
        ]
    },
    "10. Estruturas Específicas de Linguagem": {
        "JavaScript": [
            "Protótipos e herança prototípica",
            "this e bind, call, apply",
            "Manipulação do DOM",
            "let, const e var",
            "Desestruturação e espalhamento (...)",
            "Arrow functions e contexto de this"
        ],
        "Python": [
            "Decoradores",
            "Geradores e yield",
            "Compreensões (list, dict, set)",
            "Context Managers (with)",
            "Módulos e pacotes (import)"
        ]
    },
    "11. Testes": {
        "Testes Unitários": [
            "Bibliotecas de teste (JavaScript: Jest, Mocha; Python: unittest, pytest)",
            "Mocking",
            "TDD (Test Driven Development)"
        ]
    },
    "12. Técnicas de Depuração e Ferramentas": {
        "Depuração": [
            "Uso do console.log (JavaScript) e print (Python)",
            "Uso de ferramentas de depuração no navegador",
            "Uso do pdb em Python para debugging"
        ],
        "Ferramentas": [
            "Linters (ESLint para JavaScript, Pylint para Python)",
            "Analisadores estáticos (TypeScript para JavaScript, MyPy para Python)"
        ]
    },
    "13. Paradigmas de Programação": {
        "Funcional": [
            "Imutabilidade",
            "Funções puras",
            "Aplicação de funções (map, filter, reduce)"
        ],
        "Event-Driven": [
            "Eventos e Listeners (JavaScript, especialmente para programação frontend)"
        ]
    },
    "14. Estruturas Avançadas": {
        "Python": [
            "Collections (namedtuple, Counter, defaultdict)",
            "Manipulação de iteradores e geradores avançados"
        ],
        "JavaScript": [
            "Trabalhar com objetos complexos (Object.assign, Object.entries)",
            "Classes (ES6+)",
            "Proxy e Reflect"
        ]
    },
    "15. Web e APIs": {
        "JavaScript": [
            "Manipulação do DOM",
            "Requisições HTTP (Fetch API, axios)",
            "Manipulação de JSON"
        ],
        "Python": [
            "Requisições HTTP (requests, http.client)",
            "Parsing de JSON e XML"
        ]
    },
    "16. Padrões de Projeto": {
        "Padrões Comuns": [
            "Singleton, Factory, Observer",
            "Pub/Sub (especialmente relevante no JavaScript)",
            "Decorator (Python)"
        ]
    },
    "17. Problemas Clássicos": {
        "Problemas Comuns": [
            "Problemas de FizzBuzz",
            "Algoritmos de anagramas e palíndromos",
            "Sequências de Fibonacci e fatoriais",
            "Problemas de Two Sum, Reverse Linked List, Merge Sorted Lists"
        ]
    },
    "18. Conhecimento de Frameworks e Ferramentas": {
        "JavaScript": [
            "Node.js (event loop, pacotes)",
            "Express.js (básico de APIs)"
        ],
        "Python": [
            "Flask/Django (básico de APIs)",
            "asyncio para programação assíncrona"
        ]
    }
}

def sanitize_path(path):
    # Remove caracteres não permitidos em nomes de diretórios no Windows
    return re.sub(r'[<>:"/\\|?*]', '_', path)

def create_folder_structure(topics, base_path="."):
    for topic, subtopics in topics.items():
        # Criar a pasta principal
        sanitized_topic = sanitize_path(topic)
        topic_path = os.path.join(base_path, sanitized_topic)
        os.makedirs(topic_path, exist_ok=True)
        
        # Criar o README.md da pasta principal
        readme_path = os.path.join(topic_path, "README.md")
        with open(readme_path, "w") as readme_file:
            readme_file.write(f"# {topic}\n\n")
            if subtopics:
                readme_file.write("## Subtópicos\n\n")
                for subtopic in sorted(subtopics):
                    sanitized_subtopic = sanitize_path(subtopic)
                    subtopic_path = sanitized_subtopic.replace(" ", "%20")  # Para links com espaços
                    readme_file.write(f"- [{subtopic}]({subtopic_path}/README.md)\n")
        
        # Criar subpastas, se houver
        for subtopic, subsubtopics in subtopics.items():
            sanitized_subtopic = sanitize_path(subtopic)
            subtopic_path = os.path.join(topic_path, sanitized_subtopic)
            os.makedirs(subtopic_path, exist_ok=True)
            
            # Criar o README.md da subpasta
            sub_readme_path = os.path.join(subtopic_path, "README.md")
            with open(sub_readme_path, "w") as sub_readme_file:
                sub_readme_file.write(f"# {subtopic}\n\n")
                if subsubtopics:
                    sub_readme_file.write("## Subtópicos\n\n")
                    for subsubtopic in sorted(subsubtopics):
                        sanitized_subsubtopic = sanitize_path(subsubtopic)
                        subsubtopic_path = sanitized_subsubtopic.replace(" ", "%20")  # Para links com espaços
                        sub_readme_file.write(f"- [{subsubtopic}]({subsubtopic_path}/README.md)\n")
                else:
                    sub_readme_file.write(f"Este é o README para o subtopico {subtopic}.\n")
            
            # Criar subsubpastas, se houver
            for subsubtopic in sorted(subsubtopics):
                sanitized_subsubtopic = sanitize_path(subsubtopic)
                subsubtopic_path = os.path.join(subtopic_path, sanitized_subsubtopic)
                os.makedirs(subsubtopic_path, exist_ok=True)
                
                # Criar o README.md da subsubpasta
                subsub_readme_path = os.path.join(subsubtopic_path, "README.md")
                with open(subsub_readme_path, "w") as subsub_readme_file:
                    subsub_readme_file.write(f"# {subsubtopic}\n\n")
                    subsub_readme_file.write(f"Este é o README para o subtopico {subsubtopic}.\n")

if __name__ == "__main__":
    create_folder_structure(topics)
    print(f"Estrutura de pastas criada na raiz do diretório atual.")