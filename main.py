__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
import random


# =========================================================
# INNER PATH
# ANDROID VERSION
# =========================================================

BG = "#090b14"
WHITE = "#f4f4f7"
SOFT = "#b8bdcc"

GREEN = "#39d353"
RED = "#ff3b5c"
BLUE = "#3b82f6"
PINK = "#ff69b4"

GREEN_DARK = "#07150d"
RED_DARK = "#19080c"
BLUE_DARK = "#07111f"
PINK_DARK = "#190914"


def hex_color(value):
    value = value.lstrip("#")

    return tuple(
        int(value[i:i+2], 16) / 255
        for i in (0, 2, 4)
    ) + (1,)


questions = [

    {
        "question":
        "When you face a difficult decision, what do you trust the most?",
        "answers": [
            ("What I believe is right, even if it makes things harder for me.", "green"),
            ("What I feel in that moment, even if I cannot fully explain it.", "red"),
            ("What makes the most sense after considering every possible outcome.", "blue"),
            ("What feels right when I consider how my decision will affect others.", "pink")
        ]
    },

    {
        "question":
        "When something important in your life comes to an end, what is hardest for you to accept?",
        "answers": [
            ("That something I believed in may never become what I imagined.", "green"),
            ("That I cannot simply turn off what I felt.", "red"),
            ("That I may never fully understand why it had to happen.", "blue"),
            ("That I may have to continue without someone who mattered to me.", "pink")
        ]
    },

    {
        "question":
        "When someone misunderstands who you really are, how do you usually respond?",
        "answers": [
            ("I let them believe what they want and continue being myself.", "green"),
            ("It affects me more than I usually allow them to see.", "red"),
            ("I try to understand why they reached that conclusion.", "blue"),
            ("I wish they could see the part of me I was trying to show them.", "pink")
        ]
    },

    {
        "question":
        "Which statement feels closest to the way you see life?",
        "answers": [
            ("People can become someone completely different from who they are today.", "green"),
            ("The moments we feel most deeply are often the ones we remember longest.", "red"),
            ("There is usually more to the truth than what first appears.", "blue"),
            ("The meaning of our lives is deeply connected to the people we touch.", "pink")
        ]
    },

    {
        "question":
        "If you had to choose between protecting your peace and doing what you believe is right, what would you most likely do?",
        "answers": [
            ("I would choose what could lead to something better in the long run.", "green"),
            ("I would choose what I could not forgive myself for ignoring.", "red"),
            ("I would first question whether my idea of 'right' is actually justified.", "blue"),
            ("I would think about who might be affected before making the choice.", "pink")
        ]
    },

    {
        "question":
        "When you think about your past, what do you find yourself doing most often?",
        "answers": [
            ("I think about how everything I experienced shaped who I could become.", "green"),
            ("I remember how certain moments made me feel.", "red"),
            ("I replay events and wonder what I could have understood differently.", "blue"),
            ("I remember the people connected to those moments more than the events themselves.", "pink")
        ]
    },

    {
        "question":
        "Imagine you could know exactly what your future holds. Would you want to know?",
        "answers": [
            ("No. I would rather create the future than be told what it will be.", "green"),
            ("Only if knowing it would help me protect something I deeply care about.", "red"),
            ("Yes. Understanding what is coming would help me prepare for it.", "blue"),
            ("Only if it would help me know whether the people I care about will still be there.", "pink")
        ]
    },

    {
        "question":
        "When you look at the person you are becoming, what matters to you most?",
        "answers": [
            ("Becoming someone who can create a life that feels meaningful.", "green"),
            ("Becoming someone who never becomes afraid of feeling deeply.", "red"),
            ("Becoming someone who understands themselves and the world around them.", "blue"),
            ("Becoming someone capable of giving and receiving something genuine.", "pink")
        ]
    }
]


