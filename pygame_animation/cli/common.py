from pygame_animation.console import console


def verbose_callback(value: bool) -> None:
    if value:
        console.quiet = False
