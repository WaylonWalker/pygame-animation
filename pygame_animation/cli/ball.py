import random
import sys

import pygame
import typer

from pygame_animation.cli.common import verbose_callback

ball_app = typer.Typer()


@ball_app.callback()
def ball(
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="run the ball annimation",
    ),
):
    "ball cli"


@ball_app.command()
def run(
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
    ball_radius: int = typer.Option(20),
    restitution: int = typer.Option(-2),
    gravity: int = typer.Option(5),
    friction: int = typer.Option(0.9),
):

    pygame.init()

    # Set up the display
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncing Ball Animation")

    # Set up the ball
    ball_color = (255, 255, 255)
    ball_x = screen_width // 2
    ball_y = screen_height // 2
    ball_speed_x = random.randint(-5, 5)
    ball_speed_y = random.randint(-5, 5)
    squishyness = 100

    # Set up the clock
    clock = pygame.time.Clock()

    # Run the game loop
    while True:
        squish = 0
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the ball position
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Check for collisions with the walls
        if ball_x + ball_radius >= screen_width or ball_x - ball_radius <= 0:
            ball_speed_x = -ball_speed_x

        if ball_y + ball_radius >= screen_height or ball_y - ball_radius <= 0:
            # restitution
            ball_speed_y = -ball_speed_y - restitution
            # friction
            ball_speed_x *= friction

        if ball_y <= ball_radius:
            ball_y = ball_radius
        if ball_y >= screen_height - ball_radius:
            ball_y = screen_height - ball_radius
        if ball_x <= ball_radius:
            ball_x = ball_radius
        if ball_x >= screen_width - ball_radius:
            ball_x = screen_width - ball_radius

        if ball_y - ball_radius <= 0:
            squish = ball_speed_y * squishyness

        else:
            ball_speed_y += gravity

        # Draw the ball
        screen.fill((0, 0, 0))
        if squish != 0:
            ball_width = ball_radius * (2 + squish)
            ball_height = ball_radius * (2 - squish)
            print(ball_width, ball_height)
            ball_x = ball_x - ball_width // 2
            pygame.draw.ellipse(
                screen,
                ball_color,
                (ball_x, ball_y, ball_width, ball_height),
            )
            # pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

        else:
            pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

        # Update the display
        pygame.display.flip()

        # Wait for a little bit to control the frame rate
        clock.tick(60)