results = {

    "green": {
        "title": "THE DREAMER",
        "color": GREEN,
        "background": GREEN_DARK,
        "text":
        "You tend to look beyond what something is and toward what it could become. "
        "You are drawn to possibilities, new beginnings, and the idea that a person is never completely defined by their past. "
        "Even when you do not know where a decision will lead, you can find meaning in taking the first step. "
        "You may sometimes expect too much from the future, or keep believing in possibilities long after others have stopped. "
        "But that same quality allows you to see doors where other people only see walls. "
        "You do not simply search for a path. "
        "A part of you wants to become the person who creates one. "
        "Your greatest strength is the ability to believe that something different is still possible.",
        "poem":
        "A seed beneath the silent ground,\n"
        "knows not the shape of what will be.\n"
        "Yet somewhere past the dark,\n"
        "it dreams of becoming a tree."
    },

    "red": {
        "title": "THE FLAME",
        "color": RED,
        "background": RED_DARK,
        "text":
        "You experience many things more intensely than you allow people to see. "
        "When something matters to you, it rarely remains something ordinary. "
        "You can become deeply attached to people, ideas, memories, and moments that others might consider insignificant. "
        "This gives you an unusual ability to care, commit, and keep moving when something truly matters. "
        "But intensity has its cost. "
        "You may hold onto things because letting go feels like admitting that they never mattered. "
        "Sometimes you protect your feelings by hiding them, and sometimes you protect what you love by carrying more than you should. "
        "Your strength is not that you never burn. "
        "It is that even after being hurt, something inside you still knows how to care.",
        "poem":
        "I carried the fire in my hands,\n"
        "though I knew it could leave scars.\n"
        "Some flames are not meant to warm the night—\n"
        "they remind us who we are."
    },

    "blue": {
        "title": "THE LOST SEA",
        "color": BLUE,
        "background": BLUE_DARK,
        "text":
        "Your mind rarely accepts the first answer it receives. "
        "You tend to look beneath words, actions, and explanations, searching for the part that has not yet been understood. "
        "You may spend more time than others thinking about decisions that have already been made, imagining different outcomes and questioning what they meant. "
        "This depth can make you perceptive, analytical, and difficult to deceive. "
        "But the same mind that helps you understand the world can sometimes make it difficult to simply live in the moment. "
        "You may search for certainty in places where certainty does not exist. "
        "Perhaps your greatest challenge is learning that not every unanswered question is a problem that needs to be solved. "
        "Some truths become clearer only after we stop chasing them.",
        "poem":
        "I searched beneath the quiet waves,\n"
        "for answers the surface could not keep.\n"
        "Perhaps I was never truly lost,\n"
        "only deeper than the world could see."
    },

    "pink": {
        "title": "THE HEART",
        "color": PINK,
        "background": PINK_DARK,
        "text":
        "You naturally give meaning to the connections between people. "
        "For you, a decision is rarely only about yourself; somewhere in your thoughts is the question of who might be affected by it. "
        "You remember voices, small gestures, conversations, and moments that other people might forget. "
        "This sensitivity can make you deeply understanding and loyal, but it can also make distance and loss harder for you than you let others know. "
        "You may sometimes give more of yourself than you receive, because caring feels more natural to you than keeping score. "
        "Your strength is your ability to make people feel seen and remembered. "
        "But remember that understanding others should never require you to disappear inside their needs. "
        "A heart can remain open without belonging entirely to someone else.",
        "poem":
        "Some hearts leave without a sound,\n"
        "yet their echoes never fade.\n"
        "Perhaps love is not what stays,\n"
        "but what changes us when it leaves."
    }
}


class BackgroundWidget(BoxLayout):

    def __init__(self, bg_color=BG, **kwargs):

        super().__init__(**kwargs)

        self.bg_color = bg_color

        with self.canvas.before:

            Color(
                *hex_color(bg_color)
            )

            self.rect = Rectangle(
                pos=self.pos,
                size=self.size
            )

            Color(
                1,
                1,
                1,
                0.12
            )

            self.circle = Ellipse(
                pos=(0, 0),
                size=(dp(240), dp(240))
            )

        self.bind(
            pos=self.update_graphics,
            size=self.update_graphics
        )

    def update_graphics(self, *args):

        self.rect.pos = self.pos
        self.rect.size = self.size

        self.circle.pos = (
            self.width * 0.50 - dp(120),
            self.height * 0.55
        )


class BaseScreen(Screen):

    def make_label(
        self,
        text,
        size,
        color=WHITE,
        bold=False
    ):

        label = Label(
            text=text,
            color=hex_color(color),
            font_size=dp(size),
            bold=bold,
            halign="center",
            valign="middle"
        )

        label.bind(
            size=lambda obj, value:
            setattr(
                obj,
                "text_size",
                value
            )
        )

        return label


