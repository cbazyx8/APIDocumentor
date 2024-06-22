# 📝 API Documentation Generator

This Python script can automatically generate API documentation for your Python modules. It uses the docstrings and function signatures to create a clean and easy-to-read Markdown file.

## 🚀 How it Works

1. The script takes a Python module as input.
2. It goes through all the functions and classes in the module.
3. For each one, it extracts the docstring and the parameter information.
4. It then formats this information into a Markdown-formatted documentation.
5. Finally, it writes the generated documentation to an output file.

## 🛠️ Usage

1. Make sure you have Python installed on your machine.
2. Save the script to a file, e.g., `api_doc_generator.py`.
3. In your Python project, import the module you want to document and run the `generate_api_documentation` function:

   ```python
   import my_module
   from api_doc_generator import generate_api_documentation

   generate_api_documentation(my_module, 'my_module_docs.md')
   ```

4. The documentation will be saved to the `my_module_docs.md` file in the current directory.

## 💻 Example Output

The generated documentation will look like this:

```
## my_function()

This is the docstring for the my_function() function.

**Parameters:**

- **arg1**: str
- **arg2**: int

## class MyClass

This is the docstring for the MyClass class.
```

## 🤝 Contributing

If you have any ideas for improvements or find any issues, feel free to open a pull request or submit an issue on the project's repository. We'd love to hear your feedback and work together to make this tool even better!

## 📜 License

This project is licensed under the [MIT License](LICENSE). You're free to use, modify, and distribute the code as per the terms of the license.

