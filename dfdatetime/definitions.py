# -*- coding: utf-8 -*-
"""The date and time definitions.

Also see:
  https://en.wikipedia.org/wiki/Day
  https://en.wikipedia.org/wiki/Hour
  https://en.wikipedia.org/wiki/Minute
"""

PRECISION_1_DAY = u'1d'
PRECISION_1_HOUR = u'1h'
PRECISION_1_NANOSECOND = u'1ns'
PRECISION_100_NANOSECONDS = u'100ns'
PRECISION_1_MICROSECOND = u'1us'
PRECISION_1_MILLISECOND = u'1ms'
PRECISION_1_MINUTE = u'1min'
PRECISION_1_SECOND = u'1s'
PRECISION_2_SECONDS = u'2s'

PRECISION_VALUES = frozenset([
    PRECISION_1_DAY,
    PRECISION_1_HOUR,
    PRECISION_1_NANOSECOND,
    PRECISION_100_NANOSECONDS,
    PRECISION_1_MICROSECOND,
    PRECISION_1_MILLISECOND,
    PRECISION_1_MINUTE,
    PRECISION_1_SECOND,
    PRECISION_2_SECONDS])
