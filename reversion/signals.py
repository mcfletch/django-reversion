from django.dispatch.dispatcher import Signal


_signal_args = [
    "revision",
    "versions",
]

pre_revision_commit = Signal()
post_revision_commit = Signal()
