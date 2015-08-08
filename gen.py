#!/usr/bin/env python2

from __future__ import unicode_literals
from __future__ import print_function

import random
import cairo


WIDTH  = 533
HEIGHT = 533
CAPTION_HEIGHT = 150


HEADS = [
        'el',
        'wo',
        'rat',
        'cat',
        'dog',
        'dolph',
        'snak',
        ]
TAILS = [
        'opus',
        'fog',
        'cat',
        'dog',
        'phin',
        'nake',
        ]


def load_png(f):
    img = cairo.ImageSurface.create_from_png(f)
    if img.get_width() != WIDTH:
        raise Exception('{}: Wrong width {}'.format(f.name, img.get_width()))
    if img.get_height() != HEIGHT:
        raise Exception('{}: Wrong height {}'.format(f.name, im.get_height()))
    return img

def draw(f_head, f_tail):
    img =  cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT + CAPTION_HEIGHT)
    ctx = cairo.Context(img)

    ctx.set_source_rgb(1,1,1)
    ctx.paint()

    head_img = load_png(f_head)
    tail_img = load_png(f_tail)

    ctx.set_source_surface(tail_img)
    ctx.paint()
    ctx.set_source_surface(head_img)
    ctx.paint()

    ctx.select_font_face('PT Mono', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(50)
    x_bearing, y_bearing, width, height = ctx.text_extents(name)[:4]
    ctx.move_to(0.5 * WIDTH - width / 2 - x_bearing, HEIGHT + 0.5 * CAPTION_HEIGHT - height / 2 - y_bearing)
    ctx.text_path(name)

    ctx.set_source_rgb(0,0,0)
    ctx.stroke_preserve()
    ctx.set_source_rgb(1,1,0)
    ctx.fill()

    return img



if __name__ == '__main__':
    head = random.choice(HEADS)
    tail = random.choice(TAILS)

    vowels = {'a', 'e', 'i', 'o', 'u'}
    mid = '' if head[-1] in vowels or tail[0] in vowels else 'o'
    name = head + mid + tail

    with open('in/{}-head.png'.format(head), 'rt') as f_head:
        with open('in/{}-tail.png'.format(tail), 'rt') as f_tail:
            img = draw(f_head, f_tail)
            img.write_to_png('{}.png'.format(name))
            print(name)
