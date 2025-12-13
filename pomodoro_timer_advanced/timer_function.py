import math

class TimerFunction:
    """
    - manage reps
    - decide session(Work/Short Break/Long Break)
    - manage countdown scheduling(after)
    - UI update by call-back
    """
    def __init__(self, after, after_cancel, settings, on_tick, on_session_change, on_marks_change):
        """
        :param after: window.after of Tk
        :param after_cancel: window.after_cancel of Tk
        :param settings: timer_setting module
        :param on_tick(min_str, sec_str): deliver time to UI per sec
        :param on_session_change(title, color): deliver Work/Break status
        :param on_marks_change(marks): deliver checkmark string
        """
        self.after = after
        self.after_cancel = after_cancel
        self.s = settings

        self.on_tick = on_tick
        self.on_session_change = on_session_change
        self.on_marks_change = on_marks_change

        self.reps = 0
        self._timer_id = None

    def reset(self):
        if self._timer_id is not None:
            self.after_cancel(self._timer_id)
            self._timer_id = None

        self.reps = 0
        self.on_tick("00", "00")
        self.on_session_change("Pomodoro", self.s.COTTON_ROSE)
        self.on_marks_change("")

    def start(self):
        self.reps += 1

        work_sec = self.s.WORK_MIN * 60
        short_break_sec = self.s.SHORT_BREAK_MIN * 60
        long_break_sec = self.s.LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.on_session_change("Break", self.s.SWEET_PEONY)
            self._count_down(long_break_sec)
        elif self.reps % 2 == 0:
            self.on_session_change("Break", self.s.PINK_CARNATION)
            self._count_down(short_break_sec)
        else:
            self.on_session_change("Work", self.s.DRY_SAGE)
            self._count_down(work_sec)

    def _count_down(self, count):
        count_min = count // 60
        count_sec = count % 60

        self.on_tick(f"{count_min:02d}", f"{count_sec:02d}")

        if count > 0:
            self._timer_id = self.after(1000, self._count_down, count - 1)
        else:
            # End session and start next session
            self._update_marks()
            self.start()

    def _update_marks(self):
        work_sessions = math.floor(self.reps / 2)
        marks = "✔" * work_sessions
        self.on_marks_change(marks)