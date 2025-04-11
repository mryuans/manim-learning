from manimlib import * # type: ignore


class MarkupTextEx(Scene):
    def construct(self) -> None:
        mtext = MarkupText("<span>This is MarkupText</span>.").shift(UP)
        mtext1 = MarkupText("This is <i>italic</i>.").next_to(mtext, DOWN)
        mtext2 = MarkupText("And this is <b>bold</b>.").next_to(mtext1, DOWN)

        self.play(LaggedStart(*(
            Write(mtext),
            Write(mtext1),
            Write(mtext2),
        ), run_time=5, lag_ratio=0.3))


class CodeEx(Scene):
    def construct(self) -> None:
        codeblock = Code(
            r'''
            from manimlib import *
            
            
            class Text(Scene): 
                text = Text("Hello World")
            '''
        )
        self.play(Write(codeblock))

