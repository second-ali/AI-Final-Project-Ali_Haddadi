#!/usr/bin/env pythoh
# -*- encoding: utf-8 -*-

import emojies


def demojizePersian(input_text):
    no_emoji_text = emojies.replace(input_text)
    return no_emoji_text
