import inspect
import os
import re

def generate_api_documentation(module, output_file='api_docs.md'):
    """
    Generate API documentation for a Python module.

    Args:
        module (module): The Python module to document.
        output_file (str, optional): The output file path for the generated documentation. Defaults to 'api_docs.md'.
    """
    documentation = []

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) or inspect.isclass(obj):
            documentation.append(generate_object_documentation(name, obj))

    with open(output_file, 'w') as f:
        f.write('\n'.join(documentation))

    print(f'API documentation generated: {output_file}')

def generate_object_documentation(name, obj):
    """
    Generate documentation for a Python object (function or class).

    Args:
        name (str): The name of the object.
        obj (function or class): The Python object to document.

    Returns:
        str: The generated documentation.
    """
    doc = inspect.getdoc(obj)
    if doc:
        doc = re.sub(r'\n\s*\n', '\n\n', doc.strip())
    else:
        doc = 'No documentation available.'

    if inspect.isfunction(obj):
        params = inspect.signature(obj).parameters
        param_docs = [f'- **{name}**: {param.annotation}' for name, param in params.items()]
        return f'## {name}()\n\n{doc}\n\n**Parameters:**\n\n{"\n".join(param_docs)}'
    elif inspect.isclass(obj):
        return f'## class {name}\n\n{doc}'
    else:
        return ''


