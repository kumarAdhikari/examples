from dataclasses import dataclass, replace


@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


def frame_text(text: str, frame: Frame) -> str:
    def topline():
        print(fancy_frame.top_left, end='')
        for x in range(1, len(text) + 1):
            print(fancy_frame.top, end="")
        print(fancy_frame.top_right, end='')

    def bottomline():
        print(fancy_frame.bottom_left, end='')
        for x in range(1, len(text) + 1):
            print(fancy_frame.top, end="")
        print(fancy_frame.bottom_right, end='')

    ff = f"{topline()}{print()}{print(fancy_frame.left, end='')}{print({str(text)} , end='')}{print(fancy_frame.right, end='')}{print()}{bottomline()}"

    return ff

frame_text("Lorem ipsum", Frame())