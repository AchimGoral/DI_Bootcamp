class Phone:

    def __init__(self, number):
        self.number = number
        self.call_history = []
        self.messages = []


    def call(self, other_phone):
        self.call_history.append(other_phone)

    def show_call_history(self):
        for item in self.call_history:
            print(f"Number: {item}")

    def send_message(self, other_phone, message):
        new_dict = {}
        self.messages.append(message)
        new_dict["from"] = self.number
        new_dict["to"] = other_phone
        new_dict["message"] = message
        return new_dict

    def show_outgoing_messages(self):
        out_msg = self.send_message(other_phone = 0, message = "")
        for item in out_msg:
            print(item)

    def show_incoming_messages(self):
        pass

    def show_messages_from(self, number):
        pass



phone = Phone(56554554656)
phone.call(6454879988)
phone.call(458444654565)
phone.show_call_history()
print(phone.send_message(4566161514654, "Hello"))
phone.show_outgoing_messages()