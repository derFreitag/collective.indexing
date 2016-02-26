import warnings

warnings.warn(
    '2.0b1 was the last release of collective.indexing. '
    'Starting with Plone 5.X.Y its code has already merged in. '
    'For more information and upgrade information, see its PLIP: '
    'https://github.com/plone/Products.CMFPlone/issues/1343',
    DeprecationWarning,
)

def initialize(context):
    # apply the monkey patches...
    from collective.indexing import monkey
    monkey  # make pyflakes happy...
