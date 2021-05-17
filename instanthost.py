import mimetypes

import click
import requests

host_api = "http://instant-host.herokuapp.com/api/host"
edit_api = "http://instant-host.herokuapp.com/api/edit"


def TinyShortner(big_url: str) -> str:
    """
    Function short the big urls to tiny by Tiny Api
    """
    return requests.post(
        "https://tinyurl.com/api-create.php", data={"url": big_url}
    ).text


@click.command()
@click.argument("file")
@click.option("--edit", help="To Edit or Update your file", is_flag=True)
@click.option("--key", default="", help="Your Private Key to edit or update")
def run(file, edit, key):
    """ Host page or file from your Terminal """

    with open(file, "r") as file_obj:
        try:
            source = file_obj.read()
        except UnicodeDecodeError:
            click.echo("👎 Binary file are not supported 😞")
            exit()
    if edit:
        response = requests.post(edit_api, json={"source": source, "key": key})
    else:
        mimetype = mimetypes.guess_type(file)[0]
        if mimetype:
            response = requests.post(
                host_api, json={"source": source, "mimetype": mimetype}
            )
        else:
            click.echo("👎 Unable Detect the Mimetype of the File 😞")
            exit()

    data = response.json()
    short_url = TinyShortner(data["hosted_at"])
    data.update({"tiny_url": short_url})
    click.echo("✌️  Hosted Successfully ✨" + "\n")
    for i, j in data.items():
        click.echo(f"{i}: {j}" + "\n")


if __name__ == "__main__":
    run()
