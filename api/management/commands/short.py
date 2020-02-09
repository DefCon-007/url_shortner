import djclick as click
from api.models import ShortUrls
from djclick.params import ModelInstance
from api.helper import add_new_url, add_list_of_urls
from api.exceptions import InvalidURLException
from django.conf import settings

@click.command()
@click.option('--url', help='The URL to be shortened')
@click.option('--name', default=None, help='Name to use as placeholder for long url')
@click.option('--file', default=None, help='Please give the full path of URL file.')
@click.option('--out', default=None, help='(Optional) Please give the full path of file to store short names.')
def command(url, name, file, out):
    if file:
        with open(file, "r") as f:
            data = []
            for line in f:
                if line.strip():
                    li = line.split(" ")
                    if len(li) == 1:
                        li.append(None)
                    data.append(li)
            short_names = add_list_of_urls(data)
            names_str = "\n".join(short_names)
            if out:
                with open(out, 'w+') as o:
                    o.write(names_str)
                click.secho("Short URLs saved at {}".format(out), fg="green")
            else:
                click.secho("Following are the short names for given URL", fg="green")
                for i in short_names:
                    click.secho("http://{}/{}".format(settings.BASE_URL,i))
    if url:
        try:
            short = add_new_url(url, name)
            click.secho("Short URL created. Goto http://{}/{}".format(settings.BASE_URL, short), fg="green")
        except InvalidURLException:
            click.secho("Invalid URL please try again!", fg="red")
        except Exception as e:
            click.secho(e)
            click.secho('Unable to shorten the given URL, try again!', fg='red')