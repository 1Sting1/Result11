from Src.Models.event_type import event_type

class console_logger:
    """
    Наблюдатель, который логгирует сообщения в консоль.
    """

    def handle_event(self, handle_type: str, data: list):
        if handle_type == event_type.write_log():
            for item in data:
                print(f"Log item: {item}")
        elif handle_type == event_type.save_log():
            print("Saving log...")
