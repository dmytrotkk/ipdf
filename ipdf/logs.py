import sys
import logging
import colorful as cf

from ipdf.constants import PALETTE, LINE


cf.use_style('solarized')


def color_args_str(args, title=None, type='info'):
    s = cf.blue(f'\n{LINE}\n')
    if title:
        with cf.with_palette(PALETTE) as c:
            if type == 'error':
                s += f'{c.bold_error(title)}\n'
            elif type == 'success':
                s += f'{c.bold_success(title)}\n'
            else:
                s += f'{c.bold_info(title)}\n'
    for k in args:
        s += f'{cf.bold_violet(k)}: '
        s += f'{args[k]}\n'
    s += cf.blue(f'{LINE}\n')
    return s


def init_logger():
    handlers = []
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    handlers.append(stream_handler)

    logging.basicConfig(level=logging.DEBUG, handlers=handlers)
