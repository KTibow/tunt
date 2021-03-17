"""Custom simple template engine for HTML."""

import yaml

with open("assets/template.html") as template_code:
    base_html = template_code.read()


def compile_template(config_file):
    """Compile a template into an HTML file.

    Args:
        config_file: A stream object, like returned from open.

    Returns:
        A string containing the compiled HTML.
    """
    config_file = yaml.safe_load(config_file)
    compiled_styles = ""
    compiled_scripts = ""
    for style in config_file["styles"]:
        compiled_styles += f"<link rel='stylesheet' href='{style}'/>"
    for script in config_file["scripts"]:
        compiled_scripts += f"<script src='{script}'></script>"
    return (
        base_html.replace("=title=", config_file["title"])
        .replace("=content=", config_file["content"])
        .replace("=styles=", compiled_styles)
        .replace("=scripts=", compiled_scripts)
    )
