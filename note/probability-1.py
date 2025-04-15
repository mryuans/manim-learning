from manimlib import *


class Dis(InteractiveScene):
    dice_ex = DieFace(6)
    dice = VGroup(*(DieFace(num) for num in np.random.randint(1, 7, 20)))
    def construct(self) -> None:
        title = Title("Probability-1")
        text1 = Text("Let's make it change its number randomly with your left button", font_size=30).to_edge(DOWN)
        
        self.play(
            Write(title),
            DrawBorderThenFill(self.dice_ex)
        )

        self.play(Write(text1))
    def on_mouse_press(self, point, button: int, mods) -> None:
        if button == 1:
            if self.dice_ex in self.mobjects:
                self.remove(self.dice_ex)
            dice_cg = self.dice.copy()
            for dice_ in dice_cg:
                dice_.shift(np.random.uniform(-0.1, 0.1, 3))
            self.play(ShowSubmobjectsOneByOne(dice_cg), run_time=2)
            self.wait(0.5)
            self.remove(dice_cg)