class WelcomeScreen(BaseScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.build_ui()

    def build_ui(self):

        root = BackgroundWidget(
            bg_color=BG,
            orientation="vertical",
            padding=[
                dp(28),
                dp(40),
                dp(28),
                dp(40)
            ],
            spacing=dp(18)
        )

        root.add_widget(
            WidgetSpacer()
        )

        title = self.make_label(
            "INNER PATH",
            30,
            WHITE,
            True
        )

        root.add_widget(
            title
        )

        subtitle = self.make_label(
            "PERSONALITY TEST",
            15,
            SOFT
        )

        root.add_widget(
            subtitle
        )

        description = self.make_label(
            "Discover what lies within your choices.",
            14,
            "#858b9e"
        )

        root.add_widget(
            description
        )

        begin = Button(
            text="BEGIN",
            size_hint_y=None,
            height=dp(58),
            background_normal="",
            background_color=hex_color("#20263a"),
            color=hex_color(WHITE),
            font_size=dp(16),
            bold=True
        )

        begin.bind(
            on_release=self.start
        )

        root.add_widget(
            begin
        )

        root.add_widget(
            WidgetSpacer()
        )

        self.add_widget(root)

    def start(self, *args):

        app = App.get_running_app()

        app.reset_test()

        app.sm.current = "question"


class WidgetSpacer(Widget):
    pass


class QuestionScreen(BaseScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.layout = None

        self.build_ui()

    def build_ui(self):

        self.layout = BackgroundWidget(
            bg_color=BG,
            orientation="vertical",
            padding=[
                dp(20),
                dp(35),
                dp(20),
                dp(35)
            ],
            spacing=dp(20)
        )

        self.add_widget(
            self.layout
        )

    def refresh(self):

        self.layout.clear_widgets()

        app = App.get_running_app()

        index = app.current_question

        question = questions[index]

        number = self.make_label(
            "QUESTION "
            + str(index + 1)
            + " / 8",
            12,
            SOFT
        )

        number.size_hint_y = None
        number.height = dp(40)

        self.layout.add_widget(
            number
        )

        title = self.make_label(
            "YOUR QUESTION",
            23,
            WHITE,
            True
        )

        title.size_hint_y = None
        title.height = dp(60)

        self.layout.add_widget(
            title
        )

        q = self.make_label(
            question["question"],
            19,
            WHITE,
            True
        )

        q.size_hint_y = None
        q.height = dp(145)

        self.layout.add_widget(
            q
        )

        self.layout.add_widget(
            WidgetSpacer()
        )

        for answer, color_name in question["answers"]:

            colors = {
                "green": "#122a18",
                "red": "#301016",
                "blue": "#10213c",
                "pink": "#301225"
            }

            button = Button(
                text=answer,
                size_hint_y=None,
                height=dp(86),
                background_normal="",
                background_color=hex_color(
                    colors[color_name]
                ),
                color=hex_color(WHITE),
                font_size=dp(13),
                bold=True
            )

            button.bind(
                on_release=lambda btn,
                c=color_name:
                self.answer(c)
            )

            self.layout.add_widget(
                button
            )

    def answer(self, color):

        app = App.get_running_app()

        app.scores[color] += 1

        if app.current_question < 7:

            app.current_question += 1

            self.refresh()

        else:

            app.show_result()


class ResultScreen(BaseScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.layout = None

        self.build_ui()

    def build_ui(self):

        self.layout = BackgroundWidget(
            bg_color=BG,
            orientation="vertical",
            padding=[
                dp(24),
                dp(35),
                dp(24),
                dp(40)
            ],
            spacing=dp(15)
        )

        self.add_widget(
            self.layout
        )

    def refresh(self):

        self.layout.clear_widgets()

        app = App.get_running_app()

        winner = app.get_winner()

        data = results[winner]

        top = self.make_label(
            "YOUR RESULT",
            12,
            SOFT
        )

        top.size_hint_y = None
        top.height = dp(35)

        self.layout.add_widget(
            top
        )

        title = self.make_label(
            data["title"],
            27,
            data["color"],
            True
        )

        title.size_hint_y = None
        title.height = dp(65)

        self.layout.add_widget(
            title
        )

        heart = self.make_label(
            "♥",
            40,
            data["color"]
        )

        heart.size_hint_y = None
        heart.height = dp(60)

        self.layout.add_widget(
            heart
        )

        scroll = ScrollView(
            do_scroll_x=False
        )

        text_box = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            padding=[
                dp(10),
                dp(5),
                dp(10),
                dp(5)
            ]
        )

        text_box.bind(
            minimum_height=text_box.setter(
                "height"
            )
        )

        analysis = self.make_label(
            data["text"],
            15,
            "#e5e7ef"
        )

        analysis.size_hint_y = None
        analysis.height = dp(360)

        text_box.add_widget(
            analysis
        )

        poem = self.make_label(
            data["poem"],
            15,
            data["color"]
        )

        poem.size_hint_y = None
        poem.height = dp(145)

        text_box.add_widget(
            poem
        )

        scroll.add_widget(
            text_box
        )

        self.layout.add_widget(
            scroll
        )

        again = Button(
            text="BEGIN AGAIN",
            size_hint_y=None,
            height=dp(58),
            background_normal="",
            background_color=hex_color("#20263a"),
            color=hex_color(WHITE),
            font_size=dp(15),
            bold=True
        )

        again.bind(
            on_release=self.restart
        )

        self.layout.add_widget(
            again
        )

    def restart(self, *args):

        app = App.get_running_app()

        app.reset_test()

        app.sm.current = "welcome"


class InnerPathApp(App):

    def build(self):

        self.title = "INNER PATH"

        Window.clearcolor = hex_color(BG)

        self.current_question = 0

        self.scores = {
            "green": 0,
            "red": 0,
            "blue": 0,
            "pink": 0
        }

        self.sm = ScreenManager(
            transition=FadeTransition(
                duration=0.18
            )
        )

        self.welcome = WelcomeScreen(
            name="welcome"
        )

        self.question_screen = QuestionScreen(
            name="question"
        )

        self.result_screen = ResultScreen(
            name="result"
        )

        self.sm.add_widget(
            self.welcome
        )

        self.sm.add_widget(
            self.question_screen
        )

        self.sm.add_widget(
            self.result_screen
        )

        return self.sm

    def reset_test(self):

        self.current_question = 0

        for color in self.scores:

            self.scores[color] = 0

    def get_winner(self):

        priority = [
            "green",
            "red",
            "blue",
            "pink"
        ]

        winner = priority[0]

        for color in priority:

            if self.scores[color] > self.scores[winner]:

                winner = color

        return winner

    def show_result(self):

        self.result_screen.refresh()

        self.sm.current = "result"


if __name__ == "__main__":

    InnerPathApp().run()
