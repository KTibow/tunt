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
    return (
        base_html.replace("=title=", config_file["title"])
        .replace("=content=", config_file["content"])
        .replace(
            "=styles=",
            "\n".join(
                [
                    f"<link rel='stylesheet' href='{style}'/>"
                    for style in config_file["styles"]
                ]
            ),
        )
        .replace(
            "=scripts=",
            "\n".join(
                [
                    f"<script src='{script}'></script>"
                    for script in config_file["scripts"]
                ]
            ),
        )
    )
