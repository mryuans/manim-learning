from manimlib import *


class SamplingEx(Scene):
    def construct(self) -> None:
        # 1. 创建基础样本空间并设置标题
        space = SampleSpace(
            height=3,
            width=5,
            fill_color=GREY_D,
            stroke_color=GREY_B,
            stroke_width=0.5,
        )
        space.add_title("Probability Sample Space")
        self.play(DrawBorderThenFill(space))
        self.wait()

        # 2. 创建水平分区
        space.divide_horizontally(
            p_list=[0.6, 0.4],
            colors=[GREEN_E, BLUE_E]
        )
        # 添加左侧标签
        braces_labels = space.get_side_braces_and_labels(["P(A)", "P(\\neg A)"])
        self.play(
            *[GrowFromCenter(brace) for brace in braces_labels[0]],
            *[Write(label) for label in braces_labels[1]]
        )
        self.wait()

        # 3. 在第二部分添加垂直分区
        space.divide_vertically(
            p_list=[0.5, 0.5],
            colors=[MAROON_B, YELLOW],
            vect=RIGHT
        )
        # 添加顶部标签
        top_braces_labels = space.get_bottom_braces_and_labels(["B", "\\neg B"])
        self.play(
            *[GrowFromCenter(brace) for brace in top_braces_labels[0]],
            *[Write(label) for label in top_braces_labels[1]]
        )
        self.wait()

        # 4. 创建新的样本空间展示其他功能
        self.play(FadeOut(space), FadeOut(VGroup(*braces_labels, *top_braces_labels)))
        
        new_space = SampleSpace(
            height=4,
            width=6,
            fill_opacity=0.7
        )
        new_space.add_title("Multiple Partitions")
        self.play(DrawBorderThenFill(new_space))

        # 5. 创建三等分垂直分区
        new_space.divide_vertically(
            p_list=[0.3, 0.3, 0.4],
            colors=[BLUE, GREEN, RED]
        )
        vert_labels = new_space.get_top_braces_and_labels(
            ["X", "Y", "Z"],
            buff=SMALL_BUFF
        )
        self.play(
            *[GrowFromCenter(brace) for brace in vert_labels[0]],
            *[Write(label) for label in vert_labels[1]]
        )
        self.wait()

        # 6. 在中间部分添加水平分区
        new_space.vertical_parts[1].divide_horizontally(
            p_list=[0.7, 0.3],
            colors=[YELLOW_B, PURPLE_A]
        )
        self.wait(2)

        # 7. 创建一个条形图来对比概率
        chart = BarChart(
            values=[0.3, 0.3, 0.4],
            bar_names=["X", "Y", "Z"],
            y_axis_label_height=0.2,
            bar_colors=[BLUE, GREEN, RED]
        )
        chart.next_to(new_space, DOWN, buff=1)
        self.play(ShowCreation(chart))
        self.wait(2)
