from string import Template

import click


@click.command()
@click.argument('pairs', nargs=-1)
@click.argument('target_file', nargs=1)
@click.option('--output', '-o', required=False, type=click.Path())
def cmd(pairs, target_file, output):
    try:
        context = {pair.split('=')[0]: pair.split('=')[1] for pair in pairs}
        with open(target_file) as f:
            t = Template(f.read())
        if output:
            with open(output, 'w') as f:
                f.write(t.substitute(context))
        else:
            click.echo(t.substitute(context))
    except IndexError:
        click.echo('Each arguments must be include "=".')
    except KeyError as e:
        click.echo(f'Not found: {e}')


if __name__ == '__main__':
    cmd()

