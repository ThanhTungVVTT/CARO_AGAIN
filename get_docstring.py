import ast
from menu import *
def extract_docstrings(file_path):
    docstrings = []

    # Phân tích cú pháp của file
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    # Lặp qua các nút của cây cú pháp
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            docstrings.append((node.name, ast.get_docstring(node)))
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    docstrings.append((f"{item.name}", ast.get_docstring(item)))
        elif isinstance(node, ast.FunctionDef):
            docstrings.append((node.name, ast.get_docstring(node)))

    return docstrings

docstrings = extract_docstrings('game.py')+extract_docstrings('menu.py')+extract_docstrings('board.py')+extract_docstrings('button.py')+extract_docstrings('player.py')

# In ra tên và docstring của các lớp và hàm
for name, docstring in docstrings:
    print(f"{name}")
    print(f"  {docstring}")
    print()