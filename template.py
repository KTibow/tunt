"""Custom simple template engine for HTML."""

import yaml


def compile_template(config_file):
    """Compile a template into an HTML file.

    Args:
        config_file: A stream object, like returned from open.

    Returns:
        A string containing the compiled HTML.
    """
    config_file = yaml.safe_load(config_file)
    styles = "\n".join(
        [
            f"<link rel='stylesheet' href='/asset/css/{style}'/>"
            for style in config_file["styles"]
        ]
    )
    scripts = "\n".join(
        [
            f"<script src='/asset/js/{script}'></script>"
            for script in config_file["scripts"]
        ]
    )
    return f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{config_file["title"]}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        {styles}
    </head>
    <body>
        {config_file["content"]}
        {scripts}
    </body>
</html>
"""
