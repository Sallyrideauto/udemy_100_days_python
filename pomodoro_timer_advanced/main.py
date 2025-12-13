import timer_setting as s
from timer_ui import PomodoroUI
from timer_function import TimerFunction

def main():
    ui = PomodoroUI(s)

    engine = TimerFunction(
        after=ui.window.after,
        after_cancel=ui.window.after_cancel,
        settings=s,
        on_tick=ui.set_time,
        on_session_change=ui.set_session,
        on_marks_change=ui.set_marks
    )

    ui.bind_start(engine.start)
    ui.bind_reset(engine.reset)

    ui.run()

if __name__ == "__main__":
    main()