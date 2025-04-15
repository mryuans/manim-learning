from manimlib import * # type: ignore


class IntereactiveMouse(InteractiveScene):
    def construct(self) -> None:
        title = Title("InteractiveScene")
        self.play(Write(title))

    def on_mouse_press(self, point, button: int, mods: int) -> None:
        if button == 1:
            self.play(Write(Text("Left button? Yes.").move_to(point)))
        if button == 4:
            self.play(Write(Text("Right button? Yes.").move_to(point)))

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        char = chr(symbol)
        if char == " ":
            self.play(Write(Text("BlankSpace? Yes.").to_edge(BOTTOM)))



