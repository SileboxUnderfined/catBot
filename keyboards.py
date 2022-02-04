from vk_api.keyboard import *
def startKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Хочу кота",color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    return keyboard.get_keyboard()