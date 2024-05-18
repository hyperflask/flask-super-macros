# Flask-Super-Macros

Super charged Jinja macros for Flask using [Jinja Super Macros](https://github.com/hyperflask/jinja-super-macros).

- Inspired by frontend component frameworks
- Use macros like html components
- Auto macro loader
- Compatible with [Storybook](https://storybook.js.org/)

## Installation

    pip install flask-super-macros

## Usage

```python
from flask import Flask
from flask_super_macros import SuperMacros

app = Flask(__name__)
SuperMacros(app)
```

Macros will be automatically registered from:

 - Macro defined using the `macro` directive in all template files called `__macros__.html`
 - Created from files with the extension `.macro.html`
 - Created from files in the `macros` folder

*(Note: [creating macros from files]() is the equivalent of wrapping the whole file in a macro directive)*

Example `macros/btn.html`:

```
<{button class="btn" **kwargs}>{{ inner }}</{}>
```

You can then use this macro in any template (no need to import):

```
<{ btn onclick="alert('hello')" }>click me</{ btn }>
```

See [Jinja Super Macros documentation]() to learn more about the new macro calling syntax.

To register macros from other files, the [macro registry]() is available under ̀`app.macros`:

```python
app.macros.register_from_template("macros.html")
```

You can also [create macros fron functions]() using `app.macro`:

```python
from jinja_super_macros import html_class

@app.macro
def btn(**kwargs):
    """<{button class="btn" **kwargs}>{{ inner }}</{}>"""
```

## Storybook

Registered jinja macros can be viewed in Storybook using the server renderer.

Initialize your storybook project:

    npx storybook@latest init -t server

(Optionnaly, empty the stories folder first to remove examples)

Create story files:

    flask create-macro-stories --watch